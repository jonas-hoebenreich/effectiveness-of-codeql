import csv
import datetime
import json
import os
import random
import subprocess
import time

import requests
import yaml
from future.backports.datetime import date, timedelta

from config import GITHUB_TOKEN, INTERVAL_RELEASES, RANDOM_SAMPLE_MIN, RANDOM_SAMPLE_MAX, CUTOFF_DATE, \
    CODEQL_DEFAULT_PATH
from src.Database import Database
from libraries.ghapi.all import GhApi


def _sort_date(e):
    return e['date']


# check ratelimit
# how many requests we have left to the GitHub API?
def check_response_header(headers):
    remaining = int(headers['x-ratelimit-remaining'])
    if remaining < 4:
        refresh = int(headers['x-ratelimit-reset'])
        wait_for_refresh(refresh)


# wait until the GitHub API ratelimit refreshes
def wait_for_refresh(refresh):
    now = time.time()
    sleep = refresh - now
    print('sleep for ', str(sleep + 3) + 's')
    time.sleep(sleep + 3)


# Project class (manage Repositories)
class Project:
    database = None
    ghapi = None
    headers = {'Authorization': 'token ' + GITHUB_TOKEN[0],
               'Accept': 'application/vnd.github.v3.text-match+json'}  # 'application/vnd.github.cloak-preview'}
    current_token = 0
    ghapis = None

    def __init__(self, ):
        self.database = Database()
        self.ghapis = [GhApi(token=GITHUB_TOKEN[0]), GhApi(token=GITHUB_TOKEN[1]), GhApi(token=GITHUB_TOKEN[2]),
                       GhApi(token=GITHUB_TOKEN[3])]
        self.ghapi = self.ghapis[0]

    def add_project(self, username: str, projectname: str,
                    language='', status=4, enqueue='release', gid=None, uses_codeql=-1):
        # Push Project and relevant releases to database
        pid = self.database.add_project(username, projectname, language, status, gid, uses_codeql)
        if status == 1:
            if enqueue == 'commit':
                self.enqueue_relevant_commits(pid, username, projectname)
            elif enqueue == 'release':
                self.enqueue_relevant_releases(pid, username, projectname)

    def add_jobs_from_project_db(self, enqueue='release'):
        # Push Project and relevant releases to database
        project = self.database.fetch_and_update_project(status=0, newstatus=2)
        while project is not None:
            if enqueue == 'commit':
                self.enqueue_relevant_commits(project[1], project[2], project[3])
            elif enqueue == 'release':
                self.enqueue_relevant_releases(project[1], project[2], project[3])
            else:
                self.enqueue_js_commits(project[1], project[2], project[3])
            project = self.database.fetch_and_update_project()

    def add_language_to_projects(self):
        # Push Project and relevant releases to database
        # TODO only adds if javascript
        project = self.database.fetch_and_remove_project(-1)
        while project is not None:
            try:
                languages = self.ghapi.repos.list_languages(owner=project[1], repo=project[2])
                for language in languages:
                    if language.lower() in {"cpp", "csharp", "go", "java", "javascript", "python", "ruby"}:
                        self.add_project(username=project[1], projectname=project[2], language=language.lower(),
                                         status=0, enqueue='')
            except BaseException as error:
                print(error)
                self.add_project(username=project[1], projectname=project[2], status=-2, enqueue=None)
            project = self.database.fetch_and_remove_project()

    def add_rules(self, file):
        # TODO
        # Safe rules from .sarif file in database
        f = open(file, "r")
        c = f.read()
        j = json.loads(c)
        rules = j["runs"][0]['tool']['driver']["rules"]
        for rule in rules:
            for i in {"description", "description", "precision", "problem.severity", "security-severity", 'tags'}:
                if i not in rule["properties"]:
                    rule["properties"][i] = "0"

            rule_id = rule['id']
            shortdescription = rule['shortDescription']['text']
            description = rule['properties']['description']
            kind = rule['properties']['kind']
            precision = rule['properties']['precision']
            problem_severity = rule['properties']['problem.severity']
            security_severity = rule['properties']['security-severity']
            tags = json.dumps(rule['properties']['tags'])

            self.database.add_rule(rule_id, shortdescription, description, kind, precision, problem_severity,
                                   security_severity, tags)

    def enqueue_all_releases(self, gid, username, projectname):  # TODO
        # Push all releases of a repository to database jobs
        releases = self.ghapi.repos.list_releases(username, projectname, 100, 1)
        for release in releases:
            print('Add release:', release['created_at'], username, projectname, release['tag_name'])  # TODO
            self.database.enqueue_job(
                gid=gid,
                url=release['zipball_url'],
                published=release['created_at'],
            )

    def enqueue_relevant_releases(self, gid, username, projectname):
        # Push only relevant (skip releases that are to close together) releases to database
        current = datetime.date(2100, 1, 1)  # Date in the distant future
        keep_going = 1
        i = 1
        while keep_going:
            releases = self.ghapi.repos.list_releases(username, projectname, 100, i)
            keep_going = 0
            i += 1
            for release in releases:
                keep_going = 1
                release_date = datetime.datetime.strptime(release['created_at'], "%Y-%m-%dT%H:%M:%SZ").date()
                if abs(current - release_date).days >= INTERVAL_RELEASES:
                    print('Add relevant release:', release['created_at'], username, projectname,
                          release['tag_name'])  # TODO
                    self.database.enqueue_job(
                        gid=gid,
                        url=release['zipball_url'],
                        published=release['created_at'],
                    )
                    current = release_date
                else:
                    print('Skip irrelevant release:', release['created_at'], username, projectname,
                          release['tag_name'])  # TODO

    def enqueue_relevant_commits(self, gid, username, projectname, since=datetime.date(1900, 1, 1),
                                 until=datetime.date(2100, 1, 1)):
        print('Enqueuing commits for:', gid, username + '/' + projectname, since, until)
        # Push all relevant releases of a repository to database jobs
        current = datetime.date(2100, 1, 1)  # Date in the distant future
        keep_going = 1
        i = 1
        all_commits = []
        while keep_going:
            keep_going = 0
            try:
                commits = self.execute_request('http://api.github.com/repos/' + username + '/' +
                                               projectname + '/commits?per_page=100&page=' + str(i)
                                               + '&since=' + since.isoformat() + 'Z'
                                               + '&until=' + until.isoformat() + 'Z'
                                               )
                # commits = self.ghapi.repos.list_commits(owner=username, repo=projectname, per_page=100, page=i)
                if commits is not None:
                    i += 1
                    for commit in commits:
                        keep_going = 1
                        url = 'http://github.com/' + username + '/' + projectname + '/archive/' + commit['sha'] + '.zip'
                        all_commits.append({'url': url, 'date': commit['commit']['author']['date']})
            except Exception as error:
                print('ERROR:', username, projectname)
                print(error)
                self.database.update_project_status(gid, -3)
                return
        all_commits.sort(key=_sort_date)
        for commit in all_commits:
            release_date = datetime.datetime \
                .strptime(commit['date'], "%Y-%m-%dT%H:%M:%SZ") \
                .date()
            if abs(current - release_date).days >= INTERVAL_RELEASES:
                self.database.enqueue_job(
                    gid=gid,
                    url=commit['url'],
                    published=commit['date'],
                )
                current = release_date

    def condense_queued_commits(self, gid, username: str, projectname: str):
        print('Enqueuing commits for:', gid, username + '/' + projectname)
        dates = self.database.get_commits_for_gid(gid)
        for d in range(0, len(dates) - 1):
            since = dates[d][0] + timedelta(days=INTERVAL_RELEASES)
            until = dates[d + 1][0] - timedelta(days=INTERVAL_RELEASES)
            if since < until:
                self.enqueue_relevant_commits(gid, username, projectname, since, until)

    def enqueue_commits_before_after_codeql(self, gid, username: str, projectname: str, codeql_since, days=14):
        print('Enqueuing commits for:', gid, username + '/' + projectname)
        keep_going = 1
        i = 1
        all_commits = []
        before = datetime.datetime.strptime(codeql_since, "%Y-%m-%dT%H:%M:%SZ") - timedelta(days=days)
        after = datetime.datetime.strptime(codeql_since, "%Y-%m-%dT%H:%M:%SZ") + timedelta(days=days)
        while keep_going:
            keep_going = 0
            url = 'http://api.github.com/repositories/' + str(gid) + '/commits?per_page=100&page=' + str(
                i) + '&since=' + before.isoformat() + 'Z&until=' + after.isoformat() + 'Z'
            commits = self.execute_request(url)
            if commits is not None:
                i += 1
                for commit in commits:
                    keep_going = 1
                    url = 'http://github.com/' + username + '/' + projectname + '/archive/' + commit['sha'] + '.zip'
                    all_commits.append({'url': url, 'date': commit['commit']['author']['date']})
        all_commits.sort(key=_sort_date)
        if len(all_commits) > 1:
            self.database.enqueue_job(
                gid=gid,
                url=all_commits[0]['url'],
                published=all_commits[0]['date'],
            )
            self.database.enqueue_job(
                gid=gid,
                url=all_commits[len(all_commits) - 1]['url'],
                published=all_commits[len(all_commits) - 1]['date'],
            )

    def enqueue_js_commits(self, gid, username, projectname):
        self.switch_token()
        print('Enqueuing js commits for:', str(gid), username, projectname)
        keep_going = True
        i = 1
        while keep_going:
            keep_going = False
            # try:
            commits = self.ghapi.repos.list_commits(owner=username, repo=projectname, per_page=100, page=i)
            i = i + 1
            for commit in commits:
                keep_going = True
                if self.commits_contains_js_file(username, projectname, commit['sha']):
                    self.database.enqueue_job(
                        gid=gid,
                        url='http://github.com/' + username + '/' + projectname + '/archive/' + commit['sha'] + '.zip',
                        published=commit['commit']['author']['date'],
                    )

    def commits_contains_js_file(self, username, projectname, ref):
        url = 'http://api.github.com/repos/' + username + '/' + projectname + '/commits/' + ref
        try:
            r = requests.get(url, headers=self.headers)
            check_response_header(r.headers)
            if r.ok:
                commit_details = r.json()
                if len(commit_details['files']) == 300:
                    return True
                for file in commit_details['files']:
                    if file['filename'].endswith('.js') or file['filename'].endswith('.ts'):
                        return True
                return False
            else:
                print('ERROR', ref, username, projectname, r.status_code)
                return -2
        except (Exception, requests.RequestException) as error:
            print('Exception', ref, username, projectname, error)
            time.sleep(10)
            return self.commits_contains_js_file(username, projectname, ref)

    def checking_uses_codeql(self):
        for c in range(1000):
            project = self.database.fetch_project_by_uses_codeql()
            uses_codeql = self.has_github_workflows(project[0], project[1], project[2])
            self.database.update_project_uses_codeql(project[0], uses_codeql)

    def uses_codeql(self, username, projectname):
        commits = self.ghapi.repos.list_commits(owner=username, repo=projectname, path=CODEQL_DEFAULT_PATH)

        if len(commits) > 0:
            return 1
        else:
            return 0

    def has_github_workflows(self, gid, username, projectname):
        try:
            url = 'http://github.com/' + username + '/' + projectname + '/blob/main/.github/workflows/'
            r = requests.get(url, headers=self.headers)
            if r.ok:
                print('OK', gid, username, projectname)
                return 2
            else:
                print('ERROR', gid, username, projectname, r.status_code)
                return -2
        except (Exception, requests.RequestException) as error:
            print('Exception', gid, username, projectname)
            return -3

    def generate_random_repo_sample(self, seed=0, language='javascript'):
        random.seed(seed)
        while random.randint(RANDOM_SAMPLE_MIN, RANDOM_SAMPLE_MAX) != 374613344:
            continue
        while True:
            self.check_repo_by_id(random.randint(RANDOM_SAMPLE_MIN, RANDOM_SAMPLE_MAX), language)
            self.switch_token()

    def check_repo_by_id(self, rid, language):
        repo = self.get_repo_by_id(rid)
        if repo:
            decoded_result = repo.json()
            if decoded_result["pushed_at"] is not None and not self.check_pushed_at(decoded_result["pushed_at"]):
                return 0
            username = decoded_result['owner']['login']
            projectname = decoded_result['name']
            # TODO hardcoded JavaScript
            if decoded_result['language'] != 'JavaScript' and not self.check_repo_language(username, projectname):
                return 0
            uses_codeql = self.uses_codeql(username, projectname)
            gid = decoded_result['id']
            self.add_project(username, projectname, language, 0, gid=gid, uses_codeql=uses_codeql)
            print(gid, username, projectname, language, uses_codeql)
            return 1
        return 0

    def get_repo_by_id(self, rid):
        return self.execute_request('http://api.github.com/repositories/' + str(rid))

    def check_pushed_at(self, pushed_at):
        pushed_at_date = datetime.datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ").date()
        if (CUTOFF_DATE - pushed_at_date).days > 0:
            return False
        return True

    def check_repo_language(self, owner, repo, language='javascript'):
        used_languages = self.ghapi.repos.list_languages(owner=owner, repo=repo)
        for used_language in used_languages:
            if used_language.lower() == language:
                return True
        return False

    def switch_token(self):
        self.current_token = (self.current_token + 1) % len(GITHUB_TOKEN)
        self.headers = {'Authorization': 'token ' + GITHUB_TOKEN[self.current_token]}
        self.ghapi = self.ghapis[self.current_token]

    def search_codeql_repos(self):
        start = 376228375
        end = 462000000
        t = time.time()
        for rid in range(start, end):
            self.find_codeql_repo(rid)
            self.switch_token()
            if rid % 100 == 0:
                print(str(rid), 'time:', str(time.time() - t))
                t = time.time()

    def search_codeql_repos_2(self, start=376252700):
        t = time.time()
        rid = start
        while True:
            self.switch_token()
            url = 'http://api.github.com/repositories?since=' + str(rid)
            r = requests.get(url, headers=self.headers, timeout=5)
            repos = r.json()
            # repos = self.ghapi.repos.list_public(since=rid)
            if len(repos) > 0:
                for repo in repos:
                    if repo is None:
                        print("Repo is None. Skipping repo...")
                        continue
                    rid = repo['id']
                    if not repo['fork']:
                        self.find_codeql_repo(rid)
                        if rid % 100 == 0:
                            print(str(rid), 'time:', str(time.time() - t), 'now:', str(time.time()))
                            t = time.time()
            else:
                rid = rid + 100

    def find_codeql_repo(self, rid, language='javascript'):
        if self.database.check_project_exists(rid):
            uses_codeql = self.uses_codeql_by_id(rid)
            if uses_codeql:
                decoded_result = self.get_repo_by_id(rid)
                if decoded_result:
                    # decoded_result = repo.json()
                    if decoded_result["pushed_at"] is not None and not self.check_pushed_at(
                            decoded_result["pushed_at"]):
                        return 0
                    username = decoded_result['owner']['login']
                    projectname = decoded_result['name']
                    # TODO hardcoded JavaScript
                    if decoded_result['language'] != 'JavaScript' and not self.check_repo_language(username,
                                                                                                   projectname):
                        return 0
                    gid = decoded_result['id']
                    self.add_project(username, projectname, language, 4, gid=gid, uses_codeql=uses_codeql)
                    print(gid, username, projectname, language, uses_codeql)
                    return 1
                return 0

    def add_project_to_table_by_id(self, gid, language):
        decoded_result = self.get_repo_by_id(gid)
        if decoded_result:
            username = decoded_result['owner']['login']
            projectname = decoded_result['name']
            gid = decoded_result['id']
            self.add_project(username, projectname, language, 4, gid=gid, uses_codeql=1)
            self.add_project_meta(gid)

    def uses_codeql_by_id(self, rid):
        commits = self.execute_request(
            'http://api.github.com/repositories/' + str(rid) + '/commits?path=.github/workflows/codeql-analysis.yml')
        if commits is not None:
            if len(commits) > 0:
                return 1
            else:
                return 0

    def codeql_since(self, gid):
        commits = self.execute_request(
            'http://api.github.com/repositories/' + str(gid) + '/commits?path=.github/workflows/codeql-analysis.yml')
        if commits is not None and len(commits) > 0:
            first_commit = commits[-1]
            return first_commit['commit']['committer']['date']
        else:
            return '1900-01-01T00:00:00Z'

    def random_codeql_sample(self):
        t = time.time()
        random.seed()
        checked = 0
        found = 0
        while True:
            start = random.randint(RANDOM_SAMPLE_MIN, RANDOM_SAMPLE_MAX)
            self.switch_token()
            # print(str(start), 'time:', str(time.time() - t), 'now:', str(time.time()))
            t = time.time()
            url = 'http://api.github.com/repositories?since=' + str(start)
            try:
                r = requests.get(url, headers=self.headers, timeout=10)
                check_response_header(r.headers)
            except (Exception, requests.RequestException) as error:
                print('EXCEPTION random_codeql_sample', error)
                time.sleep(10)
                continue
            repos = r.json()
            # repos = self.ghapi.repos.list_public(since=rid)
            if len(repos) > 0:
                for repo in repos:
                    checked = checked + 1
                    if repo is None:
                        print("Repo is None. Skipping repo...")
                        continue
                    gid = repo['id']
                    if not repo['fork']:
                        if self.find_codeql_repo(gid) == 1:
                            found = found + 1
                            print('Ratio randomly checked to found', str(found / checked), 'Checked:', str(checked),
                                  'found:', str(found))

    def codeql_repos_by_commit_search(self):
        for order in ['desc', 'asc']:
            for page in range(1, 11):
                for search in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'z', 'o',
                               'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'y', 'x', 'c', 'v', 'b', 'n', 'u',
                               'm', 'typescript', 'node', 'js', 'add', 'linux', 'cli', 'python', 'ruby', 'config',
                               'typescript', 'portfolio', 'i', 'open', 'doc', 'documentation', 'perform', 'request',
                               'linux', 'web', 'home', 'language', 'windows', 'download', 'main', 'master', 'pull',
                               'analyze', 'java', 'scanning', 'javascript', 'push', 'ubuntu', 'go', 'api', 'yml',
                               'portfolio', 'cpp', 'csharp', 'github', 'codeql', 'ts', 'analysis.yml', 'action',
                               'branch', 'branches', 'name', 'jobs', 'true', 'compile', 'checkout', 'init', 'name',
                               'autobuild', 'matrix', 'read', 'runs', 'steps', 'cron', 'permissions', 'analysis',
                               'v1', 'v2', '@', 'repository', 'owner', 'null', 'with', 'schedule', 'sudo', 'event',
                               'contents', 'events', 'security', 'sec', 'head', 'pull_request', 'strategy'}:
                    for sort in ['author-date', 'committer-date']:
                        if total_count > (page - 1) * 100:
                            url = 'http://api.github.com/search/commits?per_page=100&q=' + search + '+codeql&page=' + str(
                                page) + '&sort=' + sort + '&order=' + order
                            print('analyze page', str(page), search, sort, order)
                            self.switch_token()
                            try:
                                time.sleep(60)
                                r = requests.get(url, headers=self.headers, timeout=60)
                                check_response_header(r.headers)
                            except (Exception, requests.RequestException) as error:
                                print(error)
                                print('skip page', str(page))
                                time.sleep(10)
                                continue
                            if r.ok:
                                repos = r.json()
                                for repo in repos['items']:
                                    if repo is None:
                                        print("Repo is None. Skipping ...")
                                        continue
                                    details = repo['repository']
                                    rid = details['id']
                                    self.find_codeql_repo(rid)
                                total_count = repos['total_count']
                            else:
                                print('search not OK', r.status_code)
                                if r.status_code == 403:
                                    time.sleep(30)
                                else:
                                    exit(1)

    # http://api.github.com/search/commits?per_page=100&q=github+action+committer-date:2021-04-15..2021-04-15&page=5&sort=committer-date&order=desc
    def codeql_add_repos_to_checking_queue(self, repos):
        for repo in repos['items']:
            rid = repo['repository']['id']
            self.database.add_repo_to_checking(rid)

    def codeql_repos_check_date(self, date, page, sort='author-date', order='asc'):
        url = 'http://api.github.com/search/commits?per_page=100&q=codeql+committer-date:' + \
              str(date) + '..' + str(date) + '&page=' + str(page) + '&sort=' + sort + '&order=' + order

        return self.codeql_repos_check_url(url)

    def codeql_repos_by_commit_date_search(self):
        current_date = date(2020, 4, 1)
        end_date = date(2022, 5, 30)

        while current_date <= end_date:
            total_count = 1000
            page = 1
            while page * 100 <= total_count + 100 and page <= 10:
                # self.codeql_repos_check_date(current_date, page, sort='committer-date', order='asc')
                # self.codeql_repos_check_date(current_date, page, sort='committer-date', order='desc')
                total_count = self.codeql_repos_check_date(current_date, page, order='asc')  # sort='committer-date', )
                if total_count >= 1000 + (page - 1) * 100:
                    self.codeql_repos_check_date(current_date, page, order='desc')  # sort='committer-date', )
                page = page + 1
                if total_count > 1000 and page == 1:
                    print(str(total_count), '\n', str(current_date))
            current_date += timedelta(days=1)

    def codeql_repos_check_url(self, url):
        print(url)
        self.switch_token()
        try:
            r = requests.get(url, headers=self.headers, timeout=60)
            check_response_header(r.headers)
            if r.ok:
                self.codeql_add_repos_to_checking_queue(r.json())
                return r.json()['total_count']
            else:
                print('search not OK', r.status_code)
                if r.status_code == 403:
                    time.sleep(60)
                    return self.codeql_repos_check_url(url)
                else:
                    exit(1)
        except (Exception, requests.RequestException) as error:
            print(error)
            time.sleep(60)
            return self.codeql_repos_check_url(url)

    def codeql_repos_by_code_search(self):
        for sort in ['indexed', 'best-match']:
            for search in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'z', 'o',
                           'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'y', 'x', 'c', 'v', 'b', 'n', 'u',
                           'm', 'typescript', 'node', 'js', 'add', 'linux', 'cli', 'python', 'ruby', 'config',
                           'typescript', 'portfolio', 'i', 'open', 'doc', 'documentation', 'perform', 'request',
                           'linux', 'web', 'home', 'language', 'windows', 'download', 'main', 'master', 'pull',
                           'analyze', 'java', 'scanning', 'javascript', 'push', 'ubuntu', 'go', 'api', 'yml',
                           'portfolio', 'cpp', 'csharp', 'github', 'codeql', 'ts', 'analysis.yml', 'action',
                           'branch', 'branches', 'name', 'jobs', 'true', 'compile', 'checkout', 'init', 'name',
                           'autobuild', 'matrix', 'read', 'runs', 'steps', 'cron', 'permissions', 'analysis',
                           'v1', 'v2', '@', 'repository', 'owner', 'null', 'with', 'schedule', 'sudo', 'event',
                           'contents', 'events', 'security', 'sec', 'head', 'pull_request', 'strategy'}:
                total_count = 1000
                page = 1
                while page * 100 <= total_count + 100 and page <= 10:
                    url = 'http://api.github.com/search/code?&q=codeql+' + search + '&per_page=100&page=' + str(
                        page) + '&sort=' + sort + '&order=asc'
                    total_count = self.codeql_repos_check_url(url)
                    if page == 1:
                        print(total_count)
                    if total_count >= 1000 + (page - 1) * 100:
                        time.sleep(60)
                        self.codeql_repos_check_url(
                            'http://api.github.com/search/code?&q=codeql+' + search + '&per_page=100&page=' + str(
                                page) + '&sort=' + sort + '&order=desc')
                    page += 1
                    time.sleep(60)

    def codeql_repos_by_code_date_search(self):
        for page in range(1, 10):
            for order in ['desc', 'asc']:
                for sort in ['committer-date', 'author-date']:
                    for query in ['codeql', 'analyze', 'workflow', 'config', 'codeql-config', 'security', 'scanning', 'analysis']:
                        current_date = date(2022, 5, 1)
                        end_date = date(2020, 5, 1)
                        delta = timedelta(days=1)

                        # iterate over range of dates
                        while current_date >= end_date:
                            current_date -= delta
                            url = 'http://api.github.com/search/code?per_page=100&q=' + query + '+committer-date:' + str(
                                current_date) + '..' + str(current_date + timedelta(days=1)) + '&page=' + str(
                                page) + '&sort=' + sort + '&order=' + order
                            print('analyze page', url)
                            self.switch_token()
                            try:
                                r = requests.get(url, headers=self.headers, timeout=60)
                                check_response_header(r.headers)
                            except (Exception, requests.RequestException) as error:
                                print(error)
                                print('skip page', str(page))
                                time.sleep(10)
                                continue
                            if r.ok:
                                repos = r.json()
                                for repo in repos['items']:
                                    if repo is None:
                                        print("Repo is None. Skipping ...")
                                        continue
                                    details = repo['repository']
                                    rid = details['id']
                                    self.find_codeql_repo(rid)
                            else:
                                print('search not OK', r.status_code)
                                if r.status_code == 403:
                                    time.sleep(30)
                                else:
                                    exit(1)

    def add_project_meta(self, gid):
        repo = self.get_repo_by_id(gid)
        if repo:
            languages = self.execute_request(repo['languages_url'])
            javascript_size = 0
            if 'JavaScript' in languages:
                javascript_size = languages['JavaScript']
            number_pulls = self.get_number_of_pulls(gid)
            number_contributors = self.get_number_of_contributors(gid)
            self.database.add_project_meta(
                gid,
                repo['fork'],
                repo['created_at'],
                repo['updated_at'],
                repo['pushed_at'],
                self.codeql_since(gid),
                repo['size'],
                repo['stargazers_count'],
                repo['watchers_count'],
                json.dumps(languages),
                javascript_size,
                repo['has_issues'],
                repo['has_projects'],
                repo['has_downloads'],
                repo['has_wiki'],
                repo['forks_count'],
                repo['open_issues_count'],
                json.dumps(repo['license']),
                repo['is_template'],
                repo['default_branch'],
                number_pulls,
                number_contributors
            )
        else:
            self.database.update_project_status_gid(gid, -4)
            print(str(gid))

    def get_languages_by_id(self, gid):
        return self.execute_request('http://api.github.com/repos/' + str(gid) + '/languages')

    def execute_request(self, url):
        self.switch_token()
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            check_response_header(r.headers)
            if r.ok:
                return r.json()
            else:
                return None
        except (Exception, requests.RequestException) as error:
            print('ERROR execute_request', error)
            time.sleep(10)
            self.execute_request(url)

    def find_codeql_repo_for_sample_over_all_repos(self, rid):
        status = self.get_repo_status(rid)
        if status == 200:
            status = 1
            uses_codeql = self.uses_codeql_by_id(rid)
            if uses_codeql:
                status = 2
                repo = self.get_repo_by_id(rid)
                if repo:
                    decoded_result = repo.json()
                    username = decoded_result['owner']['login']
                    projectname = decoded_result['name']
                    if not (decoded_result['language'] != 'JavaScript' and not self.check_repo_language(username,
                                                                                                        projectname)):
                        status = 3
                        if not decoded_result['fork']:
                            status = 4
        self.database.add_sample_over_all_repos(rid, status)

    def get_repo_status(self, gid):
        self.switch_token()
        try:
            r = requests.get('http://api.github.com/repositories/' + str(gid), headers=self.headers, timeout=5)
            check_response_header(r.headers)
            return r.status_code
        except (Exception, requests.RequestException) as error:
            print('ERROR execute_request', error)
            time.sleep(10)
            self.execute_request('http://api.github.com/repos/' + str(gid))

    def create_codeql_repo_for_sample_over_all_repos(self):
        random.seed()
        while True:
            rid = random.randint(RANDOM_SAMPLE_MIN, RANDOM_SAMPLE_MAX)
            self.find_codeql_repo_for_sample_over_all_repos(rid)

    def add_codeql_config_changes(self, gid, user, repo):
        print(gid, user, repo)
        commits = self.execute_request(
            'http://api.github.com/repositories/' + str(gid) + '/commits?path=.github/workflows/codeql-analysis.yml')
        config_changes = {}
        if commits is not None:
            for commit in commits:
                date = commit['commit']['committer']['date']
                sha = commit['sha']
                r = requests.get(
                    'http://raw.githubusercontent.com/' + user + '/' + repo + '/' + sha + '/.github/workflows/codeql-analysis.yml',
                    timeout=20)
                config_changes[date] = {}
                config_changes[date]['sha'] = sha
                config_changes[date]['author'] = commit['commit']['author']
                try:
                    config_changes[date]['config'] = yaml.safe_load(r.content)
                except Exception as error:
                    config_changes[date]['config'] = 'invalid yml'
        self.database.add_codeql_config_changes(gid, json.dumps(config_changes))

    def add_codeql_languages(self, gid, user, repo, branch='master'):
        try:
            r = requests.get(
                'http://raw.githubusercontent.com/' + user + '/' + repo + '/' + branch + '/.github/workflows/codeql'
                                                                                         '-analysis.yml', timeout=10)
        except (Exception, requests.RequestException) as error:
            print('ERROR execute_request', gid, user, repo, '\n', error)
            return
        try:
            if r.ok:
                data = yaml.safe_load(r.content)
                if 'javascript' in data['jobs']['analyze']['strategy']['matrix']['language']:
                    scans_javascript = 1
                else:
                    scans_javascript = 0
            else:
                scans_javascript = r.status_code * -1
                if branch != 'main':
                    return self.add_codeql_languages(gid, user, repo, branch='main')
                data = None
        except Exception:
            scans_javascript = -1
            data = None
        self.database.add_codeql_scanning_config(gid, scans_javascript, json.dumps(data))
        return 0

    def repos_checking_queue(self):
        while True:
            gid = self.database.fetch_checking_repo()
            if gid is not None:
                self.find_codeql_repo(gid)
            else:
                time.sleep(300)

    def add_repos_of_org(self, org):
        print(org)
        c = True
        page = 1
        while c:
            c = False
            url = 'https://api.github.com/orgs/' + org + '/repos?per_page=100&page=' + str(page)
            repos = self.execute_request(url)
            page = page + 1
            if repos is not None:
                for repo in repos:
                    c = True
                    rid = repo['id']
                    self.database.add_repo_to_checking(rid)

    def add_most_starred_repos(self):
        for page in range(11):
            url = 'https://api.github.com/search/repositories?q=created:">2008-01-01"language:javascriptsort=stars&order=desc&per_page=100&page=' + str(
                page)
            repos = self.execute_request(url)
            if repos is not None:
                for repo in repos['items']:
                    rid = repo['id']
                    self.database.add_repo_to_checking(rid)

    def save_all_commit_details(self, gid, username, projectname):
        print('Commit details for:', gid)
        # Push all releases of a repository to database jobs
        keep_going = 1
        i = 1
        all_commits = []
        while keep_going:
            keep_going = 0
            # try:
            commits = self.execute_request(
                'http://api.github.com/repositories/' + str(gid) + '/commits?per_page=100&page=' + str(i))
            if commits is not None:
                i += 1
                for commit in commits:
                    if commit is None:
                        print('ERROR')
                    keep_going = 1
                    url = 'http://github.com/' + username + '/' + projectname + '/archive/' + commit['sha'] + '.zip'
                    author = {
                        'name': commit['commit']['author']['name'],
                        'email': commit['commit']['author']['email']
                    }
                    if 'author' in commit and commit['author'] is not None:
                        if 'id' in commit['author']:
                            author['id'] = commit['author']['id']
                        if 'login' in commit['author']:
                            author['login'] = commit['author']['login']

                    all_commits.append((
                        gid,
                        commit['sha'],
                        url,
                        commit['commit']['author']['date'],
                        json.dumps(author)
                    ))
            # except Exception as error:
            #     print('ERROR:', username, projectname)
            #     print(error)
            #     return
        if len(all_commits) > 0:
            self.database.add_commits(all_commits)

    def gid_for_fullname(self, fullname):
        url = "https://api.github.com/repos/" + fullname
        result = self.execute_request(url)
        return result['id']

    def add_commit_details(self, jid: int, username: str, projectname: str, sha: str):
        result = self.execute_request("http://api.github.com/repos/" + username + '/' + projectname + '/commits/' + sha)
        if result is not None:
            author = result['commit']['author']['name']
            author_name = ''
            email = result['commit']['author']['email']
            author_details = self.get_author_details(author)
            if author_details is not None:
                author_name = author_details['name']
                if email.endswith("noreply.github.com"):
                    email = author_details['email']
            self.database.add_commit_details(jid, author, author_name, email)

    def get_author_details(self, username: str):
        return self.execute_request("https://api.github.com/users/" + username)

    def get_number_of_pulls(self, gid: int):
        url = 'http://api.github.com/repositories/' + str(gid) + '/pulls?per_page=100&page='
        number_pulls = 0
        n = 100
        page = 1
        while n == 100:
            x = self.execute_request(url + str(page))
            if x is not None:
                n = len(x)
                number_pulls += n
                page += 1
            else:
                n = 0
        return number_pulls

    def get_number_of_contributors(self, gid: int):
        url = 'http://api.github.com/repositories/' + str(gid) + '/contributors?per_page=100&page='
        number_contributors = 0
        n = 100
        page = 1
        while n == 100:
            x = self.execute_request(url + str(page))
            if x is not None:
                n = len(x)
                number_contributors += n
                page += 1
            else:
                n = 0
        return number_contributors

    def read_criticality_score_file(self):
        with open('/home/jonas/Dokumente/UNI/7-Semester/Bachelorarbeit/BA-thesis/criticality_score_all.csv',
                  mode='r') as file:
            # reading the CSV file
            file = csv.reader(file)
            header = next(file)

            # displaying the contents of the CSV file
            for lines in file:
                username = lines[0]
                r = lines[1].find('/' + username)
                projectname = lines[1][19:lines[1][20:-1].find('/' + username) - len(username)]
                criticality_score = lines[15]
                print(username, projectname, criticality_score)
                self.database.set_criticality_score(username, projectname, criticality_score)
