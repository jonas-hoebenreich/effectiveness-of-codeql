create schema xxxxxx

-- xxxxxx.projects
DROP TABLE IF EXISTS xxxxxx.projects CASCADE;
CREATE TABLE xxxxxx.projects (
  id serial,
  gid BIGINT UNIQUE,
  username character varying(255) NOT NULL,
  projectname character varying(255) NOT NULL,
  language character varying(512),
  status integer DEFAULT 0,
  uses_codeql integer NULL,
);
ALTER TABLE
  xxxxxx.projects
ADD
  CONSTRAINT projects_pkey PRIMARY KEY (id);

--xxxxxx.project_meta
DROP TABLE IF EXISTS xxxxxx.project_meta CASCADE;
CREATE TABLE xxxxxx.project_meta (
  gid BIGINT UNIQUE,
  fork BOOLEAN NULL,
  created_at timestamp without time zone NOT NULL,
  updated_at timestamp without time zone NOT NULL,
  pushed_at timestamp without time zone NOT NULL,
  codeql_since timestamp without time zone NOT NULL,
  size integer NULL,
  stargazers_count integer NULL,
  watchers_count integer NULL,
  languages JSON NULL,
  javascript_size integer NULL,
  has_issues BOOLEAN NULL,
  has_projects BOOLEAN NULL,
  has_downloads BOOLEAN NULL,
  has_wiki BOOLEAN NULL,
  forks_count integer NULL,
  open_issues_count integer NULL,
  license JSON NULL,
  is_template BOOLEAN NULL,
  is_random_sample BOOLEAN NULL,
  default_branch character varying(1024) NULL,
  number_pulls integer NULL,
  number_contributors integer NULL
);
ALTER TABLE xxxxxx.project_meta
    ADD CONSTRAINT project_meta_pk PRIMARY KEY (gid);
ALTER TABLE xxxxxx.project_meta
   ADD FOREIGN KEY (gid) REFERENCES xxxxxx.projects(gid);

--xxxxxx.jobs
DROP TABLE IF EXISTS xxxxxx.jobs CASCADE;
CREATE TABLE xxxxxx.jobs (
  id SERIAL,
  gid integer NULL,
  url character varying(512) NULL,
  published timestamp without time zone NOT NULL,
  status integer DEFAULT 0
);
ALTER TABLE
  xxxxxx.jobs
ADD
  CONSTRAINT job_pkey PRIMARY KEY (id);

-- xxxxxx.results
DROP TABLE IF EXISTS xxxxxx.results CASCADE;
CREATE TABLE xxxxxx.results (
  id SERIAL,
  ruleid character varying(2048) NULL,
  jid integer NOT NULL,
  locations json NULL,
  ruleindex integer NULL,
  message character varying(32768) NULL,
  data json NULL
);
ALTER TABLE
  xxxxxx.results
ADD
  CONSTRAINT results_pkey PRIMARY KEY (id);

-- xxxxxx.rules
DROP TABLE IF EXISTS xxxxxx.rules CASCADE;
CREATE TABLE xxxxxx.rules (
  rule_id character varying(512) NOT NULL,
  shortdescription character varying(512) NULL,
  description character varying(512) NULL,
  kind character varying(255) NULL,
  "precision" character varying(255) NULL,
  problem_severity character varying(255) NULL,
  security_severity double precision NULL,
  tags json NULL
);
ALTER TABLE
  xxxxxx.rules
ADD
  CONSTRAINT rules_pkey PRIMARY KEY (rule_id);

-- xxxxxx.sample_over_all_repos
DROP TABLE IF EXISTS xxxxxx.sample_over_all_repos CASCADE;
CREATE TABLE xxxxxx.sample_over_all_repos (
  gid BIGINT UNIQUE,
  status integer NULL
);

