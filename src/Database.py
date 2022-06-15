import json
import time

import config as cfg
import psycopg2


# Database class to talk to the database
# All the functions of this class expect sanitized input!
class Database:
    conn = None
    cursor = None

    # initalize class
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database=cfg.POSTGRES["database"],
                user=cfg.POSTGRES["user"],
                password=cfg.POSTGRES["password"],
                host=cfg.POSTGRES["host"],
                port=cfg.POSTGRES["port"],
                connect_timeout=10
            )
            self.cursor = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    # close db connection
    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Database Error close", error)

    # connect to db
    def open(self):
        self.conn = psycopg2.connect(
            database=cfg.POSTGRES["database"],
            user=cfg.POSTGRES["user"],
            password=cfg.POSTGRES["password"],
            host=cfg.POSTGRES["host"],
            port=cfg.POSTGRES["port"],
            connect_timeout=60
        )
        self.cursor = self.conn.cursor()

    # load pending job form database
    def fetch_job(self, pid):
        # load job from database
        record = None
        try:
            # Set status of 1 waiting job to process id
            sql = "UPDATE " + cfg.POSTGRES["environment"] + ".jobs " + \
                  "SET status = " + pid + \
                  " WHERE id = (SELECT id " \
                  "FROM " + cfg.POSTGRES["environment"] + ".jobs " \
                                                          "WHERE status = 0 " \
                                                          "LIMIT 1 FOR UPDATE SKIP LOCKED) " + \
                  "RETURNING id;"
            self.cursor.execute(sql)
            self.conn.commit()
            job_id = self.cursor.fetchone()
            if job_id is None:
                return 1
            sql = """SELECT 
                        j.id as jid,
                        username, 
                        projectname, 
                        url, 
                        language
                    FROM 
                      """ + cfg.POSTGRES["environment"] + """.projects p
                          INNER JOIN
                              """ + cfg.POSTGRES["environment"] + """.jobs j 
                          ON 
                              p.gid = j.gid
                    WHERE
                        j.id = %s;"""
            self.cursor.execute(sql, job_id)
            self.conn.commit()
            record = self.cursor.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.try_again()
            return self.fetch_job(pid)
        return record

    # update job Status
    def set_job_status(self, jid, status):
        # update status of job jid
        try:
            sql = "UPDATE " + cfg.POSTGRES["environment"] + ".jobs SET status = %s WHERE id = %s"
            self.cursor.execute(sql, (str(status), str(jid)))
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            time.sleep(30)  # try again in 30 seconds
            self.try_again()
            return self.set_job_status(jid, status)

    # safe CodeQL results to database
    def digest_results(self, jid, results):
        # Safe results from sarif codeql output to db
        for result in results:
            self.add_result(jid, result)

    # add single finding to results table
    def add_result(self, jid, result):
        sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".results (jid, ruleid, ruleindex, message, locations, " \
                                                             "data) VALUES (%s, %s, %s, '-', %s, %s)"
        try:
            self.cursor.execute(sql, (jid,
                                      result["ruleId"],
                                      result["ruleIndex"],
                                      json.dumps(result["locations"]),
                                      json.dumps(result),
                                      )
                                )
            self.conn.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print('ERROR add_result', error)
            time.sleep(30)
            self.try_again()
            return self.add_result(jid, result)

    # create a new pending job
    def enqueue_job(self, gid, url, published):
        # Add job to queue if it does not yet exist
        sql = "SELECT count(*) FROM " + cfg.POSTGRES["environment"] + ".jobs " \
                                                                      "WHERE gid = %s AND url = %s;"
        self.cursor.execute(sql, (gid, url))
        not_enqueued = self.cursor.fetchone()[0]

        if not_enqueued == 0:
            sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".jobs (gid, url, published) " \
                                                                 "VALUES (%s, %s, %s);"
            self.cursor.execute(sql, (gid, url, published))
            self.conn.commit()

    # add new repository to projects table
    def add_project(self, username, projectname, language='', status=1, gid=None, uses_codeql=-1):
        if self.check_project_exists(gid, username, projectname):
            try:
                sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".projects" \
                                                                     " (gid, username, projectname, language, status, uses_codeql) " \
                                                                     "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"
                self.cursor.execute(sql, (str(gid), username, projectname, language, str(status), str(uses_codeql)))
                self.conn.commit()
                return self.cursor.fetchone()
            except Exception as error:
                print(error)
                return '0'
        else:
            print('projects exists:', str(gid), username, projectname, language, str(status), str(uses_codeql))
            return '0'  # TODO

    # check if a project with the same username/projectname already in table
    def check_project_exists(self, gid, username='', projectname=''):
        # add project to projects if it does not yet exist
        sql = "SELECT id FROM " + cfg.POSTGRES["environment"] + ".projects " \
                                                                "WHERE gid = %s OR (username = %s AND projectname = %s);"
        self.cursor.execute(sql, (gid, username, projectname))
        exists = self.cursor.fetchone()
        return exists is None or exists[0] == 0

    # add rule to rules table
    def add_rule(self, rule_id, shortdescription, description, kind, precision, problem_severity, security_severity,
                 tags):
        # Add codeql rule to db
        sql = "SELECT count(*) FROM " + cfg.POSTGRES["environment"] + ".rules " \
                                                                      "WHERE rule_id = '" + rule_id + "';"
        self.cursor.execute(sql)
        exists = self.cursor.fetchone()[0]

        if exists == 0:
            sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".rules " \
                                                                 "(rule_id, shortdescription, description, kind, precision, problem_severity, security_severity, tags) " \
                                                                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            self.cursor.execute(sql, (
                rule_id, shortdescription, description, kind, precision, problem_severity, security_severity, tags))
            self.conn.commit()

    # get repository and set new status
    def fetch_and_update_project(self, status=0, newstatus=1):
        # fetch one project and set new status
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".projects " + \
              "SET status = " + str(newstatus) + \
              "WHERE id = (SELECT id " \
              "FROM " + cfg.POSTGRES["environment"] + ".projects " \
                                                      "WHERE status = " + str(status) + \
              " LIMIT 1 FOR UPDATE SKIP LOCKED) " + \
              "RETURNING *;"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchone()

    # set repository status
    def update_project_status_gid(self, gid, newstatus=1):
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".projects " + \
              "SET status = " + str(newstatus) + \
              "WHERE gid = " + str(gid) + ";"
        self.cursor.execute(sql)
        self.conn.commit()

    # get a project and remove it from project table
    def fetch_and_remove_project(self, status=-1):
        # fetch one project and remove it from db
        sql = "DELETE FROM " + cfg.POSTGRES["environment"] + ".projects" + \
              " WHERE status = " + str(status) + \
              " AND id = (SELECT id FROM " + cfg.POSTGRES["environment"] + ".projects WHERE status = " + str(
            status) + "LIMIT 1)" + \
              " RETURNING *;"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchone()

    # set new repository status
    def update_project_status(self, gid: int, newstatus: int):
        # update project status
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".projects" + \
              " SET status = " + str(newstatus) + \
              " WHERE id = " + str(gid)
        self.cursor.execute(sql)
        self.conn.commit()

    # get project where uses_codeql is null
    def fetch_project_by_uses_codeql(self):
        # fetch projects where uses_codeql is null
        sql = "SELECT * FROM " + cfg.POSTGRES["environment"] + ".projects " + \
              "WHERE uses_codeql is null;"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchone()

    # set uses_codeql for a repository
    def update_project_uses_codeql(self, gid: int, uses_codeql: int):
        # update uses_codeql of a projects
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".projects" + \
              " SET uses_codeql = " + str(uses_codeql) + \
              " WHERE gid = " + str(gid)
        self.cursor.execute(sql)
        self.conn.commit()

    # set (or insert) repository meta in project_meta table
    def add_project_meta(self, gid, fork, created_at, updated_at, pushed_at, codeql_since, size, stargazers_count,
                         watchers_count, languages, javascript_size, has_issues, has_projects, has_downloads, has_wiki,
                         forks_count, open_issues_count, license, is_template, default_branch, number_pulls
                         ):
        sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".project_meta (gid, fork, created_at, updated_at, " \
                                                             "pushed_at, codeql_since, size, stargazers_count, " \
                                                             "watchers_count, " \
                                                             "languages, javascript_size, has_issues, has_projects, " \
                                                             "has_downloads, has_wiki, forks_count, " \
                                                             "open_issues_count, license, is_template, default_branch, number_pulls) " \
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
             "%s, %s, %s, %s, %s, %s, %s, %s, %s)" \
             "ON CONFLICT (gid)" \
             "DO UPDATE SET gid = %s, fork = %s, created_at = %s, " \
             "updated_at = %s, pushed_at = %s, codeql_since = %s, " \
             "size = %s, stargazers_count = %s, watchers_count = %s, " \
             "languages = %s, javascript_size = %s, has_issues = %s, " \
             "has_projects = %s, has_downloads = %s, has_wiki = %s, " \
             "forks_count = %s, open_issues_count = %s, license = %s, " \
             "is_template = %s, default_branch = %s, number_pulls = %s; "
        self.cursor.execute(sql, (gid, fork, created_at, updated_at, pushed_at, codeql_since, size, stargazers_count, watchers_count,
                                  languages, javascript_size, has_issues, has_projects, has_downloads, has_wiki,
                                  forks_count, open_issues_count, license, is_template, default_branch, number_pulls, gid, fork, created_at, updated_at, pushed_at, codeql_since, size, stargazers_count, watchers_count,
                                  languages, javascript_size, has_issues, has_projects, has_downloads, has_wiki,
                                  forks_count, open_issues_count, license, is_template, default_branch, number_pulls
                                  )
                            )
        self.conn.commit()

    # insert sample gid
    def add_sample_over_all_repos(self, gid, status):
        sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".sample_over_all_repos (gid, status) VALUES (%s, %s);"
        self.cursor.execute(sql, (gid, status))
        self.conn.commit()

    # set job status to 0 where status=-3 (happens on download error)
    def jobs_to_zero(self):
        try:
            sql = "update " + cfg.POSTGRES["environment"] + ".jobs set status = 0 where status = -3;"
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as error:
            print(error)

    # set (or insert) codeql_scanning_config
    def add_codeql_scanning_config(self, gid, scans_javascript, data):
        sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".codeql_scanning_config (gid, scans_javascript, data) " \
                                                             "VALUES (%s, %s, %s)" \
                                                             "ON CONFLICT (gid)" \
                                                             "DO UPDATE SET scans_javascript = %s, data = %s;"

        self.cursor.execute(sql, (gid, scans_javascript, data, scans_javascript, data))
        self.conn.commit()

    # add a new repo, that could use CodeQL
    def add_repo_to_checking(self, gid):
        sql = "INSERT INTO " + cfg.POSTGRES["environment"] + ".repos_checking (gid, status) " \
                                                             "VALUES (%s, %s)" \
                                                             "ON CONFLICT (gid)" \
                                                             "DO NOTHING;"
        try:
            self.cursor.execute(sql, (gid, 0))
            self.conn.commit()
        except Exception as error:
            print(error)

    # get potential CodeQL repo from repos_checking table and set status to 1
    def fetch_checking_repo(self):
        try:
            # Set status of 1 waiting job to process id
            sql = "UPDATE " + cfg.POSTGRES["environment"] + ".repos_checking " + \
                  "SET status = 1 " \
                  "WHERE gid = (SELECT gid " \
                  "FROM " + cfg.POSTGRES["environment"] + ".repos_checking " \
                                                          "WHERE status = 0 " \
                                                          "LIMIT 1 FOR UPDATE SKIP LOCKED) " + \
                  "RETURNING gid;"
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.fetchone()[0]
        except (Exception, psycopg2.DatabaseError) as error:
            # print(error)
            return None

    # add json data for all changes to CodeQL configuration
    def add_codeql_config_changes(self, gid, config_changes):
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".codeql_scanning_config " + \
              "SET config_changes = %s " \
              "WHERE gid = %s;"
        self.cursor.execute(sql, (config_changes, gid))
        self.conn.commit()

    # get all results for a repository
    def results_for_gid(self, gid):
        sql = """
                select
                    published as timestamp,
                    html_constructed_from_input,
                    reflected_xss,
                    stored_xss,
                    unsafe_jquery_plugin,
                    xss,
                    xss_through_dom,
                    xss_through_exception,   
                    overall
                from
                    Analysis_TABLE
                where
                        gid = """ + str(gid) + """
                    and published >= '2009-01-01'
                    and published <= '2022-04-30'
                order by
                    published
            """
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    # get result for repository (just specified column)
    def single_result_for_gid(self, gid, column='overall'):
        sql = """
                select
                    published as timestamp,
                    """ + column + """ as result
                from
                    Analysis_TABLE
                where
                        gid = """ + str(gid) + """
                    and published >= '2009-01-01'
                    and published <= '2022-04-30'
                order by
                    published
            """
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    # select result for repository (timediff in seconds, just specified column)
    def single_day_diff_result_for_gid(self, gid, column='overall'):
        sql = """
                select
                    concat(timediff, ' seconds') as timestamp,
                    """ + column + """ as result
                from
                    Analysis_TABLE a
                where
                        gid = """ + str(gid) + """
                    and timediff >= -43200000
                    and timediff <= 17280000
                order by
                    published
            """
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    #get results for one repository ID
    def single_day_diff_all_results_for_gid(self, gid):
        sql = """
                select
                    concat(timediff, ' seconds') as timestamp,
                    html_constructed_from_input,
                    reflected_xss,
                    stored_xss,
                    unsafe_jquery_plugin,
                    xss,
                    xss_through_dom,
                    xss_through_exception,   
                    overall
                from
                    Analysis_TABLE a
                where
                        gid = """ + str(gid) + """
                    and timediff >= -500000000-- -43200000
                    and timediff <= 54000000 --17280000
                order by
                    published
            """
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    # close connection and connect again
    def try_again(self):
        try:
            self.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("try_again", error)
        self.conn = psycopg2.connect(
            database=cfg.POSTGRES["database"],
            user=cfg.POSTGRES["user"],
            password=cfg.POSTGRES["password"],
            host=cfg.POSTGRES["host"],
            port=cfg.POSTGRES["port"],
            connect_timeout=60
        )
        self.cursor = self.conn.cursor()

    # get reposirory IDs
    # where is a SQL WHERE statement
    def get_gids_by_where(self, where):
        sql = """
                select
                    distinct p.gid
                from
                    """ + cfg.POSTGRES["environment"] + """.projects p
                    inner join """ + cfg.POSTGRES["environment"] + """.codeql_scanning_config c on c.gid = p.gid
                    inner join """ + cfg.POSTGRES["environment"] + """.project_meta pm on p.gid = pm.gid
                    inner join Analysis_TABLE a on p.gid = a.gid
                where
                        """ + where + """
            """
        self.cursor.execute(sql)
        self.conn.commit()
        return [r[0] for r in self.cursor.fetchall()]

    # get average number of problems and javascript site for each repository
    def get_avg_problems_vs_jssize(self, gids):
        sql = """
                  select
                      javascript_size as javascript_size,
                      avg(overall) as avg_problems
                  from 
                      analysis_table a
                      inner join """ + cfg.POSTGRES["environment"] + """.project_meta pm on a.gid = pm.gid
                  where a.gid in """ + str(gids).replace("[", "(").replace("]", ")") + """
                  group by
                      javascript_size,
                      a.gid;
            """
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    # get jobs for a repository
    def get_commits_for_gid(self, gid):
        sql = """
            select
                j.published
                --to_char (j.published, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')
            from
                """ + cfg.POSTGRES["environment"] + """.jobs j
                inner join """ + cfg.POSTGRES["environment"] + """.project_meta pm on j.gid = pm.gid
            where
                published :: date - codeql_since :: date >= -500
                and published :: date - codeql_since :: date <= 200
                and j.status in (1, -2, 0)
                and j.gid = """ + str(gid) + """
            order by
                published
            """
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    # set number_pulls in project_meta
    def set_number_pulls(self, gid: int, number_pulls: int):
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".project_meta SET number_pulls = %s WHERE gid = %s"
        self.cursor.execute(sql, (number_pulls, gid))
        self.conn.commit()

    # set number_contributors in project_meta
    def set_number_contributors(self, gid: int, number_contributors: int):
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".project_meta SET number_contributors = %s WHERE gid = %s"
        self.cursor.execute(sql, (number_contributors, gid))
        self.conn.commit()

    # set criticality score in project_meta
    def set_criticality_score(self, username, projectname, criticality_score):
        sql = "UPDATE " + cfg.POSTGRES["environment"] + ".project_meta " \
                                                        "SET criticality_score = %s " \
                                                        "WHERE gid in (" \
                                                            "SELECT gid " \
                                                            "FROM " + cfg.POSTGRES["environment"] + ".projects " \
                                                            "WHERE username = %s and projectname = %s" \
                                                        ")"
        self.cursor.execute(sql, (criticality_score, username, projectname))
        self.conn.commit()
