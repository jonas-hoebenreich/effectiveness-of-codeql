the following folder contain the results of the analysis script:

- 305507071: just the repository with the GitHub ID: 305507071
- not_trigger_push: repositories that are not scanned on push
- 334191697_369692262: just the repositories with the GitHub ID: 334191697 & 369692262
- not_weekly: repositories that are not scanned weekly
- all_excl4287066: all repositories (excluding excl4287066)
- popular_stars: repositories with more than 10 stars
- all_excl_4287066_334191697_369692262: all repositories excluding 4287066 & 334191697 & 369692262
- best_performing: repositories with better performance after CodeQL
- trigger_pull_request: repositories that are scanned on pull request
- less_than_5_contributors: repositories with less than 5 contributors
- trigger_push: repositories that are scanned on push
- more_than_4_contributors: repositories that have more than 4 contributors
- weekly: repositories that are scanned weekly
- not_popular_stars: repositories that have 10 or fewer stars
- worst_performing: repositories with worse performance after CodeQL was enabled
- not_trigger_pull_request: repositories that are not scanned on pull request

files:
every file generally contains multiple keywords:
    - rule (xss_through_exception, xss, overall etc): CodeQL query used for this graph
    - _raw: no CausalImpact analysis
    - _CausalImpact_: result by CausalImpact
    - cumulative / original / pointwise: CausalImpact metric
    - mean: mathematical function used to calculate the data
    - _all: whole period