-- xxxxxx.codeql_scanning_config
DROP TABLE IF EXISTS xxxxxx.codeql_scanning_config CASCADE;
CREATE TABLE xxxxxx.codeql_scanning_config (
    gid BIGINT UNIQUE,
    scans_javascript integer DEFAULT 0,
    data JSON NULL,
    config_changes json NULL,
    deleted_at timestamp without time zone NULL,
    cron_schedule character varying(255) NULL,
    trigger_push integer NULL,
    trigger_pull_request integer NULL,
    cron_frequency_changed integer NULL,
    trigger_workflow_dispatch integer NULL
);
ALTER TABLE xxxxxx.codeql_scanning_config
    ADD CONSTRAINT codeql_scanning_config_pk PRIMARY KEY (gid);
ALTER TABLE xxxxxx.codeql_scanning_config
   ADD FOREIGN KEY (gid) REFERENCES xxxxxx.projects(gid);

-- xxxxxx.repos_checking
DROP TABLE IF EXISTS xxxxxx.repos_checking CASCADE;
CREATE TABLE xxxxxx.repos_checking (
  gid BIGINT UNIQUE,
  status integer DEFAULT 0
);
ALTER TABLE
  xxxxxx.repos_checking
ADD
  CONSTRAINT repos_checking_pkey PRIMARY KEY (gid);

-- commit_meta
DROP TABLE IF EXISTS xxxxxx.commit_meta CASCADE;
CREATE TABLE xxxxxx.commit_meta (
  gid BIGINT,
  jid BIGINT UNIQUE,
  author text DEFAULT NULL,
  author_name text DEFAULT NULL,
  email text DEFAULT NULL
);
ALTER TABLE xxxxxx.commit_meta
    ADD CONSTRAINT commit_meta_pk PRIMARY KEY (jid);
ALTER TABLE xxxxxx.commit_meta
   ADD FOREIGN KEY (jid) REFERENCES xxxxxx.jobs(id);
ALTER TABLE xxxxxx.commit_meta
   ADD FOREIGN KEY (gid) REFERENCES xxxxxx.projects(gid);


-- Analysis_VIEW
DROP VIEW IF EXISTS Analysis_VIEW;
CREATE view Analysis_VIEW
AS
select
	j.gid,
	published,
	--published :: date - codeql_since :: date as timediff,
	EXTRACT(EPOCH FROM (published - codeql_since))::bigint as timediff,
    count(r.id) FILTER (WHERE ruleid = 'js/html-constructed-from-input') as "html_constructed_from_input",
    count(r.id) FILTER (WHERE ruleid = 'js/reflected-xss') as "reflected_xss",
    count(r.id) FILTER (WHERE ruleid = 'js/stored-xss') as "stored_xss",
    count(r.id) FILTER (WHERE ruleid = 'js/unsafe-jquery-plugin') as "unsafe_jquery_plugin",
    count(r.id) FILTER (WHERE ruleid = 'js/xss') as "xss",
    count(r.id) FILTER (WHERE ruleid = 'js/xss-through-dom') as "xss_through_dom",
    count(r.id) FILTER (WHERE ruleid = 'js/xss-through-exception') as "xss_through_exception",
    count(r.id) FILTER (WHERE ruleid = 'py/incomplete-hostname-regexp') as "incomplete_hostname_regexp",
    count(r.id) FILTER (WHERE ruleid = 'py/incomplete-url-substring-sanitization') as "incomplete_url_substring_sanitization",
    count(r.id) FILTER (WHERE ruleid = 'py/overly-large-range') as "overly_large_range",
    count(r.id) as overall,
    j.id
from
	jsample.jobs j
    left outer join jsample.results r on j.id = r.jid
    inner join jsample.project_meta p on j.gid = p.gid
WHERE
	j.status = 1
group by
	published,
	j.id,
    j.gid,
    codeql_since
;

--Analysis_TABLE
DROP TABLE IF EXISTS Analysis_TABLE;
CREATE TABLE Analysis_TABLE AS SELECT * FROM Analysis_VIEW;
CREATE INDEX analysis_table_index_1 on analysis_table(gid ASC);
ALTER TABLE Analysis_TABLE
   ADD FOREIGN KEY (gid) REFERENCES xxxxxx.projects(gid);

--@weekly
-- SIMILAR TO '"[0-9]* [0-9]* \* \* [0-9]*"'

