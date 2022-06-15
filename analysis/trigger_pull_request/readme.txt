[1] "Log information"
[1] "folder: trigger_pull_request"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,8                367,2            
Prediction (s.d.)        1,9 (0,014)        373,6 (2,868)    
95% CI                   [1,8, 1,9]         [368,0, 379,2]   
                                                             
Absolute effect (s.d.)   -0,032 (0,014)     -6,343 (2,868)   
95% CI                   [-0,06, -0,0038]   [-12,02, -0,7572]
                                                             
Relative effect (s.d.)   -1,7% (0,77%)      -1,7% (0,77%)    
95% CI                   [-3,2%, -0,2%]     [-3,2%, -0,2%]   

Posterior tail-area probability p:   0,01237
Posterior prob. of a causal effect:  98,763%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,84. By contrast, in the absence of an intervention, we would have expected an average response of 1,87. The 95% interval of this counterfactual prediction is [1,84, 1,90]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,032 with a 95% interval of [-0,060, -0,0038]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 367,23. By contrast, had the intervention not taken place, we would have expected a sum of 373,58. The 95% interval of this prediction is [367,99, 379,25].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-3%, -0%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,012). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative        
Actual                   1,8                 1139,6            
Prediction (s.d.)        1,9 (0,014)         1162,4 (8,839)    
95% CI                   [1,8, 1,9]          [1144,8, 1179,5]  
                                                               
Absolute effect (s.d.)   -0,037 (0,014)      -22,806 (8,839)   
95% CI                   [-0,064, -0,0083]   [-39,949, -5,1821]
                                                               
Relative effect (s.d.)   -2% (0,76%)         -2% (0,76%)       
95% CI                   [-3,4%, -0,45%]     [-3,4%, -0,45%]   

