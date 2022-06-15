#!/usr/bin/env python
import codecs
import io
import json
import logging
import shutil
import subprocess
import sys

import requests
import zipfile
import os

from config import BASE_DIR, CODEQL_THREADS, VERBOSITY, SCRATCH_DIR, RAM
from src.Database import Database


class Worker:
    jid = "0"  # Job id
    projectname = ""  # Name of the project currently being analysed
    username = ""  # GitHub username
    url = ""  # download url
    language = ""  # Programming language
    database = None
    pid = ''  # Process id
    ready = True

    def __init__(self):
        # instantiate Worker
        self.database = Database()
        self.database.close()
        self.pid = str(os.getpid())
        logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO,
                            datefmt="%H:%M:%S")

    def to_string(self):
        # return String representation of current job
        if self.jid == '0':
            return 'Process ' + self.pid
        else:
            return "Job #" + self.jid + " (" + self.projectname + " by " + self.username + ")"

    def _info(self, message: str, level=logging.INFO):
        # Print info message
        if level == logging.ERROR:
            logging.error(self.to_string() + ": " + message)
        elif level == logging.CRITICAL:
            logging.critical(self.to_string() + ": " + message)
        else:
            logging.info(self.to_string() + ": " + message)

    def run(self):
        self._info("Hi there :)")
        # Run Jobs until no job available
        while self.ready:
            # instantiate and run Job from Job queue in database
            if self._load_job():
                self._info("Starting Job")
                if self._download_and_unzip():
                    self.remove_typescript_files()
                    if self._create_codeql_database():  # False if error creating db
                        if self._analyse_codeql_database():  # False if error analyzing db
                            self._safe_result()
                            # self.ready = False
                    self._clean_up()

    def _load_job(self):
        # Load job from database and safe Job config
        self.database.open()
        job = self.database.fetch_job(self.pid)
        self.database.close()
        if job == 1:
            self.ready = False
            self._info("No more jobs in queue. Bye.")
            return False
        elif job is None:
            self._info("Fatal error: database connection failed")
            sys.exit()
        else:
            self._setup(job[0], job[1], job[2], job[3], job[4])
            return True

    def _setup(self, jid: int, username: str, projectname: str, url: str, language: str):
        # Instantiate Job with given variables
        self.jid = str(jid)
        self.username = username
        self.projectname = projectname
        self.url = url
        # only some languages supported by codeql
        if language in {"cpp", "csharp", "go", "java", "javascript", "python", "ruby"}:
            self.language = language
        else:
            self._handle_fatal_error("The following programming language is not supported: " + language)

    def _download_and_unzip(self):
        self._info("Starting download")
        # Download zip from url
        dir_unzip = SCRATCH_DIR + "/data/" + self.jid
        try:
            r = requests.get(self.url)
            if r.ok:
                z = zipfile.ZipFile(io.BytesIO(r.content))
                self._info("starting unzip")
                z.extractall(dir_unzip)
                z.close()
                r.close()
                return True
            else:
                self._handle_warning_error("Could not download project (Status: " + str(r.status_code) + "): Reason: " +
                                           r.reason, -3)
                return False
        except (Exception, requests.RequestException) as error:
            self._handle_warning_error(str(error), -3)
            return False

    def remove_typescript_files(self):
        for f in [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(SCRATCH_DIR + "/data/" + self.jid)) for f in fn]:
            if not os.path.isdir(f):
                if f.endswith('.ts') or f.endswith('.tsx'):
                    os.remove(f)

    def _download(self):
        # deprecated
        self._info("Starting download")
        # Download zip from url
        filename = self.jid + ".zip"

        try:
            r = requests.get(self.url)
            if r.ok:
                open(SCRATCH_DIR + "/downloads/" + filename, 'wb').write(r.content)
                r.close()
                self._info("Download successful")
            else:
                raise Exception("Could not download project (Status: " + r.status_code + "): Reason: " + r.reason)
        except (Exception, requests.RequestException) as error:
            self._handle_fatal_error(str(error))

    def _unzip_project(self):
        # unzip dir
        # deprecated
        self._info("Starting unzip")
        file_zip = SCRATCH_DIR + "/downloads/" + self.jid + ".zip"
        dir_unzip = SCRATCH_DIR + "/data/" + self.jid
        try:
            with zipfile.ZipFile(file_zip) as z:
                z.extractall(dir_unzip)
                z.close()
                self._info("unzip successful")
        except (Exception, zipfile.BadZipFile) as error:
            self._handle_fatal_error(str(error))

    def _create_codeql_database(self):
        # Create CodeQL Database
        db_name = SCRATCH_DIR + "/codeql/" + self.jid
        source_root = SCRATCH_DIR + "/data/" + self.jid
        self._info("Starting to create codeql database")
        codeql = subprocess.run(
            [BASE_DIR + '/libraries/codeql/codeql', "database", "create", db_name,
             "--source-root=" + source_root, "--language=" + self.language, '--verbosity='+VERBOSITY, '--overwrite',
             "--ram="+RAM
             ]
        )
        if codeql.returncode != 0:  # Error creating db
            print(codeql.stdout)
            self._handle_warning_error('Error Creating CodeQL Database Status: ' + str(codeql.returncode))
            return False
        self._info("Finished creating codeql database")
        return True

    def _analyse_codeql_database(self, output_format='sarifv2.1.0', file_format='sarif', suite='-security-extended.qls'):
        db = SCRATCH_DIR + "/codeql/" + self.jid
        # CodeQL query suite currently hardcoded to CWE-079
        suite = BASE_DIR + "/libraries/codeql-repo/" + self.language + "/ql/src/codeql-suites/" + self.language + suite
        output = BASE_DIR + "/results/" + self.jid + '.' + file_format
        self._info("Starting to analyze codeql database")
        codeql = subprocess.run(
            [BASE_DIR + '/libraries/codeql/codeql', "database", "analyze", db, "--format=" + output_format,
             "--output=" + output, "--threads=" + CODEQL_THREADS, "--verbosity=" + VERBOSITY, "--ram=" + RAM,
             BASE_DIR + "/libraries/codeql-repo/javascript/ql/src/Security/CWE-079"
             ]
        )
        if codeql.returncode != 0:
            self._handle_warning_error('Error Analyzing CodeQL Database Status: ' + str(codeql.returncode))
            return False
        self._info("Finished analyzing codeql database")
        return True

    def _clean_up(self):
        # remove working dirs
        shutil.rmtree(SCRATCH_DIR + "/data/" + self.jid)
        shutil.rmtree(SCRATCH_DIR + "/codeql/" + self.jid)

    def _safe_result(self):
        # push results to database
        f = open(BASE_DIR + "/results/" + self.jid + ".sarif", "r", encoding='utf-8')
        c = f.read()
        j = json.loads(c)
        result = j["runs"][0]["results"]
        self.database.open()
        self.database.digest_results(self.jid, result)
        self.database.set_job_status(self.jid, "1")
        self.database.close()

    def _handle_warning_error(self, error, status=-2):
        # exit after fatal error
        self._info(error, logging.ERROR)
        self._info('Abort job and load new one')
        self.database.open()
        self.database.set_job_status(self.jid, status)
        self.database.close()

    def _handle_fatal_error(self, error):
        # exit after fatal error
        self._info(error, logging.ERROR)
        self.database.open()
        self.database.set_job_status(self.jid, -1)
        self.database.close()
        self._info("End execution after fatal error. Bye.")
        sys.exit(1)

    def safe_result(self, jid):
        # push results to database
        self.jid = str(jid)
        f = open(BASE_DIR + "/results/" + self.jid + ".sarif", "r", encoding='utf-8')
        c = f.read()
        j = json.loads(c)
        result = j["runs"][0]["results"]
        self.database.open()
        self.database.digest_results(self.jid, result)
        self.database.set_job_status(self.jid, "1")
        self.database.close()

