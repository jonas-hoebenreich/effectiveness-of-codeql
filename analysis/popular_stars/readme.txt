[1] "Log information"
[1] "folder: popular_stars"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative     
Actual                   2,4              487,5          
Prediction (s.d.)        2,5 (0,032)      497,8 (6,374)  
95% CI                   [2,4, 2,6]       [485,5, 510,9] 
                                                         
Absolute effect (s.d.)   -0,051 (0,032)   -10,296 (6,374)
95% CI                   [-0,12, 0,01]    [-23,44, 2,00] 
                                                         
Relative effect (s.d.)   -2,1% (1,3%)     -2,1% (1,3%)   
95% CI                   [-4,7%, 0,4%]    [-4,7%, 0,4%]  

Posterior tail-area probability p:   0,05092
Posterior prob. of a causal effect:  95%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 2,44. In the absence of an intervention, we would have expected an average response of 2,49. The 95% interval of this counterfactual prediction is [2,43, 2,55]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,051 with a 95% interval of [-0,12, 0,010]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 487,47. Had the intervention not taken place, we would have expected a sum of 497,77. The 95% interval of this prediction is [485,46, 510,91].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-5%, +0%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,051. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   2,4               1528,1           
Prediction (s.d.)        2,5 (0,032)       1532,2 (19,680)  
95% CI                   [2,4, 2,5]        [1493,9, 1570,0] 
                                                            
Absolute effect (s.d.)   -0,0065 (0,032)   -4,0774 (19,680) 
95% CI                   [-0,067, 0,055]   [-41,860, 34,204]
                                                            
Relative effect (s.d.)   -0,27% (1,3%)     -0,27% (1,3%)    
95% CI                   [-2,7%, 2,2%]     [-2,7%, 2,2%]    

Posterior tail-area probability p:   0,41039
Posterior prob. of a causal effect:  59%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 2,45. In the absence of an intervention, we would have expected an average response of 2,46. The 95% interval of this counterfactual prediction is [2,39, 2,52]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0065 with a 95% interval of [-0,067, 0,055]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,53K. Had the intervention not taken place, we would have expected a sum of 1,53K. The 95% interval of this prediction is [1,49K, 1,57K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -0%. The 95% interval of this percentage is [-3%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,41. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,45                89,88            
Prediction (s.d.)        0,43 (0,0091)       86,39 (1,8167)   
95% CI                   [0,41, 0,45]        [82,90, 89,94]   
                                                              
Absolute effect (s.d.)   0,017 (0,0091)      3,487 (1,8167)   
95% CI                   [-0,00034, 0,035]   [-0,06827, 6,971]
                                                              
Relative effect (s.d.)   4% (2,1%)           4% (2,1%)        
95% CI                   [-0,079%, 8,1%]     [-0,079%, 8,1%]  

Posterior tail-area probability p:   0,0308
Posterior prob. of a causal effect:  96,92%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,45. In the absence of an intervention, we would have expected an average response of 0,43. The 95% interval of this counterfactual prediction is [0,41, 0,45]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,017 with a 95% interval of [-0,00034, 0,035]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 89,88. Had the intervention not taken place, we would have expected a sum of 86,39. The 95% interval of this prediction is [82,90, 89,94].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +4%. The 95% interval of this percentage is [-0%, +8%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,031). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,46             287,51          
Prediction (s.d.)        0,44 (0,011)     271,78 (6,885)  
95% CI                   [0,41, 0,46]     [258,19, 285,00]
                                                          
Absolute effect (s.d.)   0,025 (0,011)    15,725 (6,885)  
95% CI                   [0,004, 0,047]   [2,505, 29,319] 
                                                          
Relative effect (s.d.)   5,8% (2,5%)      5,8% (2,5%)     
95% CI                   [0,92%, 11%]     [0,92%, 11%]    

Posterior tail-area probability p:   0,00824
Posterior prob. of a causal effect:  99,17611%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,46. By contrast, in the absence of an intervention, we would have expected an average response of 0,44. The 95% interval of this counterfactual prediction is [0,41, 0,46]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,025 with a 95% interval of [0,0040, 0,047]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 287,51. By contrast, had the intervention not taken place, we would have expected a sum of 271,78. The 95% interval of this prediction is [258,19, 285,00].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +6%. The 95% interval of this percentage is [+1%, +11%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,025) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,008). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,017               3,427            
Prediction (s.d.)        0,015 (0,00089)     2,914 (0,17713)  
95% CI                   [0,013, 0,016]      [2,573, 3,282]   
                                                              
Absolute effect (s.d.)   0,0026 (0,00089)    0,5138 (0,17713) 
95% CI                   [0,00073, 0,0043]   [0,14526, 0,8547]
                                                              
Relative effect (s.d.)   18% (6,1%)          18% (6,1%)       
95% CI                   [5%, 29%]           [5%, 29%]        

Posterior tail-area probability p:   0,00409
Posterior prob. of a causal effect:  99,59142%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,017. By contrast, in the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,013, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0026 with a 95% interval of [0,00073, 0,0043]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,43. By contrast, had the intervention not taken place, we would have expected a sum of 2,91. The 95% interval of this prediction is [2,57, 3,28].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +18%. The 95% interval of this percentage is [+5%, +29%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0026) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,004). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,019              12,152          
Prediction (s.d.)        0,015 (0,00051)    9,553 (0,31861) 
95% CI                   [0,014, 0,016]     [8,918, 10,176] 
                                                            
