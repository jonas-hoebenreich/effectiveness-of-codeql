[1] "Log information"
[1] "folder: more_than_4_ontributors"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   2,6              514,6           
Prediction (s.d.)        2,6 (0,036)      518,2 (7,148)   
95% CI                   [2,5, 2,7]       [504,3, 532,6]  
                                                          
Absolute effect (s.d.)   -0,018 (0,036)   -3,626 (7,148)  
95% CI                   [-0,09, 0,051]   [-18,04, 10,225]
                                                          
Relative effect (s.d.)   -0,7% (1,4%)     -0,7% (1,4%)    
95% CI                   [-3,5%, 2%]      [-3,5%, 2%]     

Posterior tail-area probability p:   0,31141
Posterior prob. of a causal effect:  69%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 2,57. In the absence of an intervention, we would have expected an average response of 2,59. The 95% interval of this counterfactual prediction is [2,52, 2,66]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,018 with a 95% interval of [-0,090, 0,051]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 514,57. Had the intervention not taken place, we would have expected a sum of 518,20. The 95% interval of this prediction is [504,35, 532,61].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-3%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,311. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   2,6              1614,0          
Prediction (s.d.)        2,6 (0,034)      1624,6 (21,236) 
95% CI                   [2,5, 2,7]       [1582,5, 1665,9]
                                                          
Absolute effect (s.d.)   -0,017 (0,034)   -10,594 (21,236)
95% CI                   [-0,083, 0,05]   [-51,938, 31,49]
                                                          
Relative effect (s.d.)   -0,65% (1,3%)    -0,65% (1,3%)   
95% CI                   [-3,2%, 1,9%]    [-3,2%, 1,9%]   

