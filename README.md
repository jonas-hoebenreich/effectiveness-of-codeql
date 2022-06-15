# CodeQL Repo Analyzer

Analyze Github repos on a large scale with [CodeQL](https://codeql.github.com/)

CodeQL is a semantic code analysis engine to discover security vulnerabilities. The goal of this project is to scan commits/releases to open source projects over time.

## Project Architecture

This project consists of the following components:
- `Database.py`:
  - Connetcts to PostgreSQL DB
  - tables:
    - `jobs`: jid = Job ID, a commit (or theoretically a release) on GitHub
    - `projects` = GitHub repository
    - `project_meta`: metadata for GitHub repositories
    - `results`: findings identified by CodeQL
    - `codeql_scanning_config`: CodeQL configuration details for a project
    - `commit_meta`: metadata for commits (mainly author)
    - `repos_checking`: all repos that have been checked for CodeQL (necessary to prevent double checking of repos)
    - `rules`: CWE-079 rules by CodeQL
    - `sample_over_all_repos`: used to extrapolate the number of CodeQL repos on GitHub
    - `Analysis_VIEW` & `Analysis_TABLE`: speed up analysis by precalculating results
- `Worker.py`: 
  - Connect to Database and fetch a new job
  - Download snapshot from GitHub
  - Create CodeQL database
  - Run CWE-079 query suite on this database
  - Read output file and safe findings in database
  - repeat until no more jobs in queue
- `Project.py`:
  - project = GitHub repository
  - gid = GitHub ID of a repository
  - add new jobs to queue for a project: enqueue_relevant_commits()
  - find new potential repositories that use CodeQL: codeql_repos_by_code_date_search()

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on the LRZ Linux cluster.

## Deployment on LRZ Linux Cluster

Connect to the login node:

    ssh -Y lxlogin1.lrz.de -l aa11bbb

Start SLURM job to start worker:

    sbatch slurm.job

Note: please make sure to set up config.py properly

Note: when you stark multiple slurm scripts at the same time, anaconda will probably fail

### Status codes in DB

- job:
  - `0`: job ready to go
  - `1`: job finished
  - `-1`: A fatal error occurred while processing the job
  - `-2`: A CodeQL error occurred while processing the job, skipped it
  - `-5`: CodeQL analysis failed and a retry is not worthwhile because the repository does not meet all the requirements for the sample
- projects - status:
  - `0`: project created, no jobs loaded yet
  - `1`: project created, jobs in DB
  - `-4`: repo not available
  - `-5`: repo is fork
  - `-6`: repo manually excluded from analysis as unsuitable
- projects - uses_codeql:
  - deprecated (only for development needed)
- sample_over_all_repos - status
  - `403/404/451`: not public
  - `1`: public, does not use codeql
  - `2`: public, does use codeql, but no javascript
  - `3`: public, uses codeql, uses javascript, fork
  - `4`: public, uses codeql, uses javascript, no fork
- codeql_scanning_config
  - scans_javascript
    - `-1`: invalid configuration encountered
    - `0`: does not scan javascript code
    - `1`: scans javascript code
    - `2`: config file changed so that javascript was not scanned throughout
  - trigger_push
    - `-1`: invalid triggers
    - `0`: no scan on push (and was never turned on)
    - `1`: scans on push (and was never turned off)
    - `2`: scan on push changed
  - trigger_pull_request
    - `-1`: invalid triggers
    - `0`: no scan on pull (and was never turned on)
    - `1`: scans on pull (and was never turned off)
    - `2`: scan on pull changed
  - cron_frequency_changed
    - `0`: scan frequency did not change 
    - `1`: scan frequency changed
    - `2`: no scan frequency found