Absolute effect (s.d.)   0,0042 (0,00051)   2,5995 (0,31861)
95% CI                   [0,0032, 0,0052]   [1,9767, 3,2340]
                                                            
Relative effect (s.d.)   27% (3,3%)         27% (3,3%)      
95% CI                   [21%, 34%]         [21%, 34%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8995%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,019. By contrast, in the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0042 with a 95% interval of [0,0032, 0,0052]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 12,15. By contrast, had the intervention not taken place, we would have expected a sum of 9,55. The 95% interval of this prediction is [8,92, 10,18].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +27%. The 95% interval of this percentage is [+21%, +34%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0042) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,0021              0,4165           
Prediction (s.d.)        0,0013 (0,00025)    0,2651 (0,04953) 
95% CI                   [0,00086, 0,0018]   [0,17129, 0,3640]
                                                              
Absolute effect (s.d.)   0,00076 (0,00025)   0,15142 (0,04953)
95% CI                   [0,00026, 0,0012]   [0,05246, 0,2452]
                                                              
Relative effect (s.d.)   57% (19%)           57% (19%)        
95% CI                   [20%, 93%]          [20%, 93%]       

Posterior tail-area probability p:   0,00406
Posterior prob. of a causal effect:  99,59391%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0021. By contrast, in the absence of an intervention, we would have expected an average response of 0,0013. The 95% interval of this counterfactual prediction is [0,00086, 0,0018]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00076 with a 95% interval of [0,00026, 0,0012]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,42. By contrast, had the intervention not taken place, we would have expected a sum of 0,27. The 95% interval of this prediction is [0,17, 0,36].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +57%. The 95% interval of this percentage is [+20%, +93%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,00076) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,004). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,0027             1,6670          
Prediction (s.d.)        0,0013 (0,00013)   0,8288 (0,07973)
95% CI                   [0,0011, 0,0016]   [0,6714, 0,9821]
                                                            
Absolute effect (s.d.)   0,0013 (0,00013)   0,8382 (0,07973)
95% CI                   [0,0011, 0,0016]   [0,6849, 0,9956]
                                                            
Relative effect (s.d.)   101% (9,6%)        101% (9,6%)     
95% CI                   [83%, 120%]        [83%, 120%]     

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8997%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0027. By contrast, in the absence of an intervention, we would have expected an average response of 0,0013. The 95% interval of this counterfactual prediction is [0,0011, 0,0016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0013 with a 95% interval of [0,0011, 0,0016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,67. By contrast, had the intervention not taken place, we would have expected a sum of 0,83. The 95% interval of this prediction is [0,67, 0,98].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +101%. The 95% interval of this percentage is [+83%, +120%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0013) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,73              146,59          
Prediction (s.d.)        0,75 (0,012)      149,60 (2,445)  
95% CI                   [0,72, 0,77]      [144,82, 154,67]
                                                           
Absolute effect (s.d.)   -0,015 (0,012)    -3,015 (2,445)  
95% CI                   [-0,04, 0,0088]   [-8,08, 1,7664] 
                                                           
Relative effect (s.d.)   -2% (1,6%)        -2% (1,6%)      
95% CI                   [-5,4%, 1,2%]     [-5,4%, 1,2%]   

Posterior tail-area probability p:   0,1043
Posterior prob. of a causal effect:  90%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,73. In the absence of an intervention, we would have expected an average response of 0,75. The 95% interval of this counterfactual prediction is [0,72, 0,77]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,015 with a 95% interval of [-0,040, 0,0088]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 146,59. Had the intervention not taken place, we would have expected a sum of 149,60. The 95% interval of this prediction is [144,82, 154,67].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-5%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,104. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,73              453,97          
Prediction (s.d.)        0,75 (0,011)      465,92 (6,843)  
95% CI                   [0,72, 0,77]      [452,32, 479,13]
                                                           
Absolute effect (s.d.)   -0,019 (0,011)    -11,958 (6,843) 
95% CI                   [-0,04, 0,0026]   [-25,17, 1,6434]
                                                           
Relative effect (s.d.)   -2,6% (1,5%)      -2,6% (1,5%)    
95% CI                   [-5,4%, 0,35%]    [-5,4%, 0,35%]  

Posterior tail-area probability p:   0,03882
Posterior prob. of a causal effect:  96,118%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,73. In the absence of an intervention, we would have expected an average response of 0,75. The 95% interval of this counterfactual prediction is [0,72, 0,77]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,019 with a 95% interval of [-0,040, 0,0026]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 453,97. Had the intervention not taken place, we would have expected a sum of 465,92. The 95% interval of this prediction is [452,32, 479,13].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, +0%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,039). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,11               22,42           
Prediction (s.d.)        0,11 (0,0083)      22,96 (1,6691)  
95% CI                   [0,098, 0,13]      [19,690, 26,37] 
                                                            
Absolute effect (s.d.)   -0,0027 (0,0083)   -0,5368 (1,6691)
95% CI                   [-0,02, 0,014]     [-3,95, 2,734]  
                                                            
Relative effect (s.d.)   -2,3% (7,3%)       -2,3% (7,3%)    
95% CI                   [-17%, 12%]        [-17%, 12%]     

Posterior tail-area probability p:   0,37958
Posterior prob. of a causal effect:  62%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,11. In the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,098, 0,13]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0027 with a 95% interval of [-0,020, 0,014]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 22,42. Had the intervention not taken place, we would have expected a sum of 22,96. The 95% interval of this prediction is [19,69, 26,37].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-17%, +12%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,38. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative        
Actual                   0,11                69,51             
Prediction (s.d.)        0,12 (0,0055)       77,49 (3,4489)    
95% CI                   [0,11, 0,13]        [70,71, 84,15]    
                                                               