Posterior tail-area probability p:   0,31584
Posterior prob. of a causal effect:  68%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 2,59. In the absence of an intervention, we would have expected an average response of 2,60. The 95% interval of this counterfactual prediction is [2,54, 2,67]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,017 with a 95% interval of [-0,083, 0,050]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,61K. Had the intervention not taken place, we would have expected a sum of 1,62K. The 95% interval of this prediction is [1,58K, 1,67K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-3%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,316. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,41              81,03          
Prediction (s.d.)        0,4 (0,0078)      79,9 (1,5553)  
95% CI                   [0,38, 0,42]      [76,96, 83,18] 
                                                          
Absolute effect (s.d.)   0,0054 (0,0078)   1,0892 (1,5553)
95% CI                   [-0,011, 0,02]    [-2,154, 4,07] 
                                                          
Relative effect (s.d.)   1,4% (1,9%)       1,4% (1,9%)    
95% CI                   [-2,7%, 5,1%]     [-2,7%, 5,1%]  

Posterior tail-area probability p:   0,2377
Posterior prob. of a causal effect:  76%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,41. In the absence of an intervention, we would have expected an average response of 0,40. The 95% interval of this counterfactual prediction is [0,38, 0,42]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0054 with a 95% interval of [-0,011, 0,020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 81,03. Had the intervention not taken place, we would have expected a sum of 79,94. The 95% interval of this prediction is [76,96, 83,18].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +1%. The 95% interval of this percentage is [-3%, +5%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,238. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,41              258,70          
Prediction (s.d.)        0,39 (0,0092)     243,44 (5,7352) 
95% CI                   [0,37, 0,41]      [232,25, 254,39]
                                                           
Absolute effect (s.d.)   0,024 (0,0092)    15,267 (5,7352) 
95% CI                   [0,0069, 0,042]   [4,3164, 26,453]
                                                           
Relative effect (s.d.)   6,3% (2,4%)       6,3% (2,4%)     
95% CI                   [1,8%, 11%]       [1,8%, 11%]     

Posterior tail-area probability p:   0,00302
Posterior prob. of a causal effect:  99,69819%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,41. By contrast, in the absence of an intervention, we would have expected an average response of 0,39. The 95% interval of this counterfactual prediction is [0,37, 0,41]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,024 with a 95% interval of [0,0069, 0,042]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 258,70. By contrast, had the intervention not taken place, we would have expected a sum of 243,44. The 95% interval of this prediction is [232,25, 254,39].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +6%. The 95% interval of this percentage is [+2%, +11%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,024) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,003). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,021                4,158             
Prediction (s.d.)        0,018 (0,0019)       3,562 (0,3887)    
95% CI                   [0,014, 0,022]       [2,827, 4,344]    
                                                                
Absolute effect (s.d.)   0,003 (0,0019)       0,595 (0,3887)    
95% CI                   [-0,00093, 0,0067]   [-0,18635, 1,3307]
                                                                
Relative effect (s.d.)   17% (11%)            17% (11%)         
95% CI                   [-5,2%, 37%]         [-5,2%, 37%]      

Posterior tail-area probability p:   0,07559
Posterior prob. of a causal effect:  92%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,021. In the absence of an intervention, we would have expected an average response of 0,018. The 95% interval of this counterfactual prediction is [0,014, 0,022]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0030 with a 95% interval of [-0,00093, 0,0067]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 4,16. Had the intervention not taken place, we would have expected a sum of 3,56. The 95% interval of this prediction is [2,83, 4,34].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +17%. The 95% interval of this percentage is [-5%, +37%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,076. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,024              15,216          
Prediction (s.d.)        0,019 (0,0011)     11,573 (0,7115) 
95% CI                   [0,016, 0,021]     [10,173, 12,943]
                                                            
Absolute effect (s.d.)   0,0058 (0,0011)    3,6427 (0,7115) 
95% CI                   [0,0036, 0,0081]   [2,2725, 5,0432]
                                                            
Relative effect (s.d.)   31% (6,1%)         31% (6,1%)      
95% CI                   [20%, 44%]         [20%, 44%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89879%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,024. By contrast, in the absence of an intervention, we would have expected an average response of 0,019. The 95% interval of this counterfactual prediction is [0,016, 0,021]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0058 with a 95% interval of [0,0036, 0,0081]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 15,22. By contrast, had the intervention not taken place, we would have expected a sum of 11,57. The 95% interval of this prediction is [10,17, 12,94].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +31%. The 95% interval of this percentage is [+20%, +44%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0058) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,0012                0,2465             
Prediction (s.d.)        3e-04 (0,00034)       6e-02 (0,06770)    
95% CI                   [-0,00037, 0,00099]   [-0,07329, 0,19748]
                                                                  
Absolute effect (s.d.)   0,00093 (0,00034)     0,18620 (0,06770)  
95% CI                   [0,00025, 0,0016]     [0,04907, 0,3198]  
                                                                  
Relative effect (s.d.)   309% (112%)           309% (112%)        
95% CI                   [81%, 530%]           [81%, 530%]        

Posterior tail-area probability p:   0,00409
Posterior prob. of a causal effect:  99,591%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0012. By contrast, in the absence of an intervention, we would have expected an average response of 0,00030. The 95% interval of this counterfactual prediction is [-0,00037, 0,00099]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00093 with a 95% interval of [0,00025, 0,0016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,25. By contrast, had the intervention not taken place, we would have expected a sum of 0,060. The 95% interval of this prediction is [-0,073, 0,20].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +309%. The 95% interval of this percentage is [+81%, +530%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,00093) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,004). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0016               0,9950            
Prediction (s.d.)        0,00042 (0,00018)    0,26341 (0,10983) 
95% CI                   [0,00007, 0,00077]   [0,04371, 0,48048]
                                                                
Absolute effect (s.d.)   0,0012 (0,00018)     0,7316 (0,10983)  
95% CI                   [0,00082, 0,0015]    [0,51453, 0,9513] 
                                                                
Relative effect (s.d.)   278% (42%)           278% (42%)        
95% CI                   [195%, 361%]         [195%, 361%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89879%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0016. By contrast, in the absence of an intervention, we would have expected an average response of 0,00042. The 95% interval of this counterfactual prediction is [0,000070, 0,00077]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0012 with a 95% interval of [0,00082, 0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,00. By contrast, had the intervention not taken place, we would have expected a sum of 0,26. The 95% interval of this prediction is [0,044, 0,48].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +278%. The 95% interval of this percentage is [+195%, +361%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0012) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,75              150,57         
Prediction (s.d.)        0,77 (0,015)      153,04 (2,989) 
95% CI                   [0,74, 0,8]       [147,25, 159,2]
                                                          
Absolute effect (s.d.)   -0,012 (0,015)    -2,469 (2,989) 
95% CI                   [-0,043, 0,017]   [-8,615, 3,318]
                                                          
Relative effect (s.d.)   -1,6% (2%)        -1,6% (2%)     
95% CI                   [-5,6%, 2,2%]     [-5,6%, 2,2%]  

Posterior tail-area probability p:   0,20021
Posterior prob. of a causal effect:  80%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,75. In the absence of an intervention, we would have expected an average response of 0,77. The 95% interval of this counterfactual prediction is [0,74, 0,80]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,012 with a 95% interval of [-0,043, 0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 150,57. Had the intervention not taken place, we would have expected a sum of 153,04. The 95% interval of this prediction is [147,25, 159,19].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-6%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,2. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative        
Actual                   0,75                468,44            
Prediction (s.d.)        0,78 (0,013)        483,77 (7,834)    
95% CI                   [0,75, 0,8]         [468,18, 499,0]   
                                                               
Absolute effect (s.d.)   -0,025 (0,013)      -15,331 (7,834)   
95% CI                   [-0,049, 0,00042]   [-30,553, 0,26047]
                                                               
Relative effect (s.d.)   -3,2% (1,6%)        -3,2% (1,6%)      
95% CI                   [-6,3%, 0,054%]     [-6,3%, 0,054%]   

Posterior tail-area probability p:   0,03083
Posterior prob. of a causal effect:  96,917%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,75. In the absence of an intervention, we would have expected an average response of 0,78. The 95% interval of this counterfactual prediction is [0,75, 0,80]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,025 with a 95% interval of [-0,049, 0,00042]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 468,44. Had the intervention not taken place, we would have expected a sum of 483,77. The 95% interval of this prediction is [468,18, 498,99].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-6%, +0%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,031). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,14               27,74           
Prediction (s.d.)        0,15 (0,0078)      29,10 (1,5584)  
95% CI                   [0,13, 0,16]       [26,21, 32,36]  
                                                            
Absolute effect (s.d.)   -0,0068 (0,0078)   -1,3617 (1,5584)
95% CI                   [-0,023, 0,0076]   [-4,618, 1,5264]
                                                            
Relative effect (s.d.)   -4,7% (5,4%)       -4,7% (5,4%)    
95% CI                   [-16%, 5,2%]       [-16%, 5,2%]    

Posterior tail-area probability p:   0,18939
Posterior prob. of a causal effect:  81%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,14. In the absence of an intervention, we would have expected an average response of 0,15. The 95% interval of this counterfactual prediction is [0,13, 0,16]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0068 with a 95% interval of [-0,023, 0,0076]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 27,74. Had the intervention not taken place, we would have expected a sum of 29,10. The 95% interval of this prediction is [26,21, 32,36].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -5%. The 95% interval of this percentage is [-16%, +5%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,189. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative        
Actual                   0,14                84,69             
Prediction (s.d.)        0,15 (0,0056)       93,80 (3,4772)    
95% CI                   [0,14, 0,16]        [86,97, 100,41]   
                                                               
Absolute effect (s.d.)   -0,015 (0,0056)     -9,113 (3,4772)   
95% CI                   [-0,025, -0,0037]   [-15,715, -2,2798]
                                                               
Relative effect (s.d.)   -9,7% (3,7%)        -9,7% (3,7%)      
95% CI                   [-17%, -2,4%]       [-17%, -2,4%]     

Posterior tail-area probability p:   0,0104
Posterior prob. of a causal effect:  98,96%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,14. By contrast, in the absence of an intervention, we would have expected an average response of 0,15. The 95% interval of this counterfactual prediction is [0,14, 0,16]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,015 with a 95% interval of [-0,025, -0,0037]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 84,69. By contrast, had the intervention not taken place, we would have expected a sum of 93,80. The 95% interval of this prediction is [86,97, 100,41].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -10%. The 95% interval of this percentage is [-17%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,01). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,2                249,1            
Prediction (s.d.)        1,3 (0,021)        256,3 (4,162)    
95% CI                   [1,2, 1,3]         [248,1, 264,6]   
                                                             
Absolute effect (s.d.)   -0,036 (0,021)     -7,209 (4,162)   
95% CI                   [-0,078, 0,0051]   [-15,511, 1,0269]
                                                             
Relative effect (s.d.)   -2,8% (1,6%)       -2,8% (1,6%)     
95% CI                   [-6,1%, 0,4%]      [-6,1%, 0,4%]    

Posterior tail-area probability p:   0,04225
Posterior prob. of a causal effect:  95,775%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,25. In the absence of an intervention, we would have expected an average response of 1,28. The 95% interval of this counterfactual prediction is [1,24, 1,32]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,036 with a 95% interval of [-0,078, 0,0051]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 249,13. Had the intervention not taken place, we would have expected a sum of 256,33. The 95% interval of this prediction is [248,10, 264,64].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-6%, +0%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,042). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   1,2               779,6            
Prediction (s.d.)        1,3 (0,019)       785,7 (11,760)   
95% CI                   [1,2, 1,3]        [762,2, 808,8]   
                                                            
Absolute effect (s.d.)   -0,0098 (0,019)   -6,0973 (11,760) 
95% CI                   [-0,047, 0,028]   [-29,119, 17,401]
                                                            
Relative effect (s.d.)   -0,78% (1,5%)     -0,78% (1,5%)    
95% CI                   [-3,7%, 2,2%]     [-3,7%, 2,2%]    

Posterior tail-area probability p:   0,30644
Posterior prob. of a causal effect:  69%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,25. In the absence of an intervention, we would have expected an average response of 1,26. The 95% interval of this counterfactual prediction is [1,22, 1,30]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0098 with a 95% interval of [-0,047, 0,028]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 779,65. Had the intervention not taken place, we would have expected a sum of 785,74. The 95% interval of this prediction is [762,25, 808,77].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-4%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,306. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,0085              1,7071           
Prediction (s.d.)        0,0073 (0,0027)     1,4570 (0,5495)  
95% CI                   [0,0021, 0,013]     [0,4205, 2,529]  
                                                              
Absolute effect (s.d.)   0,0013 (0,0027)     0,2501 (0,5495)  
95% CI                   [-0,0041, 0,0064]   [-0,8218, 1,2866]
                                                              
Relative effect (s.d.)   17% (38%)           17% (38%)        
95% CI                   [-56%, 88%]         [-56%, 88%]      

Posterior tail-area probability p:   0,30943
Posterior prob. of a causal effect:  69%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0085. In the absence of an intervention, we would have expected an average response of 0,0073. The 95% interval of this counterfactual prediction is [0,0021, 0,013]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0013 with a 95% interval of [-0,0041, 0,0064]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,71. Had the intervention not taken place, we would have expected a sum of 1,46. The 95% interval of this prediction is [0,42, 2,53].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +17%. The 95% interval of this percentage is [-56%, +88%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,309. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,01                 6,31              
Prediction (s.d.)        0,0084 (0,0014)      5,2241 (0,8668)   
95% CI                   [0,0056, 0,011]      [3,4959, 6,915]   
                                                                
Absolute effect (s.d.)   0,0017 (0,0014)      1,0819 (0,8668)   
95% CI                   [-0,00098, 0,0045]   [-0,60947, 2,8101]
                                                                
Relative effect (s.d.)   21% (17%)            21% (17%)         
95% CI                   [-12%, 54%]          [-12%, 54%]       

Posterior tail-area probability p:   0,11457
Posterior prob. of a causal effect:  89%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,010. In the absence of an intervention, we would have expected an average response of 0,0084. The 95% interval of this counterfactual prediction is [0,0056, 0,011]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0017 with a 95% interval of [-0,00098, 0,0045]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 6,31. Had the intervention not taken place, we would have expected a sum of 5,22. The 95% interval of this prediction is [3,50, 6,92].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +21%. The 95% interval of this percentage is [-12%, +54%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,115. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 511"
[1] "number of repositories <=-95% top_performer: 31     6,0665362035225 %"
[1] "number of repositories <0 good_performer: 65     12,720156555773 %"
[1] "number of repositories =0 no_change_with_problems: 340     66,5362035225049 %"
[1] "number of repositories >0 worst_performer: 75     14,6771037181996 %"
[1] "sum problems added - problems fixed: -141,083845906766"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 95"
[1] "number of repositories <=-95% top_performer: 8     8,42105263157895 %"
[1] "number of repositories <0 good_performer: 6     6,31578947368421 %"
[1] "number of repositories =0 no_change_with_problems: 70     73,6842105263158 %"
[1] "number of repositories >0 worst_performer: 11     11,5789473684211 %"
[1] "sum problems added - problems fixed: 7,62128704798875"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 34"
[1] "number of repositories <=-95% top_performer: 5     14,7058823529412 %"
[1] "number of repositories <0 good_performer: 2     5,88235294117647 %"
[1] "number of repositories =0 no_change_with_problems: 20     58,8235294117647 %"
[1] "number of repositories >0 worst_performer: 7     20,5882352941176 %"
[1] "sum problems added - problems fixed: 1,36080586080586"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 1     100 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: 0"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 187"
[1] "number of repositories <=-95% top_performer: 11     5,88235294117647 %"
[1] "number of repositories <0 good_performer: 11     5,88235294117647 %"
[1] "number of repositories =0 no_change_with_problems: 148     79,144385026738 %"
[1] "number of repositories >0 worst_performer: 17     9,09090909090909 %"
[1] "sum problems added - problems fixed: -71,8985085283924"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 156"
[1] "number of repositories <=-95% top_performer: 12     7,69230769230769 %"
[1] "number of repositories <0 good_performer: 19     12,1794871794872 %"
[1] "number of repositories =0 no_change_with_problems: 110     70,5128205128205 %"
[1] "number of repositories >0 worst_performer: 15     9,61538461538462 %"
[1] "sum problems added - problems fixed: -18,4073245116981"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 396"
[1] "number of repositories <=-95% top_performer: 23     5,80808080808081 %"
[1] "number of repositories <0 good_performer: 44     11,1111111111111 %"
[1] "number of repositories =0 no_change_with_problems: 284     71,7171717171717 %"
[1] "number of repositories >0 worst_performer: 45     11,3636363636364 %"
[1] "sum problems added - problems fixed: -61,8245502199145"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 2270"
[1] "number of repos with problems in this 90 day timeframe: 17"
[1] "number of repositories <=-95% top_performer: 3     17,6470588235294 %"
[1] "number of repositories <0 good_performer: 2     11,7647058823529 %"
[1] "number of repositories =0 no_change_with_problems: 7     41,1764705882353 %"
[1] "number of repositories >0 worst_performer: 5     29,4117647058824 %"
[1] "sum problems added - problems fixed: 2,06444444444444"
[1] "number of repos with overall problems in this 700 day timeframe: 590"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 136"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 54"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 6"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 257"
[1] "number of repos with xss problems in this 700 day timeframe: 213"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 444"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 40"
