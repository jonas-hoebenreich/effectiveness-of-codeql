[1] "Log information"
[1] "folder: weekly"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   1,8               365,5           
Prediction (s.d.)        1,9 (0,016)       375,4 (3,163)   
95% CI                   [1,8, 1,9]        [369,5, 381,8]  
                                                           
Absolute effect (s.d.)   -0,049 (0,016)    -9,860 (3,163)  
95% CI                   [-0,081, -0,02]   [-16,285, -3,98]
                                                           
Relative effect (s.d.)   -2,6% (0,84%)     -2,6% (0,84%)   
95% CI                   [-4,3%, -1,1%]    [-4,3%, -1,1%]  

Posterior tail-area probability p:   0,00203
Posterior prob. of a causal effect:  99,79695%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,83. By contrast, in the absence of an intervention, we would have expected an average response of 1,88. The 95% interval of this counterfactual prediction is [1,85, 1,91]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,049 with a 95% interval of [-0,081, -0,020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 365,53. By contrast, had the intervention not taken place, we would have expected a sum of 375,39. The 95% interval of this prediction is [369,51, 381,81].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,8                1135,6           
Prediction (s.d.)        1,9 (0,014)        1160,4 (9,012)   
95% CI                   [1,8, 1,9]         [1142,4, 1177,8] 
                                                             
Absolute effect (s.d.)   -0,04 (0,014)      -24,74 (9,012)   
95% CI                   [-0,068, -0,011]   [-42,200, -6,740]
                                                             
Relative effect (s.d.)   -2,1% (0,78%)      -2,1% (0,78%)    
95% CI                   [-3,6%, -0,58%]    [-3,6%, -0,58%]  

Posterior tail-area probability p:   0,00715
Posterior prob. of a causal effect:  99,28498%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,82. By contrast, in the absence of an intervention, we would have expected an average response of 1,86. The 95% interval of this counterfactual prediction is [1,83, 1,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,040 with a 95% interval of [-0,068, -0,011]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,14K. By contrast, had the intervention not taken place, we would have expected a sum of 1,16K. The 95% interval of this prediction is [1,14K, 1,18K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,007). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,26                51,61            
Prediction (s.d.)        0,26 (0,003)        52,61 (0,592)    
95% CI                   [0,26, 0,27]        [51,45, 53,77]   
                                                              
Absolute effect (s.d.)   -0,005 (0,003)      -0,998 (0,592)   
95% CI                   [-0,011, 0,00082]   [-2,160, 0,16448]
                                                              
Relative effect (s.d.)   -1,9% (1,1%)        -1,9% (1,1%)     
95% CI                   [-4,1%, 0,31%]      [-4,1%, 0,31%]   

Posterior tail-area probability p:   0,04379
Posterior prob. of a causal effect:  95,621%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,26. In the absence of an intervention, we would have expected an average response of 0,26. The 95% interval of this counterfactual prediction is [0,26, 0,27]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0050 with a 95% interval of [-0,011, 0,00082]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 51,61. Had the intervention not taken place, we would have expected a sum of 52,61. The 95% interval of this prediction is [51,45, 53,77].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, +0%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,044). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,26                162,34           
Prediction (s.d.)        0,26 (0,003)        161,42 (1,849)   
95% CI                   [0,25, 0,26]        [157,81, 165,00] 
                                                              
Absolute effect (s.d.)   0,0015 (0,003)      0,9211 (1,849)   
95% CI                   [-0,0043, 0,0073]   [-2,6579, 4,5281]
                                                              
Relative effect (s.d.)   0,57% (1,1%)        0,57% (1,1%)     
95% CI                   [-1,6%, 2,8%]       [-1,6%, 2,8%]    

Posterior tail-area probability p:   0,29429
Posterior prob. of a causal effect:  71%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,26. In the absence of an intervention, we would have expected an average response of 0,26. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0015 with a 95% interval of [-0,0043, 0,0073]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 162,34. Had the intervention not taken place, we would have expected a sum of 161,42. The 95% interval of this prediction is [157,81, 165,00].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +1%. The 95% interval of this percentage is [-2%, +3%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,294. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,02                  3,93               
Prediction (s.d.)        0,021 (0,00059)       4,267 (0,11818)    
95% CI                   [0,02, 0,023]         [4,04, 4,506]      
                                                                  
Absolute effect (s.d.)   -0,0017 (0,00059)     -0,3399 (0,11818)  
95% CI                   [-0,0029, -0,00058]   [-0,5788, -0,11658]
                                                                  
Relative effect (s.d.)   -8% (2,8%)            -8% (2,8%)         
95% CI                   [-14%, -2,7%]         [-14%, -2,7%]      

Posterior tail-area probability p:   0,00203
Posterior prob. of a causal effect:  99,79695%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,021. The 95% interval of this counterfactual prediction is [0,020, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0017 with a 95% interval of [-0,0029, -0,00058]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,93. By contrast, had the intervention not taken place, we would have expected a sum of 4,27. The 95% interval of this prediction is [4,04, 4,51].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -8%. The 95% interval of this percentage is [-14%, -3%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,02                  12,55              
Prediction (s.d.)        0,022 (0,00042)       13,609 (0,26071)   
95% CI                   [0,021, 0,023]        [13,087, 14,114]   
                                                                  
Absolute effect (s.d.)   -0,0017 (0,00042)     -1,0562 (0,26071)  
95% CI                   [-0,0025, -0,00086]   [-1,5604, -0,53383]
                                                                  
Relative effect (s.d.)   -7,8% (1,9%)          -7,8% (1,9%)       
95% CI                   [-11%, -3,9%]         [-11%, -3,9%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89868%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,022. The 95% interval of this counterfactual prediction is [0,021, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0017 with a 95% interval of [-0,0025, -0,00086]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 12,55. By contrast, had the intervention not taken place, we would have expected a sum of 13,61. The 95% interval of this prediction is [13,09, 14,11].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -8%. The 95% interval of this percentage is [-11%, -4%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0024               0,4836            
Prediction (s.d.)        0,0045 (0,00015)     0,9064 (0,02910)  
95% CI                   [0,0042, 0,0048]     [0,8496, 0,9654]  
                                                                
Absolute effect (s.d.)   -0,0021 (0,00015)    -0,4227 (0,02910) 
95% CI                   [-0,0024, -0,0018]   [-0,4818, -0,3660]
                                                                
Relative effect (s.d.)   -47% (3,2%)          -47% (3,2%)       
95% CI                   [-53%, -40%]         [-53%, -40%]      

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89796%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0024. By contrast, in the absence of an intervention, we would have expected an average response of 0,0045. The 95% interval of this counterfactual prediction is [0,0042, 0,0048]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0021 with a 95% interval of [-0,0024, -0,0018]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,48. By contrast, had the intervention not taken place, we would have expected a sum of 0,91. The 95% interval of this prediction is [0,85, 0,97].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -47%. The 95% interval of this percentage is [-53%, -40%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,0026              1,5995           
Prediction (s.d.)        0,0043 (0,0001)     2,7067 (0,0629)  
95% CI                   [0,0041, 0,0045]    [2,5830, 2,8274] 
                                                              
Absolute effect (s.d.)   -0,0018 (0,0001)    -1,1072 (0,0629) 
95% CI                   [-0,002, -0,0016]   [-1,228, -0,9835]
                                                              
Relative effect (s.d.)   -41% (2,3%)         -41% (2,3%)      
95% CI                   [-45%, -36%]        [-45%, -36%]     

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89733%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0026. By contrast, in the absence of an intervention, we would have expected an average response of 0,0043. The 95% interval of this counterfactual prediction is [0,0041, 0,0045]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0018 with a 95% interval of [-0,0020, -0,0016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,60. By contrast, had the intervention not taken place, we would have expected a sum of 2,71. The 95% interval of this prediction is [2,58, 2,83].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -41%. The 95% interval of this percentage is [-45%, -36%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,56               112,98          
Prediction (s.d.)        0,59 (0,0052)      117,74 (1,0337) 
95% CI                   [0,58, 0,6]        [115,77, 119,8] 
                                                            
Absolute effect (s.d.)   -0,024 (0,0052)    -4,758 (1,0337) 
95% CI                   [-0,034, -0,014]   [-6,805, -2,791]
                                                            
Relative effect (s.d.)   -4% (0,88%)        -4% (0,88%)     
95% CI                   [-5,8%, -2,4%]     [-5,8%, -2,4%]  

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89744%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,59. The 95% interval of this counterfactual prediction is [0,58, 0,60]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,024 with a 95% interval of [-0,034, -0,014]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 112,98. By contrast, had the intervention not taken place, we would have expected a sum of 117,74. The 95% interval of this prediction is [115,77, 119,79].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative        
Actual                   0,56               349,44            
Prediction (s.d.)        0,59 (0,0051)      365,83 (3,1545)   
95% CI                   [0,58, 0,6]        [359,56, 371,9]   
                                                              
Absolute effect (s.d.)   -0,026 (0,0051)    -16,385 (3,1545)  
95% CI                   [-0,036, -0,016]   [-22,444, -10,119]
                                                              
Relative effect (s.d.)   -4,5% (0,86%)      -4,5% (0,86%)     
95% CI                   [-6,1%, -2,8%]     [-6,1%, -2,8%]    

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,59. The 95% interval of this counterfactual prediction is [0,58, 0,60]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,026 with a 95% interval of [-0,036, -0,016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 349,44. By contrast, had the intervention not taken place, we would have expected a sum of 365,83. The 95% interval of this prediction is [359,56, 371,89].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -3%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,12              23,92          
Prediction (s.d.)        0,11 (0,0023)     21,09 (0,4622) 
95% CI                   [0,1, 0,11]       [20,2, 22,06]  
                                                          
Absolute effect (s.d.)   0,014 (0,0023)    2,832 (0,4622) 
95% CI                   [0,0093, 0,019]   [1,8634, 3,740]
                                                          
Relative effect (s.d.)   13% (2,2%)        13% (2,2%)     
95% CI                   [8,8%, 18%]       [8,8%, 18%]    

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89723%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,014 with a 95% interval of [0,0093, 0,019]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 23,92. By contrast, had the intervention not taken place, we would have expected a sum of 21,09. The 95% interval of this prediction is [20,18, 22,06].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +13%. The 95% interval of this percentage is [+9%, +18%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,014) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative     
Actual                   0,12             74,78          
Prediction (s.d.)        0,11 (0,0017)    66,16 (1,0347) 
95% CI                   [0,1, 0,11]      [64,1, 68,13]  
                                                         
Absolute effect (s.d.)   0,014 (0,0017)   8,619 (1,0347) 
95% CI                   [0,011, 0,017]   [6,648, 10,656]
                                                         
Relative effect (s.d.)   13% (1,6%)       13% (1,6%)     
95% CI                   [10%, 16%]       [10%, 16%]     

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89723%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,014 with a 95% interval of [0,011, 0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 74,78. By contrast, had the intervention not taken place, we would have expected a sum of 66,16. The 95% interval of this prediction is [64,12, 68,13].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +13%. The 95% interval of this percentage is [+10%, +16%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,014) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,85               169,39          
Prediction (s.d.)        0,87 (0,008)       173,84 (1,596)  
95% CI                   [0,85, 0,89]       [170,80, 177,09]
                                                            
Absolute effect (s.d.)   -0,022 (0,008)     -4,450 (1,596)  
95% CI                   [-0,039, -0,007]   [-7,701, -1,405]
                                                            
Relative effect (s.d.)   -2,6% (0,92%)      -2,6% (0,92%)   
95% CI                   [-4,4%, -0,81%]    [-4,4%, -0,81%] 

Posterior tail-area probability p:   0,00207
Posterior prob. of a causal effect:  99,79317%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,85. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,85, 0,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,022 with a 95% interval of [-0,039, -0,0070]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 169,39. By contrast, had the intervention not taken place, we would have expected a sum of 173,84. The 95% interval of this prediction is [170,80, 177,09].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,84               524,63           
Prediction (s.d.)        0,87 (0,0076)      542,36 (4,7266)  
95% CI                   [0,85, 0,88]       [532,79, 551,09] 
                                                             
Absolute effect (s.d.)   -0,028 (0,0076)    -17,737 (4,7266) 
95% CI                   [-0,042, -0,013]   [-26,461, -8,164]
                                                             
Relative effect (s.d.)   -3,3% (0,87%)      -3,3% (0,87%)    
95% CI                   [-4,9%, -1,5%]     [-4,9%, -1,5%]   

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89827%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,85, 0,88]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,028 with a 95% interval of [-0,042, -0,013]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 524,63. By contrast, had the intervention not taken place, we would have expected a sum of 542,36. The 95% interval of this prediction is [532,79, 551,09].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,016                3,206             
Prediction (s.d.)        0,015 (0,00077)      3,065 (0,15400)   
95% CI                   [0,014, 0,017]       [2,770, 3,375]    
                                                                
Absolute effect (s.d.)   0,0007 (0,00077)     0,1408 (0,15400)  
95% CI                   [-0,00085, 0,0022]   [-0,16907, 0,4362]
                                                                
Relative effect (s.d.)   4,6% (5%)            4,6% (5%)         
95% CI                   [-5,5%, 14%]         [-5,5%, 14%]      

Posterior tail-area probability p:   0,17444
Posterior prob. of a causal effect:  83%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. In the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,017]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00070 with a 95% interval of [-0,00085, 0,0022]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,21. Had the intervention not taken place, we would have expected a sum of 3,07. The 95% interval of this prediction is [2,77, 3,37].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +5%. The 95% interval of this percentage is [-6%, +14%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,174. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,016              10,282          
Prediction (s.d.)        0,015 (0,00042)    9,559 (0,26291) 
95% CI                   [0,014, 0,016]     [9,039, 10,073] 
                                                            
Absolute effect (s.d.)   0,0012 (0,00042)   0,7221 (0,26291)
95% CI                   [0,00033, 0,002]   [0,20846, 1,242]
                                                            
Relative effect (s.d.)   7,6% (2,8%)        7,6% (2,8%)     
95% CI                   [2,2%, 13%]        [2,2%, 13%]     

Posterior tail-area probability p:   0,00303
Posterior prob. of a causal effect:  99,69697%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. By contrast, in the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0012 with a 95% interval of [0,00033, 0,0020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 10,28. By contrast, had the intervention not taken place, we would have expected a sum of 9,56. The 95% interval of this prediction is [9,04, 10,07].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +8%. The 95% interval of this percentage is [+2%, +13%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0012) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,003). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 1528"
[1] "number of repositories <=-95% top_performer: 98     6,41361256544503 %"
[1] "number of repositories <0 good_performer: 138     9,03141361256544 %"
[1] "number of repositories =0 no_change_with_problems: 1035     67,7356020942408 %"
[1] "number of repositories >0 worst_performer: 257     16,8193717277487 %"
[1] "sum problems added - problems fixed: -440,439247617026"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 239"
[1] "number of repositories <=-95% top_performer: 24     10,0418410041841 %"
[1] "number of repositories <0 good_performer: 13     5,43933054393306 %"
[1] "number of repositories =0 no_change_with_problems: 181     75,7322175732218 %"
[1] "number of repositories >0 worst_performer: 21     8,78661087866109 %"
[1] "sum problems added - problems fixed: -22,3897689321446"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 105"
[1] "number of repositories <=-95% top_performer: 12     11,4285714285714 %"
[1] "number of repositories <0 good_performer: 11     10,4761904761905 %"
[1] "number of repositories =0 no_change_with_problems: 60     57,1428571428571 %"
[1] "number of repositories >0 worst_performer: 22     20,952380952381 %"
[1] "sum problems added - problems fixed: -15,4028935991118"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 5"
[1] "number of repositories <=-95% top_performer: 1     20 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 2     40 %"
[1] "number of repositories >0 worst_performer: 2     40 %"
[1] "sum problems added - problems fixed: -19,0994579945799"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 559"
[1] "number of repositories <=-95% top_performer: 29     5,18783542039356 %"
[1] "number of repositories <0 good_performer: 30     5,36672629695885 %"
[1] "number of repositories =0 no_change_with_problems: 441     78,8908765652952 %"
[1] "number of repositories >0 worst_performer: 59     10,5545617173524 %"
[1] "sum problems added - problems fixed: -221,641636542513"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 370"
[1] "number of repositories <=-95% top_performer: 24     6,48648648648649 %"
[1] "number of repositories <0 good_performer: 36     9,72972972972973 %"
[1] "number of repositories =0 no_change_with_problems: 241     65,1351351351351 %"
[1] "number of repositories >0 worst_performer: 69     18,6486486486486 %"
[1] "sum problems added - problems fixed: 103,741583535301"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 1098"
[1] "number of repositories <=-95% top_performer: 73     6,64845173041894 %"
[1] "number of repositories <0 good_performer: 89     8,10564663023679 %"
[1] "number of repositories =0 no_change_with_problems: 790     71,9489981785064 %"
[1] "number of repositories >0 worst_performer: 146     13,2969034608379 %"
[1] "sum problems added - problems fixed: -277,163046658722"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 8533"
[1] "number of repos with problems in this 90 day timeframe: 57"
[1] "number of repositories <=-95% top_performer: 8     14,0350877192982 %"
[1] "number of repositories <0 good_performer: 2     3,50877192982456 %"
[1] "number of repositories =0 no_change_with_problems: 29     50,8771929824561 %"
[1] "number of repositories >0 worst_performer: 18     31,5789473684211 %"
[1] "sum problems added - problems fixed: 11,515972574744"
[1] "number of repos with overall problems in this 700 day timeframe: 1202"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 220"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 105"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 10"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 469"
[1] "number of repos with xss problems in this 700 day timeframe: 370"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 840"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 74"