Posterior tail-area probability p:   0,01031
Posterior prob. of a causal effect:  98,969%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,83. By contrast, in the absence of an intervention, we would have expected an average response of 1,86. The 95% interval of this counterfactual prediction is [1,83, 1,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,037 with a 95% interval of [-0,064, -0,0083]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,14K. By contrast, had the intervention not taken place, we would have expected a sum of 1,16K. The 95% interval of this prediction is [1,14K, 1,18K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-3%, -0%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,01). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,26                51,37            
Prediction (s.d.)        0,26 (0,0026)       51,84 (0,5281)   
95% CI                   [0,25, 0,26]        [50,81, 52,90]   
                                                              
Absolute effect (s.d.)   -0,0024 (0,0026)    -0,4701 (0,5281) 
95% CI                   [-0,0076, 0,0028]   [-1,5285, 0,5646]
                                                              
Relative effect (s.d.)   -0,91% (1%)         -0,91% (1%)      
95% CI                   [-2,9%, 1,1%]       [-2,9%, 1,1%]    

Posterior tail-area probability p:   0,18126
Posterior prob. of a causal effect:  82%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,26. In the absence of an intervention, we would have expected an average response of 0,26. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0024 with a 95% interval of [-0,0076, 0,0028]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 51,37. Had the intervention not taken place, we would have expected a sum of 51,84. The 95% interval of this prediction is [50,81, 52,90].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-3%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,181. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,26                161,39           
Prediction (s.d.)        0,26 (0,0029)       160,26 (1,8029)  
95% CI                   [0,25, 0,26]        [156,70, 163,79] 
                                                              
Absolute effect (s.d.)   0,0018 (0,0029)     1,1292 (1,8029)  
95% CI                   [-0,0038, 0,0075]   [-2,3993, 4,6931]
                                                              
Relative effect (s.d.)   0,7% (1,1%)         0,7% (1,1%)      
95% CI                   [-1,5%, 2,9%]       [-1,5%, 2,9%]    

Posterior tail-area probability p:   0,26497
Posterior prob. of a causal effect:  74%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,26. In the absence of an intervention, we would have expected an average response of 0,26. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0018 with a 95% interval of [-0,0038, 0,0075]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 161,39. Had the intervention not taken place, we would have expected a sum of 160,26. The 95% interval of this prediction is [156,70, 163,79].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +1%. The 95% interval of this percentage is [-1%, +3%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,265. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,02                 3,97              
Prediction (s.d.)        0,022 (0,00058)      4,310 (0,11510)   
95% CI                   [0,02, 0,023]        [4,09, 4,539]     
                                                                
Absolute effect (s.d.)   -0,0017 (0,00058)    -0,3442 (0,11510) 
95% CI                   [-0,0029, -0,0006]   [-0,5737, -0,1205]
                                                                
Relative effect (s.d.)   -8% (2,7%)           -8% (2,7%)        
95% CI                   [-13%, -2,8%]        [-13%, -2,8%]     

Posterior tail-area probability p:   0,00209
Posterior prob. of a causal effect:  99,79079%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,022. The 95% interval of this counterfactual prediction is [0,020, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0017 with a 95% interval of [-0,0029, -0,00060]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,97. By contrast, had the intervention not taken place, we would have expected a sum of 4,31. The 95% interval of this prediction is [4,09, 4,54].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -8%. The 95% interval of this percentage is [-13%, -3%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,02                  12,65              
Prediction (s.d.)        0,022 (0,00041)       13,773 (0,25589)   
95% CI                   [0,021, 0,023]        [13,273, 14,265]   
                                                                  
Absolute effect (s.d.)   -0,0018 (0,00041)     -1,1196 (0,25589)  
95% CI                   [-0,0026, -0,00099]   [-1,6113, -0,61956]
                                                                  
Relative effect (s.d.)   -8,1% (1,9%)          -8,1% (1,9%)       
95% CI                   [-12%, -4,5%]         [-12%, -4,5%]      

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8997%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,022. The 95% interval of this counterfactual prediction is [0,021, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0018 with a 95% interval of [-0,0026, -0,00099]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 12,65. By contrast, had the intervention not taken place, we would have expected a sum of 13,77. The 95% interval of this prediction is [13,27, 14,26].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -8%. The 95% interval of this percentage is [-12%, -4%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0025               0,4933            
Prediction (s.d.)        0,0045 (0,00015)     0,8941 (0,02959)  
95% CI                   [0,0042, 0,0048]     [0,8368, 0,9515]  
                                                                
Absolute effect (s.d.)   -0,002 (0,00015)     -0,401 (0,02959)  
95% CI                   [-0,0023, -0,0017]   [-0,4582, -0,3435]
                                                                
Relative effect (s.d.)   -45% (3,3%)          -45% (3,3%)       
95% CI                   [-51%, -38%]         [-51%, -38%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89463%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0025. By contrast, in the absence of an intervention, we would have expected an average response of 0,0045. The 95% interval of this counterfactual prediction is [0,0042, 0,0048]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0020 with a 95% interval of [-0,0023, -0,0017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,49. By contrast, had the intervention not taken place, we would have expected a sum of 0,89. The 95% interval of this prediction is [0,84, 0,95].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -45%. The 95% interval of this percentage is [-51%, -38%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0026               1,6270            
Prediction (s.d.)        0,0043 (0,00011)     2,7030 (0,06645)  
95% CI                   [0,0041, 0,0045]     [2,5693, 2,8309]  
                                                                
Absolute effect (s.d.)   -0,0017 (0,00011)    -1,0760 (0,06645) 
95% CI                   [-0,0019, -0,0015]   [-1,2039, -0,9423]
                                                                
Relative effect (s.d.)   -40% (2,5%)          -40% (2,5%)       
95% CI                   [-45%, -35%]         [-45%, -35%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89474%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0026. By contrast, in the absence of an intervention, we would have expected an average response of 0,0043. The 95% interval of this counterfactual prediction is [0,0041, 0,0045]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0017 with a 95% interval of [-0,0019, -0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,63. By contrast, had the intervention not taken place, we would have expected a sum of 2,70. The 95% interval of this prediction is [2,57, 2,83].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -40%. The 95% interval of this percentage is [-45%, -35%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,57               114,18          
Prediction (s.d.)        0,59 (0,0044)      118,06 (0,8805) 
95% CI                   [0,58, 0,6]        [116,34, 119,9] 
                                                            
Absolute effect (s.d.)   -0,019 (0,0044)    -3,884 (0,8805) 
95% CI                   [-0,029, -0,011]   [-5,705, -2,159]
                                                            
Relative effect (s.d.)   -3,3% (0,75%)      -3,3% (0,75%)   
95% CI                   [-4,8%, -1,8%]     [-4,8%, -1,8%]  

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89744%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,57. By contrast, in the absence of an intervention, we would have expected an average response of 0,59. The 95% interval of this counterfactual prediction is [0,58, 0,60]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,019 with a 95% interval of [-0,029, -0,011]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 114,18. By contrast, had the intervention not taken place, we would have expected a sum of 118,06. The 95% interval of this prediction is [116,34, 119,89].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,56               352,48           
Prediction (s.d.)        0,59 (0,005)       367,11 (3,106)   
95% CI                   [0,58, 0,6]        [360,98, 373,1]  
                                                             
Absolute effect (s.d.)   -0,023 (0,005)     -14,630 (3,106)  
95% CI                   [-0,033, -0,014]   [-20,626, -8,505]
                                                             
Relative effect (s.d.)   -4% (0,85%)        -4% (0,85%)      
95% CI                   [-5,6%, -2,3%]     [-5,6%, -2,3%]   

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,59. The 95% interval of this counterfactual prediction is [0,58, 0,60]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,023 with a 95% interval of [-0,033, -0,014]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 352,48. By contrast, had the intervention not taken place, we would have expected a sum of 367,11. The 95% interval of this prediction is [360,98, 373,11].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,12              23,92          
Prediction (s.d.)        0,11 (0,0023)     21,37 (0,4617) 
95% CI                   [0,1, 0,11]       [20,5, 22,30]  
                                                          
Absolute effect (s.d.)   0,013 (0,0023)    2,548 (0,4617) 
95% CI                   [0,0081, 0,017]   [1,6208, 3,434]
                                                          
Relative effect (s.d.)   12% (2,2%)        12% (2,2%)     
95% CI                   [7,6%, 16%]       [7,6%, 16%]    

Posterior tail-area probability p:   0,00106
Posterior prob. of a causal effect:  99,89429%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,013 with a 95% interval of [0,0081, 0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 23,92. By contrast, had the intervention not taken place, we would have expected a sum of 21,37. The 95% interval of this prediction is [20,48, 22,30].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +12%. The 95% interval of this percentage is [+8%, +16%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,013) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,12              74,49          
Prediction (s.d.)        0,11 (0,0016)     66,63 (1,0023) 
95% CI                   [0,1, 0,11]       [64,7, 68,56]  
                                                          
Absolute effect (s.d.)   0,013 (0,0016)    7,858 (1,0023) 
95% CI                   [0,0095, 0,016]   [5,9273, 9,806]
                                                          
Relative effect (s.d.)   12% (1,5%)        12% (1,5%)     
95% CI                   [8,9%, 15%]       [8,9%, 15%]    

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8995%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,013 with a 95% interval of [0,0095, 0,016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 74,49. By contrast, had the intervention not taken place, we would have expected a sum of 66,63. The 95% interval of this prediction is [64,68, 68,56].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +12%. The 95% interval of this percentage is [+9%, +15%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,013) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,85                170,17           
Prediction (s.d.)        0,87 (0,0082)       174,45 (1,6436)  
95% CI                   [0,86, 0,89]        [171,46, 177,83] 
                                                              
Absolute effect (s.d.)   -0,021 (0,0082)     -4,272 (1,6436)  
95% CI                   [-0,038, -0,0064]   [-7,652, -1,2846]
                                                              
Relative effect (s.d.)   -2,4% (0,94%)       -2,4% (0,94%)    
95% CI                   [-4,4%, -0,74%]     [-4,4%, -0,74%]  

Posterior tail-area probability p:   0,00611
Posterior prob. of a causal effect:  99,389%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,85. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,86, 0,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,021 with a 95% interval of [-0,038, -0,0064]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 170,17. By contrast, had the intervention not taken place, we would have expected a sum of 174,45. The 95% interval of this prediction is [171,46, 177,83].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,006). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,84              526,94          
Prediction (s.d.)        0,87 (0,0074)     543,40 (4,6159) 
95% CI                   [0,86, 0,88]      [534,25, 552,15]
                                                           
Absolute effect (s.d.)   -0,026 (0,0074)   -16,460 (4,6159)
95% CI                   [-0,04, -0,012]   [-25,20, -7,308]
                                                           
Relative effect (s.d.)   -3% (0,85%)       -3% (0,85%)     
95% CI                   [-4,6%, -1,3%]    [-4,6%, -1,3%]  

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89827%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,86, 0,88]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,026 with a 95% interval of [-0,040, -0,012]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 526,94. By contrast, had the intervention not taken place, we would have expected a sum of 543,40. The 95% interval of this prediction is [534,25, 552,15].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,016                3,127             
Prediction (s.d.)        0,015 (0,00073)      2,984 (0,14637)   
95% CI                   [0,014, 0,016]       [2,709, 3,283]    
                                                                
Absolute effect (s.d.)   0,00071 (0,00073)    0,14244 (0,14637) 
95% CI                   [-0,00078, 0,0021]   [-0,15684, 0,4174]
                                                                
Relative effect (s.d.)   4,8% (4,9%)          4,8% (4,9%)       
95% CI                   [-5,3%, 14%]         [-5,3%, 14%]      

Posterior tail-area probability p:   0,15558
Posterior prob. of a causal effect:  84%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. In the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00071 with a 95% interval of [-0,00078, 0,0021]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,13. Had the intervention not taken place, we would have expected a sum of 2,98. The 95% interval of this prediction is [2,71, 3,28].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +5%. The 95% interval of this percentage is [-5%, +14%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,156. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,016              10,017          
Prediction (s.d.)        0,015 (0,00041)    9,307 (0,25519) 
95% CI                   [0,014, 0,016]     [8,795, 9,805]  
                                                            
Absolute effect (s.d.)   0,0011 (0,00041)   0,7093 (0,25519)
95% CI                   [0,00034, 0,002]   [0,21205, 1,221]
                                                            
Relative effect (s.d.)   7,6% (2,7%)        7,6% (2,7%)     
95% CI                   [2,3%, 13%]        [2,3%, 13%]     

Posterior tail-area probability p:   0,00202
Posterior prob. of a causal effect:  99,79818%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. By contrast, in the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0011 with a 95% interval of [0,00034, 0,0020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 10,02. By contrast, had the intervention not taken place, we would have expected a sum of 9,31. The 95% interval of this prediction is [8,80, 9,80].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +8%. The 95% interval of this percentage is [+2%, +13%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0011) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 1563"
[1] "number of repositories <=-95% top_performer: 100     6,39795265515035 %"
[1] "number of repositories <0 good_performer: 150     9,59692898272553 %"
[1] "number of repositories =0 no_change_with_problems: 1055     67,4984005118362 %"
[1] "number of repositories >0 worst_performer: 258     16,5067178502879 %"
[1] "sum problems added - problems fixed: -432,702977775756"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 246"
[1] "number of repositories <=-95% top_performer: 23     9,34959349593496 %"
[1] "number of repositories <0 good_performer: 13     5,28455284552846 %"
[1] "number of repositories =0 no_change_with_problems: 186     75,609756097561 %"
[1] "number of repositories >0 worst_performer: 24     9,75609756097561 %"
[1] "sum problems added - problems fixed: -17,8354479444902"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 111"
[1] "number of repositories <=-95% top_performer: 14     12,6126126126126 %"
[1] "number of repositories <0 good_performer: 12     10,8108108108108 %"
[1] "number of repositories =0 no_change_with_problems: 63     56,7567567567568 %"
[1] "number of repositories >0 worst_performer: 22     19,8198198198198 %"
[1] "sum problems added - problems fixed: -17,8695602657785"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 6"
[1] "number of repositories <=-95% top_performer: 1     16,6666666666667 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 3     50 %"
[1] "number of repositories >0 worst_performer: 2     33,3333333333333 %"
[1] "sum problems added - problems fixed: -19,0994579945799"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 573"
[1] "number of repositories <=-95% top_performer: 29     5,06108202443281 %"
[1] "number of repositories <0 good_performer: 31     5,41012216404887 %"
[1] "number of repositories =0 no_change_with_problems: 452     78,8830715532286 %"
[1] "number of repositories >0 worst_performer: 61     10,6457242582897 %"
[1] "sum problems added - problems fixed: -209,270340246217"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 384"
[1] "number of repositories <=-95% top_performer: 25     6,51041666666667 %"
[1] "number of repositories <0 good_performer: 40     10,4166666666667 %"
[1] "number of repositories =0 no_change_with_problems: 250     65,1041666666667 %"
[1] "number of repositories >0 worst_performer: 69     17,96875 %"
[1] "sum problems added - problems fixed: 100,849520043238"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 1120"
[1] "number of repositories <=-95% top_performer: 76     6,78571428571429 %"
[1] "number of repositories <0 good_performer: 95     8,48214285714286 %"
[1] "number of repositories =0 no_change_with_problems: 803     71,6964285714286 %"
[1] "number of repositories >0 worst_performer: 146     13,0357142857143 %"
[1] "sum problems added - problems fixed: -280,993663942673"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 8772"
[1] "number of repos with problems in this 90 day timeframe: 57"
[1] "number of repositories <=-95% top_performer: 8     14,0350877192982 %"
[1] "number of repositories <0 good_performer: 2     3,50877192982456 %"
[1] "number of repositories =0 no_change_with_problems: 29     50,8771929824561 %"
[1] "number of repositories >0 worst_performer: 18     31,5789473684211 %"
[1] "sum problems added - problems fixed: 11,515972574744"
[1] "number of repos with overall problems in this 700 day timeframe: 1235"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 224"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 111"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 11"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 479"
[1] "number of repos with xss problems in this 700 day timeframe: 385"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 861"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 80"
