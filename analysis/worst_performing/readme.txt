[1] "Log information"
[1] "folder: worst_performing"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average       Cumulative    
Actual                   12            2322          
Prediction (s.d.)        11 (0,28)     2178 (56,40)  
95% CI                   [10, 11]      [2065, 2290]  
                                                     
Absolute effect (s.d.)   0,72 (0,28)   144,12 (56,40)
95% CI                   [0,16, 1,3]   [31,44, 256,4]
                                                     
Relative effect (s.d.)   6,6% (2,6%)   6,6% (2,6%)   
95% CI                   [1,4%, 12%]   [1,4%, 12%]   

Posterior tail-area probability p:   0,00713
Posterior prob. of a causal effect:  99,28717%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 11,61. By contrast, in the absence of an intervention, we would have expected an average response of 10,89. The 95% interval of this counterfactual prediction is [10,33, 11,45]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,72 with a 95% interval of [0,16, 1,28]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 2,32K. By contrast, had the intervention not taken place, we would have expected a sum of 2,18K. The 95% interval of this prediction is [2,07K, 2,29K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +7%. The 95% interval of this percentage is [+1%, +12%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,72) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,007). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average      Cumulative    
Actual                   12           7218          
Prediction (s.d.)        10 (0,17)    6361 (104,76) 
95% CI                   [9,9, 11]    [6162,0, 6566]
                                                    
Absolute effect (s.d.)   1,4 (0,17)   856,5 (104,76)
95% CI                   [1, 1,7]     [652, 1055,9] 
                                                    