Absolute effect (s.d.)   -0,013 (0,0055)     -7,982 (3,4489)   
95% CI                   [-0,023, -0,0019]   [-14,637, -1,1963]
                                                               
Relative effect (s.d.)   -10% (4,5%)         -10% (4,5%)       
95% CI                   [-19%, -1,5%]       [-19%, -1,5%]     

Posterior tail-area probability p:   0,01518
Posterior prob. of a causal effect:  98,482%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,11. By contrast, in the absence of an intervention, we would have expected an average response of 0,12. The 95% interval of this counterfactual prediction is [0,11, 0,13]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,013 with a 95% interval of [-0,023, -0,0019]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 69,51. By contrast, had the intervention not taken place, we would have expected a sum of 77,49. The 95% interval of this prediction is [70,71, 84,15].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -10%. The 95% interval of this percentage is [-19%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,015). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,1                218,3            
Prediction (s.d.)        1,1 (0,02)         226,6 (3,96)     
95% CI                   [1,1, 1,2]         [219,2, 234,4]   
                                                             
Absolute effect (s.d.)   -0,041 (0,02)      -8,239 (3,96)    
95% CI                   [-0,08, -0,0046]   [-16,06, -0,9142]
                                                             
Relative effect (s.d.)   -3,6% (1,7%)       -3,6% (1,7%)     
95% CI                   [-7,1%, -0,4%]     [-7,1%, -0,4%]   

Posterior tail-area probability p:   0,01475
Posterior prob. of a causal effect:  98,525%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,09. By contrast, in the absence of an intervention, we would have expected an average response of 1,13. The 95% interval of this counterfactual prediction is [1,10, 1,17]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,041 with a 95% interval of [-0,080, -0,0046]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 218,32. By contrast, had the intervention not taken place, we would have expected a sum of 226,56. The 95% interval of this prediction is [219,23, 234,38].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-7%, -0%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,015). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   1,1               682,4            
Prediction (s.d.)        1,1 (0,018)       690,1 (11,110)   
95% CI                   [1,1, 1,1]        [668,2, 711,2]   
                                                            
Absolute effect (s.d.)   -0,012 (0,018)    -7,740 (11,110)  
95% CI                   [-0,046, 0,023]   [-28,854, 14,236]
                                                            
Relative effect (s.d.)   -1,1% (1,6%)      -1,1% (1,6%)     
95% CI                   [-4,2%, 2,1%]     [-4,2%, 2,1%]    

Posterior tail-area probability p:   0,24316
Posterior prob. of a causal effect:  76%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,09. In the absence of an intervention, we would have expected an average response of 1,11. The 95% interval of this counterfactual prediction is [1,07, 1,14]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,012 with a 95% interval of [-0,046, 0,023]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 682,39. Had the intervention not taken place, we would have expected a sum of 690,13. The 95% interval of this prediction is [668,15, 711,24].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-4%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,243. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,032               6,421            
Prediction (s.d.)        0,029 (0,0029)      5,846 (0,5775)   
95% CI                   [0,024, 0,035]      [4,743, 7,056]   
                                                              
