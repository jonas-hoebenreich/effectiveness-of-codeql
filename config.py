#!/usr/bin/env python
import datetime
import os

# TODO: insert DB connection parameters
POSTGRES = {
    "host": "",
    "user": "",
    "database": "postgres",
    "password": "",
    "port": 5432,
    'environment': "jsample"  # sql schema
}

INTERVAL_RELEASES = 7
GITHUB_TOKEN = []  # insert GitHub token here (supports array of multiple GitHub tokens)
CODEQL_THREADS = '6'
VERBOSITY = 'warnings'  # allowed: errors, warnings, progress, progress+, progress++, progress+++
BASE_DIR = os.getcwd()  # no slash at the end
SCRATCH_DIR = os.getcwd() + '/scratch'  # no slash at the end
RAM = "5923"  # max codeql ram in mb
CODEQL_DEFAULT_PATH = '.github/workflows/codeql-analysis.yml'


RANDOM_SAMPLE_MIN = 0  # or 0, 162000000 created 2018-12-16T12:43:34Z
RANDOM_SAMPLE_MAX = 462000000  # created 2022-02-21T19:18:28Z
CUTOFF_DATE = datetime.date(2020, 9, 30)