Relative effect (s.d.)   13% (1,6%)   13% (1,6%)    
95% CI                   [10%, 17%]   [10%, 17%]    

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8995%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 11,57. By contrast, in the absence of an intervention, we would have expected an average response of 10,19. The 95% interval of this counterfactual prediction is [9,88, 10,52]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 1,37 with a 95% interval of [1,05, 1,69]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 7,22K. By contrast, had the intervention not taken place, we would have expected a sum of 6,36K. The 95% interval of this prediction is [6,16K, 6,57K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +13%. The 95% interval of this percentage is [+10%, +17%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (1,37) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   1,8              353,6           
Prediction (s.d.)        1,7 (0,07)       345,8 (13,94)   
95% CI                   [1,6, 1,9]       [320,1, 370,1]  
                                                          
Absolute effect (s.d.)   0,039 (0,07)     7,769 (13,94)   
95% CI                   [-0,082, 0,17]   [-16,488, 33,48]
                                                          
Relative effect (s.d.)   2,2% (4%)        2,2% (4%)       
95% CI                   [-4,8%, 9,7%]    [-4,8%, 9,7%]   

Posterior tail-area probability p:   0,33087
Posterior prob. of a causal effect:  67%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,77. In the absence of an intervention, we would have expected an average response of 1,73. The 95% interval of this counterfactual prediction is [1,60, 1,85]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,039 with a 95% interval of [-0,082, 0,17]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 353,58. Had the intervention not taken place, we would have expected a sum of 345,81. The 95% interval of this prediction is [320,10, 370,07].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +2%. The 95% interval of this percentage is [-5%, +10%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,331. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average         Cumulative      
Actual                   1,8             1122,8          
Prediction (s.d.)        1,6 (0,037)     1026,4 (23,191) 
95% CI                   [1,6, 1,7]      [981,8, 1071,0] 
                                                         
Absolute effect (s.d.)   0,15 (0,037)    96,47 (23,191)  
95% CI                   [0,083, 0,23]   [51,861, 141,03]
                                                         
Relative effect (s.d.)   9,4% (2,3%)     9,4% (2,3%)     
95% CI                   [5,1%, 14%]     [5,1%, 14%]     

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,80. By contrast, in the absence of an intervention, we would have expected an average response of 1,64. The 95% interval of this counterfactual prediction is [1,57, 1,72]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,15 with a 95% interval of [0,083, 0,23]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,12K. By contrast, had the intervention not taken place, we would have expected a sum of 1,03K. The 95% interval of this prediction is [0,98K, 1,07K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +9%. The 95% interval of this percentage is [+5%, +14%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,15) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,15             29,40           
Prediction (s.d.)        0,091 (0,0037)   18,174 (0,7445) 
95% CI                   [0,084, 0,099]   [16,771, 19,714]
                                                          
Absolute effect (s.d.)   0,056 (0,0037)   11,228 (0,7445) 
95% CI                   [0,048, 0,063]   [9,689, 12,631] 
                                                          
Relative effect (s.d.)   62% (4,1%)       62% (4,1%)      
95% CI                   [53%, 70%]       [53%, 70%]      

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89723%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,15. By contrast, in the absence of an intervention, we would have expected an average response of 0,091. The 95% interval of this counterfactual prediction is [0,084, 0,099]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,056 with a 95% interval of [0,048, 0,063]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 29,40. By contrast, had the intervention not taken place, we would have expected a sum of 18,17. The 95% interval of this prediction is [16,77, 19,71].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +62%. The 95% interval of this percentage is [+53%, +70%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,056) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,15             96,28           
Prediction (s.d.)        0,087 (0,0022)   54,509 (1,3878) 
95% CI                   [0,083, 0,092]   [51,723, 57,213]
                                                          
Absolute effect (s.d.)   0,067 (0,0022)   41,771 (1,3878) 
95% CI                   [0,063, 0,071]   [39,068, 44,557]
                                                          
Relative effect (s.d.)   77% (2,5%)       77% (2,5%)      
95% CI                   [72%, 82%]       [72%, 82%]      

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8997%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,15. By contrast, in the absence of an intervention, we would have expected an average response of 0,087. The 95% interval of this counterfactual prediction is [0,083, 0,092]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,067 with a 95% interval of [0,063, 0,071]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 96,28. By contrast, had the intervention not taken place, we would have expected a sum of 54,51. The 95% interval of this prediction is [51,72, 57,21].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +77%. The 95% interval of this percentage is [+72%, +82%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,067) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,04               8,04            
Prediction (s.d.)        0,035 (0,00077)    6,906 (0,15458) 
95% CI                   [0,033, 0,036]     [6,597, 7,217]  
                                                            
Absolute effect (s.d.)   0,0057 (0,00077)   1,1367 (0,15458)
95% CI                   [0,0041, 0,0072]   [0,8259, 1,4452]
                                                            
Relative effect (s.d.)   16% (2,2%)         16% (2,2%)      
95% CI                   [12%, 21%]         [12%, 21%]      

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89701%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,040. By contrast, in the absence of an intervention, we would have expected an average response of 0,035. The 95% interval of this counterfactual prediction is [0,033, 0,036]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0057 with a 95% interval of [0,0041, 0,0072]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 8,04. By contrast, had the intervention not taken place, we would have expected a sum of 6,91. The 95% interval of this prediction is [6,60, 7,22].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +16%. The 95% interval of this percentage is [+12%, +21%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0057) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,042              26,177          
Prediction (s.d.)        0,035 (0,00038)    21,602 (0,23614)
95% CI                   [0,034, 0,035]     [21,129, 22,067]
                                                            
Absolute effect (s.d.)   0,0073 (0,00038)   4,5751 (0,23614)
95% CI                   [0,0066, 0,0081]   [4,1105, 5,0480]
                                                            
Relative effect (s.d.)   21% (1,1%)         21% (1,1%)      
95% CI                   [19%, 23%]         [19%, 23%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8994%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,042. By contrast, in the absence of an intervention, we would have expected an average response of 0,035. The 95% interval of this counterfactual prediction is [0,034, 0,035]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0073 with a 95% interval of [0,0066, 0,0081]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 26,18. By contrast, had the intervention not taken place, we would have expected a sum of 21,60. The 95% interval of this prediction is [21,13, 22,07].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +21%. The 95% interval of this percentage is [+19%, +23%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0073) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   3,2              646,1           
Prediction (s.d.)        3,1 (0,069)      628,2 (13,855)  
95% CI                   [3, 3,3]         [602, 656,3]    
                                                          
Absolute effect (s.d.)   0,09 (0,069)     17,94 (13,855)  
95% CI                   [-0,051, 0,22]   [-10,131, 43,92]
                                                          
Relative effect (s.d.)   2,9% (2,2%)      2,9% (2,2%)     
95% CI                   [-1,6%, 7%]      [-1,6%, 7%]     

Posterior tail-area probability p:   0,0954
Posterior prob. of a causal effect:  90%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 3,23. In the absence of an intervention, we would have expected an average response of 3,14. The 95% interval of this counterfactual prediction is [3,01, 3,28]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,090 with a 95% interval of [-0,051, 0,22]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 646,13. Had the intervention not taken place, we would have expected a sum of 628,19. The 95% interval of this prediction is [602,21, 656,26].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +3%. The 95% interval of this percentage is [-2%, +7%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,095. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average         Cumulative      
Actual                   3,2             1965,9          
Prediction (s.d.)        3 (0,048)       1852 (29,756)   
95% CI                   [2,9, 3,1]      [1794,8, 1909,2]
                                                         
Absolute effect (s.d.)   0,18 (0,048)    113,91 (29,756) 
95% CI                   [0,091, 0,27]   [56,705, 171,08]
                                                         
Relative effect (s.d.)   6,2% (1,6%)     6,2% (1,6%)     
95% CI                   [3,1%, 9,2%]    [3,1%, 9,2%]    

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8995%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 3,15. By contrast, in the absence of an intervention, we would have expected an average response of 2,97. The 95% interval of this counterfactual prediction is [2,88, 3,06]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,18 with a 95% interval of [0,091, 0,27]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,97K. By contrast, had the intervention not taken place, we would have expected a sum of 1,85K. The 95% interval of this prediction is [1,79K, 1,91K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +6%. The 95% interval of this percentage is [+3%, +9%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,18) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   0,92           184,98          
Prediction (s.d.)        0,59 (0,028)   118,82 (5,628)  
95% CI                   [0,54, 0,65]   [107,99, 130,11]
                                                        
Absolute effect (s.d.)   0,33 (0,028)   66,16 (5,628)   
95% CI                   [0,27, 0,38]   [54,87, 76,99]  
                                                        
Relative effect (s.d.)   56% (4,7%)     56% (4,7%)      
95% CI                   [46%, 65%]     [46%, 65%]      

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89754%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,92. By contrast, in the absence of an intervention, we would have expected an average response of 0,59. The 95% interval of this counterfactual prediction is [0,54, 0,65]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,33 with a 95% interval of [0,27, 0,38]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 184,98. By contrast, had the intervention not taken place, we would have expected a sum of 118,82. The 95% interval of this prediction is [107,99, 130,11].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +56%. The 95% interval of this percentage is [+46%, +65%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,33) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average        Cumulative     
Actual                   0,93           582,11         
Prediction (s.d.)        0,57 (0,016)   353,76 (10,085)
95% CI                   [0,53, 0,6]    [333,78, 373,6]
                                                       
Absolute effect (s.d.)   0,37 (0,016)   228,36 (10,085)
95% CI                   [0,33, 0,4]    [208,47, 248,3]
                                                       
Relative effect (s.d.)   65% (2,9%)     65% (2,9%)     
95% CI                   [59%, 70%]     [59%, 70%]     

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89785%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,93. By contrast, in the absence of an intervention, we would have expected an average response of 0,57. The 95% interval of this counterfactual prediction is [0,53, 0,60]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,37 with a 95% interval of [0,33, 0,40]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 582,11. By contrast, had the intervention not taken place, we would have expected a sum of 353,76. The 95% interval of this prediction is [333,78, 373,64].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +65%. The 95% interval of this percentage is [+59%, +70%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,37) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   5,3              1066,6          
Prediction (s.d.)        5,1 (0,14)       1014,6 (28,27)  
95% CI                   [4,8, 5,3]       [961,7, 1069,5] 
                                                          
Absolute effect (s.d.)   0,26 (0,14)      51,93 (28,27)   
95% CI                   [-0,015, 0,52]   [-2,916, 104,84]
                                                          
Relative effect (s.d.)   5,1% (2,8%)      5,1% (2,8%)     
95% CI                   [-0,29%, 10%]    [-0,29%, 10%]   

Posterior tail-area probability p:   0,03399
Posterior prob. of a causal effect:  96,601%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 5,33. In the absence of an intervention, we would have expected an average response of 5,07. The 95% interval of this counterfactual prediction is [4,81, 5,35]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,26 with a 95% interval of [-0,015, 0,52]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,07K. Had the intervention not taken place, we would have expected a sum of 1,01K. The 95% interval of this prediction is [0,96K, 1,07K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +5%. The 95% interval of this percentage is [-0%, +10%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,034). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   5,3            3319,5          
Prediction (s.d.)        4,8 (0,09)     2980,4 (56,32)  
95% CI                   [4,6, 4,9]     [2867,9, 3088,5]
                                                        
Absolute effect (s.d.)   0,54 (0,09)    339,07 (56,32)  
95% CI                   [0,37, 0,72]   [231,01, 451,58]
                                                        
Relative effect (s.d.)   11% (1,9%)     11% (1,9%)      
95% CI                   [7,8%, 15%]    [7,8%, 15%]     

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89474%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 5,32. By contrast, in the absence of an intervention, we would have expected an average response of 4,78. The 95% interval of this counterfactual prediction is [4,60, 4,95]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,54 with a 95% interval of [0,37, 0,72]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,32K. By contrast, had the intervention not taken place, we would have expected a sum of 2,98K. The 95% interval of this prediction is [2,87K, 3,09K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +11%. The 95% interval of this percentage is [+8%, +15%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,54) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative    
Actual                   0,17             33,09         
Prediction (s.d.)        0,14 (0,0066)    27,91 (1,3278)
95% CI                   [0,13, 0,15]     [25,36, 30,63]
                                                        
Absolute effect (s.d.)   0,026 (0,0066)   5,177 (1,3278)
95% CI                   [0,012, 0,039]   [2,455, 7,729]
                                                        
Relative effect (s.d.)   19% (4,8%)       19% (4,8%)    
95% CI                   [8,8%, 28%]      [8,8%, 28%]   

Posterior tail-area probability p:   0,00204
Posterior prob. of a causal effect:  99,79633%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,17. By contrast, in the absence of an intervention, we would have expected an average response of 0,14. The 95% interval of this counterfactual prediction is [0,13, 0,15]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,026 with a 95% interval of [0,012, 0,039]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 33,09. By contrast, had the intervention not taken place, we would have expected a sum of 27,91. The 95% interval of this prediction is [25,36, 30,63].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +19%. The 95% interval of this percentage is [+9%, +28%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,026) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,17             105,07          
Prediction (s.d.)        0,13 (0,0033)    83,26 (2,0374)  
95% CI                   [0,13, 0,14]     [79,25, 87,13]  
                                                          
Absolute effect (s.d.)   0,035 (0,0033)   21,813 (2,0374) 
95% CI                   [0,029, 0,041]   [17,945, 25,820]
                                                          
Relative effect (s.d.)   26% (2,4%)       26% (2,4%)      
95% CI                   [22%, 31%]       [22%, 31%]      

Posterior tail-area probability p:   0,00104
Posterior prob. of a causal effect:  99,89648%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,17. By contrast, in the absence of an intervention, we would have expected an average response of 0,13. The 95% interval of this counterfactual prediction is [0,13, 0,14]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,035 with a 95% interval of [0,029, 0,041]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 105,07. By contrast, had the intervention not taken place, we would have expected a sum of 83,26. The 95% interval of this prediction is [79,25, 87,13].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +26%. The 95% interval of this percentage is [+22%, +31%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,035) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 513"
[1] "number of repositories <=-95% top_performer: 1     0,194931773879142 %"
[1] "number of repositories <0 good_performer: 32     6,23781676413255 %"
[1] "number of repositories =0 no_change_with_problems: 228     44,4444444444444 %"
[1] "number of repositories >0 worst_performer: 252     49,1228070175439 %"
[1] "sum problems added - problems fixed: 696,783233406679"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 75"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 2     2,66666666666667 %"
[1] "number of repositories =0 no_change_with_problems: 51     68 %"
[1] "number of repositories >0 worst_performer: 22     29,3333333333333 %"
[1] "sum problems added - problems fixed: 70,8397057299231"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 47"
[1] "number of repositories <=-95% top_performer: 1     2,12765957446809 %"
[1] "number of repositories <0 good_performer: 3     6,38297872340426 %"
[1] "number of repositories =0 no_change_with_problems: 22     46,8085106382979 %"
[1] "number of repositories >0 worst_performer: 21     44,6808510638298 %"
[1] "sum problems added - problems fixed: 31,2581525232246"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 5"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 3     60 %"
[1] "number of repositories >0 worst_performer: 2     40 %"
[1] "sum problems added - problems fixed: 0,900542005420053"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 137"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 1     0,72992700729927 %"
[1] "number of repositories =0 no_change_with_problems: 77     56,2043795620438 %"
[1] "number of repositories >0 worst_performer: 59     43,0656934306569 %"
[1] "sum problems added - problems fixed: 140,021297631691"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 165"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 16     9,6969696969697 %"
[1] "number of repositories =0 no_change_with_problems: 84     50,9090909090909 %"
[1] "number of repositories >0 worst_performer: 65     39,3939393939394 %"
[1] "sum problems added - problems fixed: 182,66671271435"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 362"
[1] "number of repositories <=-95% top_performer: 3     0,828729281767956 %"
[1] "number of repositories <0 good_performer: 20     5,52486187845304 %"
[1] "number of repositories =0 no_change_with_problems: 195     53,8674033149171 %"
[1] "number of repositories >0 worst_performer: 144     39,7790055248619 %"
[1] "sum problems added - problems fixed: 248,845294671771"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 538"
[1] "number of repos with problems in this 90 day timeframe: 32"
[1] "number of repositories <=-95% top_performer: 2     6,25 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 13     40,625 %"
[1] "number of repositories >0 worst_performer: 17     53,125 %"
[1] "sum problems added - problems fixed: 22,2515281302995"
[1] "number of repos with overall problems in this 700 day timeframe: 538"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 66"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 55"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 6"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 145"
[1] "number of repos with xss problems in this 700 day timeframe: 179"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 374"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 38"
