[1] "Log information"
[1] "folder: not_popular_stars"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   1,7               337,9           
Prediction (s.d.)        1,7 (0,013)       346,9 (2,645)   
95% CI                   [1,7, 1,8]        [341,8, 352,2]  
                                                           
Absolute effect (s.d.)   -0,045 (0,013)    -8,996 (2,645)  
95% CI                   [-0,072, -0,02]   [-14,367, -3,93]
                                                           
Relative effect (s.d.)   -2,6% (0,76%)     -2,6% (0,76%)   
95% CI                   [-4,1%, -1,1%]    [-4,1%, -1,1%]  

Posterior tail-area probability p:   0,00203
Posterior prob. of a causal effect:  99,79695%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,69. By contrast, in the absence of an intervention, we would have expected an average response of 1,73. The 95% interval of this counterfactual prediction is [1,71, 1,76]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,045 with a 95% interval of [-0,072, -0,020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 337,88. By contrast, had the intervention not taken place, we would have expected a sum of 346,87. The 95% interval of this prediction is [341,81, 352,24].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative        
Actual                   1,7                1045,6            
Prediction (s.d.)        1,7 (0,013)        1072,6 (8,185)    
95% CI                   [1,7, 1,7]         [1056,5, 1088,8]  
                                                              
Absolute effect (s.d.)   -0,043 (0,013)     -27,011 (8,185)   
95% CI                   [-0,069, -0,017]   [-43,140, -10,907]
                                                              
Relative effect (s.d.)   -2,5% (0,76%)      -2,5% (0,76%)     
95% CI                   [-4%, -1%]         [-4%, -1%]        

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,68. By contrast, in the absence of an intervention, we would have expected an average response of 1,72. The 95% interval of this counterfactual prediction is [1,69, 1,74]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,043 with a 95% interval of [-0,069, -0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,05K. By contrast, had the intervention not taken place, we would have expected a sum of 1,07K. The 95% interval of this prediction is [1,06K, 1,09K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,21                42,80            
Prediction (s.d.)        0,22 (0,0022)       44,14 (0,4404)   
95% CI                   [0,22, 0,22]        [43,28, 44,98]   
                                                              
Absolute effect (s.d.)   -0,0067 (0,0022)    -1,3463 (0,4404) 
95% CI                   [-0,011, -0,0024]   [-2,180, -0,4791]
                                                              
Relative effect (s.d.)   -3% (1%)            -3% (1%)         
95% CI                   [-4,9%, -1,1%]      [-4,9%, -1,1%]   

Posterior tail-area probability p:   0,00209
Posterior prob. of a causal effect:  99,79101%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,21. By contrast, in the absence of an intervention, we would have expected an average response of 0,22. The 95% interval of this counterfactual prediction is [0,22, 0,22]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0067 with a 95% interval of [-0,011, -0,0024]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 42,80. By contrast, had the intervention not taken place, we would have expected a sum of 44,14. The 95% interval of this prediction is [43,28, 44,98].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,21                 133,39            
Prediction (s.d.)        0,22 (0,0019)        135,56 (1,1987)   
95% CI                   [0,21, 0,22]         [133,20, 137,91]  
                                                                
Absolute effect (s.d.)   -0,0035 (0,0019)     -2,1739 (1,1987)  
95% CI                   [-0,0072, 0,00029]   [-4,5224, 0,18250]
                                                                
Relative effect (s.d.)   -1,6% (0,88%)        -1,6% (0,88%)     
95% CI                   [-3,3%, 0,13%]       [-3,3%, 0,13%]    

Posterior tail-area probability p:   0,03835
Posterior prob. of a causal effect:  96,165%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,21. In the absence of an intervention, we would have expected an average response of 0,22. The 95% interval of this counterfactual prediction is [0,21, 0,22]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0035 with a 95% interval of [-0,0072, 0,00029]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 133,39. Had the intervention not taken place, we would have expected a sum of 135,56. The 95% interval of this prediction is [133,20, 137,91].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-3%, +0%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,038). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,021               4,198            
Prediction (s.d.)        0,023 (0,00067)     4,654 (0,13465)  
95% CI                   [0,022, 0,025]      [4,403, 4,928]   
                                                              
Absolute effect (s.d.)   -0,0023 (0,00067)   -0,4555 (0,13465)
95% CI                   [-0,0036, -0,001]   [-0,7296, -0,205]
                                                              
Relative effect (s.d.)   -9,8% (2,9%)        -9,8% (2,9%)     
95% CI                   [-16%, -4,4%]       [-16%, -4,4%]    

Posterior tail-area probability p:   0,00206
Posterior prob. of a causal effect:  99,79381%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,021. By contrast, in the absence of an intervention, we would have expected an average response of 0,023. The 95% interval of this counterfactual prediction is [0,022, 0,025]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0023 with a 95% interval of [-0,0036, -0,0010]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 4,20. By contrast, had the intervention not taken place, we would have expected a sum of 4,65. The 95% interval of this prediction is [4,40, 4,93].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -10%. The 95% interval of this percentage is [-16%, -4%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,021                13,207            
Prediction (s.d.)        0,024 (0,00047)      14,724 (0,29413)  
95% CI                   [0,023, 0,025]       [14,141, 15,302]  
                                                                
Absolute effect (s.d.)   -0,0024 (0,00047)    -1,5166 (0,29413) 
95% CI                   [-0,0034, -0,0015]   [-2,0946, -0,9338]
                                                                
Relative effect (s.d.)   -10% (2%)            -10% (2%)         
95% CI                   [-14%, -6,3%]        [-14%, -6,3%]     

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,021. By contrast, in the absence of an intervention, we would have expected an average response of 0,024. The 95% interval of this counterfactual prediction is [0,023, 0,025]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0024 with a 95% interval of [-0,0034, -0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 13,21. By contrast, had the intervention not taken place, we would have expected a sum of 14,72. The 95% interval of this prediction is [14,14, 15,30].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -10%. The 95% interval of this percentage is [-14%, -6%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0025               0,4983            
Prediction (s.d.)        0,0048 (0,00014)     0,9675 (0,02882)  
95% CI                   [0,0046, 0,0051]     [0,9130, 1,0287]  
                                                                
Absolute effect (s.d.)   -0,0023 (0,00014)    -0,4692 (0,02882) 
95% CI                   [-0,0027, -0,0021]   [-0,5304, -0,4147]
                                                                
Relative effect (s.d.)   -48% (3%)            -48% (3%)         
95% CI                   [-55%, -43%]         [-55%, -43%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89451%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0025. By contrast, in the absence of an intervention, we would have expected an average response of 0,0048. The 95% interval of this counterfactual prediction is [0,0046, 0,0051]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0023 with a 95% interval of [-0,0027, -0,0021]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,50. By contrast, had the intervention not taken place, we would have expected a sum of 0,97. The 95% interval of this prediction is [0,91, 1,03].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -48%. The 95% interval of this percentage is [-55%, -43%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,0025              1,5841           
Prediction (s.d.)        0,0048 (0,00013)    3,0146 (0,07836) 
95% CI                   [0,0046, 0,0051]    [2,8600, 3,1673] 
                                                              
Absolute effect (s.d.)   -0,0023 (0,00013)   -1,4305 (0,07836)
95% CI                   [-0,0025, -0,002]   [-1,5832, -1,276]
                                                              
Relative effect (s.d.)   -47% (2,6%)         -47% (2,6%)      
95% CI                   [-53%, -42%]        [-53%, -42%]     

Posterior tail-area probability p:   0,00107
Posterior prob. of a causal effect:  99,89259%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0025. By contrast, in the absence of an intervention, we would have expected an average response of 0,0048. The 95% interval of this counterfactual prediction is [0,0046, 0,0051]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0023 with a 95% interval of [-0,0025, -0,0020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,58. By contrast, had the intervention not taken place, we would have expected a sum of 3,01. The 95% interval of this prediction is [2,86, 3,17].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -47%. The 95% interval of this percentage is [-53%, -42%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,53               105,67          
Prediction (s.d.)        0,55 (0,0046)      109,72 (0,9156) 
95% CI                   [0,54, 0,56]       [107,95, 111,48]
                                                            
Absolute effect (s.d.)   -0,02 (0,0046)     -4,05 (0,9156)  
95% CI                   [-0,029, -0,011]   [-5,810, -2,273]
                                                            
Relative effect (s.d.)   -3,7% (0,83%)      -3,7% (0,83%)   
95% CI                   [-5,3%, -2,1%]     [-5,3%, -2,1%]  

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89785%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,53. By contrast, in the absence of an intervention, we would have expected an average response of 0,55. The 95% interval of this counterfactual prediction is [0,54, 0,56]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,020 with a 95% interval of [-0,029, -0,011]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 105,67. By contrast, had the intervention not taken place, we would have expected a sum of 109,72. The 95% interval of this prediction is [107,95, 111,48].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,52               325,96           
Prediction (s.d.)        0,55 (0,0049)      340,12 (3,0483)  
95% CI                   [0,54, 0,55]       [334,04, 346,02] 
                                                             
Absolute effect (s.d.)   -0,023 (0,0049)    -14,159 (3,0483) 
95% CI                   [-0,032, -0,013]   [-20,056, -8,075]
                                                             
Relative effect (s.d.)   -4,2% (0,9%)       -4,2% (0,9%)     
95% CI                   [-5,9%, -2,4%]     [-5,9%, -2,4%]   

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89691%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,52. By contrast, in the absence of an intervention, we would have expected an average response of 0,55. The 95% interval of this counterfactual prediction is [0,54, 0,55]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,023 with a 95% interval of [-0,032, -0,013]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 325,96. By contrast, had the intervention not taken place, we would have expected a sum of 340,12. The 95% interval of this prediction is [334,04, 346,02].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative    
Actual                   0,12             23,78         
Prediction (s.d.)        0,1 (0,0017)     20,6 (0,3397) 
95% CI                   [0,1, 0,11]      [20,0, 21,29] 
                                                        
Absolute effect (s.d.)   0,016 (0,0017)   3,167 (0,3397)
95% CI                   [0,012, 0,019]   [2,491, 3,822]
                                                        
Relative effect (s.d.)   15% (1,6%)       15% (1,6%)    
95% CI                   [12%, 19%]       [12%, 19%]    

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89507%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,10. The 95% interval of this counterfactual prediction is [0,100, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,016 with a 95% interval of [0,012, 0,019]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 23,78. By contrast, had the intervention not taken place, we would have expected a sum of 20,62. The 95% interval of this prediction is [19,96, 21,29].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +15%. The 95% interval of this percentage is [+12%, +19%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,016) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative     
Actual                   0,12             74,10          
Prediction (s.d.)        0,1 (0,0012)     63,3 (0,7522)  
95% CI                   [0,099, 0,1]     [61,815, 64,7] 
                                                         
Absolute effect (s.d.)   0,017 (0,0012)   10,817 (0,7522)
95% CI                   [0,015, 0,02]    [9,355, 12,28] 
                                                         
Relative effect (s.d.)   17% (1,2%)       17% (1,2%)     
95% CI                   [15%, 19%]       [15%, 19%]     

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89868%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,10. The 95% interval of this counterfactual prediction is [0,099, 0,10]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,017 with a 95% interval of [0,015, 0,020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 74,10. By contrast, had the intervention not taken place, we would have expected a sum of 63,28. The 95% interval of this prediction is [61,81, 64,74].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +17%. The 95% interval of this percentage is [+15%, +19%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,017) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,79               158,54          
Prediction (s.d.)        0,82 (0,0085)      164,70 (1,6990) 
95% CI                   [0,81, 0,84]       [161,55, 168,01]
                                                            
Absolute effect (s.d.)   -0,031 (0,0085)    -6,158 (1,6990) 
95% CI                   [-0,047, -0,015]   [-9,476, -3,015]
                                                            
Relative effect (s.d.)   -3,7% (1%)         -3,7% (1%)      
95% CI                   [-5,8%, -1,8%]     [-5,8%, -1,8%]  

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89659%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,79. By contrast, in the absence of an intervention, we would have expected an average response of 0,82. The 95% interval of this counterfactual prediction is [0,81, 0,84]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,031 with a 95% interval of [-0,047, -0,015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 158,54. By contrast, had the intervention not taken place, we would have expected a sum of 164,70. The 95% interval of this prediction is [161,55, 168,01].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative        
Actual                   0,78               489,81            
Prediction (s.d.)        0,82 (0,0069)      508,96 (4,3063)   
95% CI                   [0,8, 0,83]        [500,4, 517,36]   
                                                              
Absolute effect (s.d.)   -0,031 (0,0069)    -19,150 (4,3063)  
95% CI                   [-0,044, -0,017]   [-27,541, -10,630]
                                                              
Relative effect (s.d.)   -3,8% (0,85%)      -3,8% (0,85%)     
95% CI                   [-5,4%, -2,1%]     [-5,4%, -2,1%]    

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,78. By contrast, in the absence of an intervention, we would have expected an average response of 0,82. The 95% interval of this counterfactual prediction is [0,80, 0,83]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,031 with a 95% interval of [-0,044, -0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 489,81. By contrast, had the intervention not taken place, we would have expected a sum of 508,96. The 95% interval of this prediction is [500,44, 517,36].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,012               2,390            
Prediction (s.d.)        0,011 (0,00079)     2,266 (0,15731)  
95% CI                   [0,0099, 0,013]     [1,9716, 2,590]  
                                                              
Absolute effect (s.d.)   0,00062 (0,00079)   0,12339 (0,15731)
95% CI                   [-0,001, 0,0021]    [-0,200, 0,4182] 
                                                              
Relative effect (s.d.)   5,4% (6,9%)         5,4% (6,9%)      
95% CI                   [-8,8%, 18%]        [-8,8%, 18%]     

Posterior tail-area probability p:   0,20412
Posterior prob. of a causal effect:  80%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,012. In the absence of an intervention, we would have expected an average response of 0,011. The 95% interval of this counterfactual prediction is [0,0099, 0,013]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00062 with a 95% interval of [-0,00100, 0,0021]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 2,39. Had the intervention not taken place, we would have expected a sum of 2,27. The 95% interval of this prediction is [1,97, 2,59].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +5%. The 95% interval of this percentage is [-9%, +18%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,204. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,012                7,581             
Prediction (s.d.)        0,012 (0,00043)      7,182 (0,26962)   
95% CI                   [0,011, 0,012]       [6,652, 7,693]    
                                                                
Absolute effect (s.d.)   0,00064 (0,00043)    0,39912 (0,26962) 
95% CI                   [-0,00018, 0,0015]   [-0,11189, 0,9294]
                                                                
Relative effect (s.d.)   5,6% (3,8%)          5,6% (3,8%)       
95% CI                   [-1,6%, 13%]         [-1,6%, 13%]      

Posterior tail-area probability p:   0,07337
Posterior prob. of a causal effect:  93%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,012. In the absence of an intervention, we would have expected an average response of 0,012. The 95% interval of this counterfactual prediction is [0,011, 0,012]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00064 with a 95% interval of [-0,00018, 0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 7,58. Had the intervention not taken place, we would have expected a sum of 7,18. The 95% interval of this prediction is [6,65, 7,69].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +6%. The 95% interval of this percentage is [-2%, +13%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,073. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 1302"
[1] "number of repositories <=-95% top_performer: 78     5,99078341013825 %"
[1] "number of repositories <0 good_performer: 115     8,83256528417819 %"
[1] "number of repositories =0 no_change_with_problems: 889     68,2795698924731 %"
[1] "number of repositories >0 worst_performer: 220     16,8970814132104 %"
[1] "sum problems added - problems fixed: -366,212897640955"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 192"
[1] "number of repositories <=-95% top_performer: 21     10,9375 %"
[1] "number of repositories <0 good_performer: 10     5,20833333333333 %"
[1] "number of repositories =0 no_change_with_problems: 145     75,5208333333333 %"
[1] "number of repositories >0 worst_performer: 16     8,33333333333333 %"
[1] "sum problems added - problems fixed: -26,291244784897"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 94"
[1] "number of repositories <=-95% top_performer: 12     12,7659574468085 %"
[1] "number of repositories <0 good_performer: 10     10,6382978723404 %"
[1] "number of repositories =0 no_change_with_problems: 54     57,4468085106383 %"
[1] "number of repositories >0 worst_performer: 18     19,1489361702128 %"
[1] "sum problems added - problems fixed: -17,2278935991118"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 5"
[1] "number of repositories <=-95% top_performer: 1     20 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 2     40 %"
[1] "number of repositories >0 worst_performer: 2     40 %"
[1] "sum problems added - problems fixed: -19,0994579945799"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 465"
[1] "number of repositories <=-95% top_performer: 23     4,94623655913978 %"
[1] "number of repositories <0 good_performer: 23     4,94623655913978 %"
[1] "number of repositories =0 no_change_with_problems: 369     79,3548387096774 %"
[1] "number of repositories >0 worst_performer: 50     10,752688172043 %"
[1] "sum problems added - problems fixed: -192,436097322642"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 319"
[1] "number of repositories <=-95% top_performer: 17     5,32915360501567 %"
[1] "number of repositories <0 good_performer: 31     9,71786833855799 %"
[1] "number of repositories =0 no_change_with_problems: 206     64,576802507837 %"
[1] "number of repositories >0 worst_performer: 65     20,3761755485893 %"
[1] "sum problems added - problems fixed: 124,273901943022"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 922"
[1] "number of repositories <=-95% top_performer: 57     6,1822125813449 %"
[1] "number of repositories <0 good_performer: 73     7,9175704989154 %"
[1] "number of repositories =0 no_change_with_problems: 671     72,7765726681128 %"
[1] "number of repositories >0 worst_performer: 121     13,1236442516269 %"
[1] "sum problems added - problems fixed: -244,259189568601"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 7422"
[1] "number of repos with problems in this 90 day timeframe: 47"
[1] "number of repositories <=-95% top_performer: 7     14,8936170212766 %"
[1] "number of repositories <0 good_performer: 2     4,25531914893617 %"
[1] "number of repositories =0 no_change_with_problems: 22     46,8085106382979 %"
[1] "number of repositories >0 worst_performer: 16     34,0425531914894 %"
[1] "sum problems added - problems fixed: 8,82708368585507"
[1] "number of repos with overall problems in this 700 day timeframe: 929"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 138"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 86"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 6"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 328"
[1] "number of repos with xss problems in this 700 day timeframe: 274"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 634"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 63"
