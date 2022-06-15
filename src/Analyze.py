#!/usr/bin/env python
import logging

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
import datetime
from src.Database import Database

sns.set_theme()
sns.set_style('darkgrid')


# Analyze Data und safe it to csv files
class Analyze:
    database = None
    dfs = None
    path = ''
    gids = []

    def __init__(self, path, where):
        logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO,
                            datefmt="%H:%M:%S")
        logging.info('Hello from Analyze')
        self.database = Database()
        self.path = path
        self.gids = self.database.get_gids_by_where(where)
        self.dfs = self.create_frame_repos()
        logging.info('raw data loaded successfully')

    # Process the data from one repository
    # 1. extrapolate at the end
    # 2. load pandas DataFrame
    # 3. Interpolate missing results
    def repo_day_diff_commit_all_problems(self, data):
        if len(data) > 0:
            if data[0][0] != '-500000000 seconds':  # '-43200000 seconds':
                data.insert(0, ['-500000000 seconds', data[0][1]])
            if data[len(data) - 1][0] != '54000000 seconds':  # '17280000 seconds':
                data.append(['54000000 seconds', data[len(data) - 1][1]])
        df = pd.DataFrame.from_records(data=data, columns=['timestamp', 'result'])
        df.index = pd.to_timedelta(df.timestamp)
        dfn = df.resample('1D').mean().interpolate()
        return dfn

    # safe csv file for overall performance across all rules
    def repos_analyze_all_problems(self):
        logging.info('starting repos_analyze_all_problems')
        for method in ['mean']:  # add support for additional pandas methods (mad, median, ...)
            i = 0
            for column in ['html_constructed_from_input', 'reflected_xss', 'stored_xss', 'unsafe_jquery_plugin', 'xss',
                           'xss_through_dom', 'xss_through_exception', 'overall']:
                df = pd.concat(self.dfs[i])
                i += 1
                if method == 'mean':
                    foo = df.groupby(by='timestamp').mean()
                else: # TODO if you want to use another pandas method
                    foo = df.groupby(by='timestamp').mad()
                # safe result in csv file
                result_all = "x\n"  # file for time frame -5788 to 624 days
                for x in range(0, 6413):
                    result_all += str(foo.result.values[x]) + '\n'
                result = "x\n"  # file for -500 to 200 days
                for x in range(5287, 5988):
                    result += str(foo.result.values[x]) + '\n' # str(x) + '\n'
                f = open(self.path + column + '_' + method + '.csv', "w")
                f.write(result)
                f.close()
                f = open(self.path + column + '_' + method + '_all.csv', "w")
                f.write(result_all)
                f.close()

    # load data frames from Database
    def create_frame_repos(self):
        dfs = [[], [], [], [], [], [], [], []]
        for gid in self.gids:
            data = self.database.single_day_diff_all_results_for_gid(gid)
            for i in range(1, 9):
                d = [(x[0], x[i]) for x in data]
                dfa = self.repo_day_diff_commit_all_problems(d)
                if not dfa.empty:
                    dfs[i - 1].append(dfa)
        return dfs

    # create csv file for problems vs js file size plots
    def avg_problems_vs_jssize(self):
        r = self.database.get_avg_problems_vs_jssize(self.gids)
        result = 'javascript_size,avg_problems\n'
        for x in r:
            result += str(x[0]) + ',' + str(x[1]) + '\n'
        f = open(self.path + "avg_problems_vs_jssize.csv", "w")
        f.write(result)
        f.close()

    # create csv files for 45 day before vs 45 day after plots
    def repos_before_after_comparison(self):
        i = 0
        for column in ['html_constructed_from_input', 'reflected_xss', 'stored_xss', 'unsafe_jquery_plugin', 'xss',
                       'xss_through_dom', 'xss_through_exception', 'overall']:
            result = "gid,before,after,change,change_percentage\n"
            for a in range(0, len(self.gids)):
                mean_before = 0
                mean_after = 0
                for b in range(5742, 5787):
                    mean_before = mean_before + self.dfs[i][a].values[b][0]
                    mean_after = mean_after + self.dfs[i][a].values[b + 46][0]
                mean_before = mean_before / 45
                mean_after = mean_after / 45
                change_percentage = (mean_after - mean_before) / (mean_before + numpy.nextafter(0, 1))
                result += str(self.gids[a]) + ',' + \
                          str(mean_before) + ',' + \
                          str(mean_after) + ',' + \
                          str(mean_after - mean_before) + ',' + \
                          str(change_percentage) + '\n'
            f = open(self.path + column + '_repos_before_after_comparison.csv', "w")
            f.write(result)
            f.close()
            i += 1

    # create csv files for individual plot performance
    def repos_individual_development(self):
        columns = ['html_constructed_from_input', 'reflected_xss', 'stored_xss', 'unsafe_jquery_plugin', 'xss',
                       'xss_through_dom', 'xss_through_exception', 'overall']
        for c in range(0, 8):
            result = 'index'
            relevant_gids = []
            for gid in range(0, len(self.gids)):
                if max(self.dfs[c][gid].values) != min(self.dfs[c][gid].values):  # ignore constanct repos
                    result += ',' + str(self.gids[gid])
                    relevant_gids.append(gid)
            result += '\n'
            for index in range(5288, 5989):
                result += str(index-5788)
                for gid in relevant_gids:
                    result += ',' + str(self.dfs[c][gid].values[index][0])
                result += '\n'
            f = open(self.path + columns[c] + '_repos_individual_development.csv', "w")
            f.write(result)
            f.close()
