[1] "Log information"
[1] "folder: all_excl4287066"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,8                363,2            
Prediction (s.d.)        1,9 (0,015)        371,7 (2,918)    
95% CI                   [1,8, 1,9]         [366,3, 377,6]   
                                                             
Absolute effect (s.d.)   -0,043 (0,015)     -8,552 (2,918)   
95% CI                   [-0,072, -0,016]   [-14,493, -3,117]
                                                             
Relative effect (s.d.)   -2,3% (0,79%)      -2,3% (0,79%)    
95% CI                   [-3,9%, -0,84%]    [-3,9%, -0,84%]  

Posterior tail-area probability p:   0,00203
Posterior prob. of a causal effect:  99,79695%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,82. By contrast, in the absence of an intervention, we would have expected an average response of 1,86. The 95% interval of this counterfactual prediction is [1,83, 1,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,043 with a 95% interval of [-0,072, -0,016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 363,15. By contrast, had the intervention not taken place, we would have expected a sum of 371,70. The 95% interval of this prediction is [366,27, 377,65].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,8                1127,2           
Prediction (s.d.)        1,8 (0,014)        1151,6 (8,824)   
95% CI                   [1,8, 1,9]         [1133,9, 1168,7] 
                                                             
Absolute effect (s.d.)   -0,039 (0,014)     -24,453 (8,824)  
95% CI                   [-0,067, -0,011]   [-41,569, -6,778]
                                                             
Relative effect (s.d.)   -2,1% (0,77%)      -2,1% (0,77%)    
95% CI                   [-3,6%, -0,59%]    [-3,6%, -0,59%]  

Posterior tail-area probability p:   0,00825
Posterior prob. of a causal effect:  99,17526%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,81. By contrast, in the absence of an intervention, we would have expected an average response of 1,85. The 95% interval of this counterfactual prediction is [1,82, 1,87]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,039 with a 95% interval of [-0,067, -0,011]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,13K. By contrast, had the intervention not taken place, we would have expected a sum of 1,15K. The 95% interval of this prediction is [1,13K, 1,17K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,008). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,25                50,75            
Prediction (s.d.)        0,26 (0,0027)       51,14 (0,5456)   
95% CI                   [0,25, 0,26]        [50,09, 52,25]   
                                                              
Absolute effect (s.d.)   -0,0019 (0,0027)    -0,3833 (0,5456) 
95% CI                   [-0,0075, 0,0033]   [-1,4984, 0,6671]
                                                              
Relative effect (s.d.)   -0,75% (1,1%)       -0,75% (1,1%)    
95% CI                   [-2,9%, 1,3%]       [-2,9%, 1,3%]    

Posterior tail-area probability p:   0,23327
Posterior prob. of a causal effect:  77%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,25. In the absence of an intervention, we would have expected an average response of 0,26. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0019 with a 95% interval of [-0,0075, 0,0033]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 50,75. Had the intervention not taken place, we would have expected a sum of 51,14. The 95% interval of this prediction is [50,09, 52,25].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-3%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,233. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,26                159,43           
Prediction (s.d.)        0,25 (0,0028)       158,59 (1,7697)  
95% CI                   [0,25, 0,26]        [155,12, 162,01] 
                                                              
Absolute effect (s.d.)   0,0013 (0,0028)     0,8353 (1,7697)  
95% CI                   [-0,0041, 0,0069]   [-2,5870, 4,3029]
                                                              
Relative effect (s.d.)   0,53% (1,1%)        0,53% (1,1%)     
95% CI                   [-1,6%, 2,7%]       [-1,6%, 2,7%]    

Posterior tail-area probability p:   0,3033
Posterior prob. of a causal effect:  70%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,26. In the absence of an intervention, we would have expected an average response of 0,25. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0013 with a 95% interval of [-0,0041, 0,0069]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 159,43. Had the intervention not taken place, we would have expected a sum of 158,59. The 95% interval of this prediction is [155,12, 162,01].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +1%. The 95% interval of this percentage is [-2%, +3%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,303. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,02                  4,07               
Prediction (s.d.)        0,022 (0,00054)       4,393 (0,10825)    
95% CI                   [0,021, 0,023]        [4,190, 4,616]     
                                                                  
Absolute effect (s.d.)   -0,0016 (0,00054)     -0,3252 (0,10825)  
95% CI                   [-0,0027, -0,00061]   [-0,5478, -0,12183]
                                                                  
Relative effect (s.d.)   -7,4% (2,5%)          -7,4% (2,5%)       
95% CI                   [-12%, -2,8%]         [-12%, -2,8%]      

Posterior tail-area probability p:   0,00206
Posterior prob. of a causal effect:  99,79381%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,022. The 95% interval of this counterfactual prediction is [0,021, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0016 with a 95% interval of [-0,0027, -0,00061]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 4,07. By contrast, had the intervention not taken place, we would have expected a sum of 4,39. The 95% interval of this prediction is [4,19, 4,62].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -7%. The 95% interval of this percentage is [-12%, -3%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,021                 13,029             
Prediction (s.d.)        0,022 (0,0004)        13,917 (0,2489)    
95% CI                   [0,022, 0,023]        [13,419, 14,399]   
                                                                  
Absolute effect (s.d.)   -0,0014 (0,0004)      -0,8874 (0,2489)   
95% CI                   [-0,0022, -0,00063]   [-1,3698, -0,39025]
                                                                  
Relative effect (s.d.)   -6,4% (1,8%)          -6,4% (1,8%)       
95% CI                   [-9,8%, -2,8%]        [-9,8%, -2,8%]     

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89868%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,021. By contrast, in the absence of an intervention, we would have expected an average response of 0,022. The 95% interval of this counterfactual prediction is [0,022, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0014 with a 95% interval of [-0,0022, -0,00063]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 13,03. By contrast, had the intervention not taken place, we would have expected a sum of 13,92. The 95% interval of this prediction is [13,42, 14,40].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -6%. The 95% interval of this percentage is [-10%, -3%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0024               0,4845            
Prediction (s.d.)        0,0044 (0,00014)     0,8782 (0,02900)  
95% CI                   [0,0041, 0,0047]     [0,8215, 0,9346]  
                                                                
Absolute effect (s.d.)   -0,002 (0,00014)     -0,394 (0,02900)  
95% CI                   [-0,0023, -0,0017]   [-0,4501, -0,3370]
                                                                
Relative effect (s.d.)   -45% (3,3%)          -45% (3,3%)       
95% CI                   [-51%, -38%]         [-51%, -38%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89463%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0024. By contrast, in the absence of an intervention, we would have expected an average response of 0,0044. The 95% interval of this counterfactual prediction is [0,0041, 0,0047]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0020 with a 95% interval of [-0,0023, -0,0017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,48. By contrast, had the intervention not taken place, we would have expected a sum of 0,88. The 95% interval of this prediction is [0,82, 0,93].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -45%. The 95% interval of this percentage is [-51%, -38%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0026               1,5981            
Prediction (s.d.)        0,0043 (0,0001)      2,6549 (0,0653)   
95% CI                   [0,004, 0,0045]      [2,524, 2,7806]   
                                                                
Absolute effect (s.d.)   -0,0017 (0,0001)     -1,0568 (0,0653)  
95% CI                   [-0,0019, -0,0015]   [-1,1825, -0,9259]
                                                                
Relative effect (s.d.)   -40% (2,5%)          -40% (2,5%)       
95% CI                   [-45%, -35%]         [-45%, -35%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89474%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0026. By contrast, in the absence of an intervention, we would have expected an average response of 0,0043. The 95% interval of this counterfactual prediction is [0,0040, 0,0045]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0017 with a 95% interval of [-0,0019, -0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,60. By contrast, had the intervention not taken place, we would have expected a sum of 2,65. The 95% interval of this prediction is [2,52, 2,78].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -40%. The 95% interval of this percentage is [-45%, -35%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,56                112,59           
Prediction (s.d.)        0,58 (0,0042)       116,13 (0,8375)  
95% CI                   [0,57, 0,59]        [114,53, 117,85] 
                                                              
Absolute effect (s.d.)   -0,018 (0,0042)     -3,547 (0,8375)  
95% CI                   [-0,026, -0,0097]   [-5,268, -1,9444]
                                                              
Relative effect (s.d.)   -3,1% (0,72%)       -3,1% (0,72%)    
95% CI                   [-4,5%, -1,7%]      [-4,5%, -1,7%]   

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89744%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,58. The 95% interval of this counterfactual prediction is [0,57, 0,59]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,018 with a 95% interval of [-0,026, -0,0097]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 112,59. By contrast, had the intervention not taken place, we would have expected a sum of 116,13. The 95% interval of this prediction is [114,53, 117,85].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,56               347,59           
Prediction (s.d.)        0,58 (0,0049)      361,83 (3,0835)  
95% CI                   [0,57, 0,59]       [355,69, 367,83] 
                                                             
Absolute effect (s.d.)   -0,023 (0,0049)    -14,235 (3,0835) 
95% CI                   [-0,032, -0,013]   [-20,243, -8,097]
                                                             
Relative effect (s.d.)   -3,9% (0,85%)      -3,9% (0,85%)    
95% CI                   [-5,6%, -2,2%]     [-5,6%, -2,2%]   

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,58. The 95% interval of this counterfactual prediction is [0,57, 0,59]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,023 with a 95% interval of [-0,032, -0,013]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 347,59. By contrast, had the intervention not taken place, we would have expected a sum of 361,83. The 95% interval of this prediction is [355,69, 367,83].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,12              23,55          
Prediction (s.d.)        0,1 (0,0021)      21,0 (0,4286)  
95% CI                   [0,1, 0,11]       [20,1, 21,86]  
                                                          
Absolute effect (s.d.)   0,013 (0,0021)    2,589 (0,4286) 
95% CI                   [0,0085, 0,017]   [1,6988, 3,429]
                                                          
Relative effect (s.d.)   12% (2%)          12% (2%)       
95% CI                   [8,1%, 16%]       [8,1%, 16%]    

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,8968%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,10. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,013 with a 95% interval of [0,0085, 0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 23,55. By contrast, had the intervention not taken place, we would have expected a sum of 20,97. The 95% interval of this prediction is [20,13, 21,86].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +12%. The 95% interval of this percentage is [+8%, +16%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,013) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,12              73,32          
Prediction (s.d.)        0,11 (0,0016)     65,69 (1,0003) 
95% CI                   [0,1, 0,11]       [63,7, 67,60]  
                                                          
Absolute effect (s.d.)   0,012 (0,0016)    7,635 (1,0003) 
95% CI                   [0,0092, 0,015]   [5,7228, 9,595]
                                                          
Relative effect (s.d.)   12% (1,5%)        12% (1,5%)     
95% CI                   [8,7%, 15%]       [8,7%, 15%]    

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89723%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,012 with a 95% interval of [0,0092, 0,015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 73,32. By contrast, had the intervention not taken place, we would have expected a sum of 65,69. The 95% interval of this prediction is [63,73, 67,60].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +12%. The 95% interval of this percentage is [+9%, +15%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,012) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,84               168,64          
Prediction (s.d.)        0,87 (0,0079)      174,97 (1,5711) 
95% CI                   [0,86, 0,89]       [171,97, 178,05]
                                                            
Absolute effect (s.d.)   -0,032 (0,0079)    -6,334 (1,5711) 
95% CI                   [-0,047, -0,017]   [-9,414, -3,333]
                                                            
Relative effect (s.d.)   -3,6% (0,9%)       -3,6% (0,9%)    
95% CI                   [-5,4%, -1,9%]     [-5,4%, -1,9%]  

Posterior tail-area probability p:   0,00104
Posterior prob. of a causal effect:  99,89594%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,86, 0,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,032 with a 95% interval of [-0,047, -0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 168,64. By contrast, had the intervention not taken place, we would have expected a sum of 174,97. The 95% interval of this prediction is [171,97, 178,05].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,84               522,35           
Prediction (s.d.)        0,87 (0,0073)      539,83 (4,5734)  
95% CI                   [0,85, 0,88]       [531,00, 548,71] 
                                                             
Absolute effect (s.d.)   -0,028 (0,0073)    -17,479 (4,5734) 
95% CI                   [-0,042, -0,014]   [-26,357, -8,649]
                                                             
Relative effect (s.d.)   -3,2% (0,85%)      -3,2% (0,85%)    
95% CI                   [-4,9%, -1,6%]     [-4,9%, -1,6%]   

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89785%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,85, 0,88]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,028 with a 95% interval of [-0,042, -0,014]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 522,35. By contrast, had the intervention not taken place, we would have expected a sum of 539,83. The 95% interval of this prediction is [531,00, 548,71].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,015               3,071            
Prediction (s.d.)        0,015 (0,00094)     2,943 (0,18715)  
95% CI                   [0,013, 0,017]      [2,595, 3,324]   
                                                              
Absolute effect (s.d.)   0,00064 (0,00094)   0,12779 (0,18715)
95% CI                   [-0,0013, 0,0024]   [-0,2531, 0,4762]
                                                              
Relative effect (s.d.)   4,3% (6,4%)         4,3% (6,4%)      
95% CI                   [-8,6%, 16%]        [-8,6%, 16%]     

Posterior tail-area probability p:   0,23046
Posterior prob. of a causal effect:  77%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,015. In the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,013, 0,017]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00064 with a 95% interval of [-0,0013, 0,0024]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,07. Had the intervention not taken place, we would have expected a sum of 2,94. The 95% interval of this prediction is [2,59, 3,32].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +4%. The 95% interval of this percentage is [-9%, +16%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,23. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,016               9,838            
Prediction (s.d.)        0,015 (0,00051)     9,146 (0,31522)  
95% CI                   [0,014, 0,016]      [8,527, 9,755]   
                                                              
Absolute effect (s.d.)   0,0011 (0,00051)    0,6925 (0,31522) 
95% CI                   [0,00013, 0,0021]   [0,08300, 1,3114]
                                                              
Relative effect (s.d.)   7,6% (3,4%)         7,6% (3,4%)      
95% CI                   [0,91%, 14%]        [0,91%, 14%]     

Posterior tail-area probability p:   0,01104
Posterior prob. of a causal effect:  98,896%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. By contrast, in the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0011 with a 95% interval of [0,00013, 0,0021]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 9,84. By contrast, had the intervention not taken place, we would have expected a sum of 9,15. The 95% interval of this prediction is [8,53, 9,76].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +8%. The 95% interval of this percentage is [+1%, +14%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0011) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,011). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 1593"
[1] "number of repositories <=-95% top_performer: 102     6,4030131826742 %"
[1] "number of repositories <0 good_performer: 152     9,54174513496547 %"
[1] "number of repositories =0 no_change_with_problems: 1077     67,608286252354 %"
[1] "number of repositories >0 worst_performer: 262     16,4469554300063 %"
[1] "sum problems added - problems fixed: -462,89773006784"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 255"
[1] "number of repositories <=-95% top_performer: 25     9,80392156862745 %"
[1] "number of repositories <0 good_performer: 14     5,49019607843137 %"
[1] "number of repositories =0 no_change_with_problems: 192     75,2941176470588 %"
[1] "number of repositories >0 worst_performer: 24     9,41176470588235 %"
[1] "sum problems added - problems fixed: -22,7354479444902"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 112"
[1] "number of repositories <=-95% top_performer: 14     12,5 %"
[1] "number of repositories <0 good_performer: 12     10,7142857142857 %"
[1] "number of repositories =0 no_change_with_problems: 63     56,25 %"
[1] "number of repositories >0 worst_performer: 23     20,5357142857143 %"
[1] "sum problems added - problems fixed: -17,3155920118102"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 6"
[1] "number of repositories <=-95% top_performer: 1     16,6666666666667 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 3     50 %"
[1] "number of repositories >0 worst_performer: 2     33,3333333333333 %"
[1] "sum problems added - problems fixed: -19,0994579945799"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 578"
[1] "number of repositories <=-95% top_performer: 29     5,01730103806228 %"
[1] "number of repositories <0 good_performer: 32     5,5363321799308 %"
[1] "number of repositories =0 no_change_with_problems: 456     78,8927335640138 %"
[1] "number of repositories >0 worst_performer: 61     10,5536332179931 %"
[1] "sum problems added - problems fixed: -214,023118023994"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 387"
[1] "number of repositories <=-95% top_performer: 25     6,45994832041344 %"
[1] "number of repositories <0 good_performer: 40     10,3359173126615 %"
[1] "number of repositories =0 no_change_with_problems: 252     65,1162790697674 %"
[1] "number of repositories >0 worst_performer: 70     18,0878552971576 %"
[1] "sum problems added - problems fixed: 101,005075598793"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 1146"
[1] "number of repositories <=-95% top_performer: 77     6,71902268760907 %"
[1] "number of repositories <0 good_performer: 98     8,55148342059337 %"
[1] "number of repositories =0 no_change_with_problems: 822     71,7277486910995 %"
[1] "number of repositories >0 worst_performer: 149     13,0017452006981 %"
[1] "sum problems added - problems fixed: -302,245162266502"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 8931"
[1] "number of repos with problems in this 90 day timeframe: 57"
[1] "number of repositories <=-95% top_performer: 8     14,0350877192982 %"
[1] "number of repositories <0 good_performer: 2     3,50877192982456 %"
[1] "number of repositories =0 no_change_with_problems: 29     50,8771929824561 %"
[1] "number of repositories >0 worst_performer: 18     31,5789473684211 %"
[1] "sum problems added - problems fixed: 11,515972574744"
[1] "number of repos with overall problems in this 700 day timeframe: 1275"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 233"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 113"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 11"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 491"
[1] "number of repos with xss problems in this 700 day timeframe: 390"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 899"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 81"