Absolute effect (s.d.)   0,0029 (0,0029)     0,5746 (0,5775)  
95% CI                   [-0,0032, 0,0084]   [-0,6353, 1,6782]
                                                              
Relative effect (s.d.)   9,8% (9,9%)         9,8% (9,9%)      
95% CI                   [-11%, 29%]         [-11%, 29%]      

Posterior tail-area probability p:   0,14834
Posterior prob. of a causal effect:  85%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,032. In the absence of an intervention, we would have expected an average response of 0,029. The 95% interval of this counterfactual prediction is [0,024, 0,035]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0029 with a 95% interval of [-0,0032, 0,0084]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 6,42. Had the intervention not taken place, we would have expected a sum of 5,85. The 95% interval of this prediction is [4,74, 7,06].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +10%. The 95% interval of this percentage is [-11%, +29%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,148. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,034               20,940           
Prediction (s.d.)        0,03 (0,0015)       18,82 (0,9414)   
95% CI                   [0,027, 0,033]      [16,953, 20,639] 
                                                              
Absolute effect (s.d.)   0,0034 (0,0015)     2,1219 (0,9414)  
95% CI                   [0,00048, 0,0064]   [0,30158, 3,9871]
                                                              
Relative effect (s.d.)   11% (5%)            11% (5%)         
95% CI                   [1,6%, 21%]         [1,6%, 21%]      

Posterior tail-area probability p:   0,00904
Posterior prob. of a causal effect:  99,09639%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,034. By contrast, in the absence of an intervention, we would have expected an average response of 0,030. The 95% interval of this counterfactual prediction is [0,027, 0,033]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0034 with a 95% interval of [0,00048, 0,0064]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 20,94. By contrast, had the intervention not taken place, we would have expected a sum of 18,82. The 95% interval of this prediction is [16,95, 20,64].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +11%. The 95% interval of this percentage is [+2%, +21%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0034) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,009). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 291"
[1] "number of repositories <=-95% top_performer: 24     8,24742268041237 %"
[1] "number of repositories <0 good_performer: 37     12,7147766323024 %"
[1] "number of repositories =0 no_change_with_problems: 188     64,6048109965636 %"
[1] "number of repositories >0 worst_performer: 42     14,4329896907216 %"
[1] "sum problems added - problems fixed: -96,6848324268846"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 63"
[1] "number of repositories <=-95% top_performer: 4     6,34920634920635 %"
[1] "number of repositories <0 good_performer: 4     6,34920634920635 %"
[1] "number of repositories =0 no_change_with_problems: 47     74,6031746031746 %"
[1] "number of repositories >0 worst_performer: 8     12,6984126984127 %"
[1] "sum problems added - problems fixed: 3,55579684040676"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 18"
[1] "number of repositories <=-95% top_performer: 2     11,1111111111111 %"
[1] "number of repositories <0 good_performer: 2     11,1111111111111 %"
[1] "number of repositories =0 no_change_with_problems: 9     50 %"
[1] "number of repositories >0 worst_performer: 5     27,7777777777778 %"
[1] "sum problems added - problems fixed: -0,0876984126984129"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 1     100 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: 0"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 113"
[1] "number of repositories <=-95% top_performer: 6     5,30973451327434 %"
[1] "number of repositories <0 good_performer: 9     7,9646017699115 %"
[1] "number of repositories =0 no_change_with_problems: 87     76,9911504424779 %"
[1] "number of repositories >0 worst_performer: 11     9,73451327433628 %"
[1] "sum problems added - problems fixed: -21,587020701352"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 68"
[1] "number of repositories <=-95% top_performer: 8     11,7647058823529 %"
[1] "number of repositories <0 good_performer: 9     13,2352941176471 %"
[1] "number of repositories =0 no_change_with_problems: 46     67,6470588235294 %"
[1] "number of repositories >0 worst_performer: 5     7,35294117647059 %"
[1] "sum problems added - problems fixed: -23,2688263442285"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 224"
[1] "number of repositories <=-95% top_performer: 20     8,92857142857143 %"
[1] "number of repositories <0 good_performer: 25     11,1607142857143 %"
[1] "number of repositories =0 no_change_with_problems: 151     67,4107142857143 %"
[1] "number of repositories >0 worst_performer: 28     12,5 %"
[1] "sum problems added - problems fixed: -57,9859726979013"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 1509"
[1] "number of repos with problems in this 90 day timeframe: 10"
[1] "number of repositories <=-95% top_performer: 1     10 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 7     70 %"
[1] "number of repositories >0 worst_performer: 2     20 %"
[1] "sum problems added - problems fixed: 2,68888888888889"
[1] "number of repos with overall problems in this 700 day timeframe: 346"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 95"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 27"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 5"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 163"
[1] "number of repos with xss problems in this 700 day timeframe: 116"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 265"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 18"
