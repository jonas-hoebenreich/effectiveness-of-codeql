[1] "Log information"
[1] "folder: trigger_push"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   1,8               363,5           
Prediction (s.d.)        1,9 (0,014)       371,6 (2,898)   
95% CI                   [1,8, 1,9]        [366,0, 377,4]  
                                                           
Absolute effect (s.d.)   -0,041 (0,014)    -8,129 (2,898)  
95% CI                   [-0,07, -0,013]   [-13,98, -2,572]
                                                           
Relative effect (s.d.)   -2,2% (0,78%)     -2,2% (0,78%)   
95% CI                   [-3,8%, -0,69%]   [-3,8%, -0,69%] 

Posterior tail-area probability p:   0,00204
Posterior prob. of a causal effect:  99,79633%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,82. By contrast, in the absence of an intervention, we would have expected an average response of 1,86. The 95% interval of this counterfactual prediction is [1,83, 1,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,041 with a 95% interval of [-0,070, -0,013]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 363,45. By contrast, had the intervention not taken place, we would have expected a sum of 371,58. The 95% interval of this prediction is [366,03, 377,44].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative        
Actual                   1,8                 1128,1            
Prediction (s.d.)        1,8 (0,014)         1151,1 (8,903)    
95% CI                   [1,8, 1,9]          [1133,4, 1168,4]  
                                                               
Absolute effect (s.d.)   -0,037 (0,014)      -23,054 (8,903)   
95% CI                   [-0,065, -0,0085]   [-40,340, -5,2987]
                                                               
Relative effect (s.d.)   -2% (0,77%)         -2% (0,77%)       
95% CI                   [-3,5%, -0,46%]     [-3,5%, -0,46%]   

Posterior tail-area probability p:   0,01031
Posterior prob. of a causal effect:  98,969%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,81. By contrast, in the absence of an intervention, we would have expected an average response of 1,84. The 95% interval of this counterfactual prediction is [1,82, 1,87]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,037 with a 95% interval of [-0,065, -0,0085]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,13K. By contrast, had the intervention not taken place, we would have expected a sum of 1,15K. The 95% interval of this prediction is [1,13K, 1,17K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, -0%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,01). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,25               50,99           
Prediction (s.d.)        0,26 (0,0032)      51,95 (0,6427)  
95% CI                   [0,25, 0,27]       [50,68, 53,27]  
                                                            
Absolute effect (s.d.)   -0,0048 (0,0032)   -0,9598 (0,6427)
95% CI                   [-0,011, 0,0015]   [-2,278, 0,3074]
                                                            
Relative effect (s.d.)   -1,8% (1,2%)       -1,8% (1,2%)    
95% CI                   [-4,4%, 0,59%]     [-4,4%, 0,59%]  

Posterior tail-area probability p:   0,06415
Posterior prob. of a causal effect:  94%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,25. In the absence of an intervention, we would have expected an average response of 0,26. The 95% interval of this counterfactual prediction is [0,25, 0,27]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0048 with a 95% interval of [-0,011, 0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 50,99. Had the intervention not taken place, we would have expected a sum of 51,95. The 95% interval of this prediction is [50,68, 53,27].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-4%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,064. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,26                160,23           
Prediction (s.d.)        0,25 (0,0029)       159,00 (1,7865)  
95% CI                   [0,25, 0,26]        [155,52, 162,45] 
                                                              
Absolute effect (s.d.)   0,002 (0,0029)      1,225 (1,7865)   
95% CI                   [-0,0036, 0,0075]   [-2,2294, 4,7043]
                                                              
Relative effect (s.d.)   0,77% (1,1%)        0,77% (1,1%)     
95% CI                   [-1,4%, 3%]         [-1,4%, 3%]      

Posterior tail-area probability p:   0,24224
Posterior prob. of a causal effect:  76%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,26. In the absence of an intervention, we would have expected an average response of 0,25. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0020 with a 95% interval of [-0,0036, 0,0075]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 160,23. Had the intervention not taken place, we would have expected a sum of 159,00. The 95% interval of this prediction is [155,52, 162,45].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +1%. The 95% interval of this percentage is [-1%, +3%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,242. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,02                  3,97               
Prediction (s.d.)        0,021 (0,00058)       4,291 (0,11547)    
95% CI                   [0,02, 0,023]         [4,07, 4,536]      
                                                                  
Absolute effect (s.d.)   -0,0016 (0,00058)     -0,3248 (0,11547)  
95% CI                   [-0,0028, -0,00053]   [-0,5698, -0,10681]
                                                                  
Relative effect (s.d.)   -7,6% (2,7%)          -7,6% (2,7%)       
95% CI                   [-13%, -2,5%]         [-13%, -2,5%]      

Posterior tail-area probability p:   0,00204
Posterior prob. of a causal effect:  99,79633%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,021. The 95% interval of this counterfactual prediction is [0,020, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0016 with a 95% interval of [-0,0028, -0,00053]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,97. By contrast, had the intervention not taken place, we would have expected a sum of 4,29. The 95% interval of this prediction is [4,07, 4,54].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -8%. The 95% interval of this percentage is [-13%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,02                  12,69              
Prediction (s.d.)        0,022 (0,00041)       13,705 (0,25788)   
95% CI                   [0,021, 0,023]        [13,198, 14,201]   
                                                                  
Absolute effect (s.d.)   -0,0016 (0,00041)     -1,0134 (0,25788)  
95% CI                   [-0,0024, -0,00081]   [-1,5095, -0,50701]
                                                                  
Relative effect (s.d.)   -7,4% (1,9%)          -7,4% (1,9%)       
95% CI                   [-11%, -3,7%]         [-11%, -3,7%]      

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8996%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,022. The 95% interval of this counterfactual prediction is [0,021, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0016 with a 95% interval of [-0,0024, -0,00081]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 12,69. By contrast, had the intervention not taken place, we would have expected a sum of 13,70. The 95% interval of this prediction is [13,20, 14,20].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -7%. The 95% interval of this percentage is [-11%, -4%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0025               0,4926            
Prediction (s.d.)        0,0045 (0,00015)     0,8929 (0,02953)  
95% CI                   [0,0042, 0,0048]     [0,8358, 0,9505]  
                                                                
Absolute effect (s.d.)   -0,002 (0,00015)     -0,400 (0,02953)  
95% CI                   [-0,0023, -0,0017]   [-0,4579, -0,3433]
                                                                
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
Actual                   0,0026               1,6248            
Prediction (s.d.)        0,0043 (0,00011)     2,6993 (0,06640)  
95% CI                   [0,0041, 0,0045]     [2,5655, 2,8269]  
                                                                
Absolute effect (s.d.)   -0,0017 (0,00011)    -1,0745 (0,06640) 
95% CI                   [-0,0019, -0,0015]   [-1,2020, -0,9407]
                                                                
Relative effect (s.d.)   -40% (2,5%)          -40% (2,5%)       
95% CI                   [-45%, -35%]         [-45%, -35%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89474%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0026. By contrast, in the absence of an intervention, we would have expected an average response of 0,0043. The 95% interval of this counterfactual prediction is [0,0041, 0,0045]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0017 with a 95% interval of [-0,0019, -0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,62. By contrast, had the intervention not taken place, we would have expected a sum of 2,70. The 95% interval of this prediction is [2,57, 2,83].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -40%. The 95% interval of this percentage is [-45%, -35%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,56               112,80          
Prediction (s.d.)        0,58 (0,0044)      116,69 (0,8779) 
95% CI                   [0,57, 0,59]       [114,99, 118,49]
                                                            
Absolute effect (s.d.)   -0,019 (0,0044)    -3,893 (0,8779) 
95% CI                   [-0,028, -0,011]   [-5,697, -2,200]
                                                            
Relative effect (s.d.)   -3,3% (0,75%)      -3,3% (0,75%)   
95% CI                   [-4,9%, -1,9%]     [-4,9%, -1,9%]  

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89785%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,58. The 95% interval of this counterfactual prediction is [0,57, 0,59]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,019 with a 95% interval of [-0,028, -0,011]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 112,80. By contrast, had the intervention not taken place, we would have expected a sum of 116,69. The 95% interval of this prediction is [114,99, 118,49].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,56               348,16           
Prediction (s.d.)        0,58 (0,0049)      362,63 (3,0716)  
95% CI                   [0,57, 0,59]       [356,48, 368,68] 
                                                             
Absolute effect (s.d.)   -0,023 (0,0049)    -14,464 (3,0716) 
95% CI                   [-0,033, -0,013]   [-20,522, -8,315]
                                                             
Relative effect (s.d.)   -4% (0,85%)        -4% (0,85%)      
95% CI                   [-5,7%, -2,3%]     [-5,7%, -2,3%]   

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,58. The 95% interval of this counterfactual prediction is [0,57, 0,59]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,023 with a 95% interval of [-0,033, -0,013]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 348,16. By contrast, had the intervention not taken place, we would have expected a sum of 362,63. The 95% interval of this prediction is [356,48, 368,68].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,12              23,82          
Prediction (s.d.)        0,11 (0,0023)     21,27 (0,4607) 
95% CI                   [0,1, 0,11]       [20,4, 22,20]  
                                                          
Absolute effect (s.d.)   0,013 (0,0023)    2,544 (0,4607) 
95% CI                   [0,0081, 0,017]   [1,6131, 3,434]
                                                          
Relative effect (s.d.)   12% (2,2%)        12% (2,2%)     
95% CI                   [7,6%, 16%]       [7,6%, 16%]    

Posterior tail-area probability p:   0,00106
Posterior prob. of a causal effect:  99,89429%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,013 with a 95% interval of [0,0081, 0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 23,82. By contrast, had the intervention not taken place, we would have expected a sum of 21,27. The 95% interval of this prediction is [20,38, 22,20].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +12%. The 95% interval of this percentage is [+8%, +16%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,013) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,12              74,17          
Prediction (s.d.)        0,11 (0,0016)     66,39 (1,0220) 
95% CI                   [0,1, 0,11]       [64,3, 68,34]  
                                                          
Absolute effect (s.d.)   0,012 (0,0016)    7,780 (1,0220) 
95% CI                   [0,0093, 0,016]   [5,8320, 9,846]
                                                          
Relative effect (s.d.)   12% (1,5%)        12% (1,5%)     
95% CI                   [8,8%, 15%]       [8,8%, 15%]    

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89463%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,012 with a 95% interval of [0,0093, 0,016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 74,17. By contrast, had the intervention not taken place, we would have expected a sum of 66,39. The 95% interval of this prediction is [64,33, 68,34].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +12%. The 95% interval of this percentage is [+9%, +15%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,012) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,84               168,27          
Prediction (s.d.)        0,87 (0,0082)      174,77 (1,6335) 
95% CI                   [0,86, 0,89]       [171,58, 177,92]
                                                            
Absolute effect (s.d.)   -0,033 (0,0082)    -6,503 (1,6335) 
95% CI                   [-0,048, -0,017]   [-9,651, -3,316]
                                                            
Relative effect (s.d.)   -3,7% (0,93%)      -3,7% (0,93%)   
95% CI                   [-5,5%, -1,9%]     [-5,5%, -1,9%]  

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,8954%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,86, 0,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,033 with a 95% interval of [-0,048, -0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 168,27. By contrast, had the intervention not taken place, we would have expected a sum of 174,77. The 95% interval of this prediction is [171,58, 177,92].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,84               521,18           
Prediction (s.d.)        0,86 (0,0074)      537,74 (4,6202)  
95% CI                   [0,85, 0,88]       [528,77, 546,61] 
                                                             
Absolute effect (s.d.)   -0,027 (0,0074)    -16,560 (4,6202) 
95% CI                   [-0,041, -0,012]   [-25,429, -7,590]
                                                             
Relative effect (s.d.)   -3,1% (0,86%)      -3,1% (0,86%)    
95% CI                   [-4,7%, -1,4%]     [-4,7%, -1,4%]   

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,86. The 95% interval of this counterfactual prediction is [0,85, 0,88]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,027 with a 95% interval of [-0,041, -0,012]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 521,18. By contrast, had the intervention not taken place, we would have expected a sum of 537,74. The 95% interval of this prediction is [528,77, 546,61].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,016                3,122             
Prediction (s.d.)        0,015 (0,00073)      2,980 (0,14636)   
95% CI                   [0,014, 0,016]       [2,706, 3,277]    
                                                                
Absolute effect (s.d.)   0,00071 (0,00073)    0,14225 (0,14636) 
95% CI                   [-0,00078, 0,0021]   [-0,15503, 0,4168]
                                                                
Relative effect (s.d.)   4,8% (4,9%)          4,8% (4,9%)       
95% CI                   [-5,2%, 14%]         [-5,2%, 14%]      

Posterior tail-area probability p:   0,15865
Posterior prob. of a causal effect:  84%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. In the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00071 with a 95% interval of [-0,00078, 0,0021]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,12. Had the intervention not taken place, we would have expected a sum of 2,98. The 95% interval of this prediction is [2,71, 3,28].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +5%. The 95% interval of this percentage is [-5%, +14%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,159. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,016              10,003          
Prediction (s.d.)        0,015 (0,00041)    9,295 (0,25483) 
95% CI                   [0,014, 0,016]     [8,784, 9,793]  
                                                            
Absolute effect (s.d.)   0,0011 (0,00041)   0,7083 (0,25483)
95% CI                   [0,00034, 0,002]   [0,20981, 1,219]
                                                            
Relative effect (s.d.)   7,6% (2,7%)        7,6% (2,7%)     
95% CI                   [2,3%, 13%]        [2,3%, 13%]     

Posterior tail-area probability p:   0,00202
Posterior prob. of a causal effect:  99,79818%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. By contrast, in the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0011 with a 95% interval of [0,00034, 0,0020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 10,00. By contrast, had the intervention not taken place, we would have expected a sum of 9,29. The 95% interval of this prediction is [8,78, 9,79].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +8%. The 95% interval of this percentage is [+2%, +13%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0011) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 1556"
[1] "number of repositories <=-95% top_performer: 98     6,29820051413882 %"
[1] "number of repositories <0 good_performer: 150     9,6401028277635 %"
[1] "number of repositories =0 no_change_with_problems: 1051     67,5449871465296 %"
[1] "number of repositories >0 worst_performer: 257     16,5167095115681 %"
[1] "sum problems added - problems fixed: -429,103523718633"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 244"
[1] "number of repositories <=-95% top_performer: 23     9,42622950819672 %"
[1] "number of repositories <0 good_performer: 13     5,32786885245902 %"
[1] "number of repositories =0 no_change_with_problems: 184     75,4098360655738 %"
[1] "number of repositories >0 worst_performer: 24     9,83606557377049 %"
[1] "sum problems added - problems fixed: -17,8354479444902"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 110"
[1] "number of repositories <=-95% top_performer: 13     11,8181818181818 %"
[1] "number of repositories <0 good_performer: 12     10,9090909090909 %"
[1] "number of repositories =0 no_change_with_problems: 63     57,2727272727273 %"
[1] "number of repositories >0 worst_performer: 22     20 %"
[1] "sum problems added - problems fixed: -17,6140047102229"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 6"
[1] "number of repositories <=-95% top_performer: 1     16,6666666666667 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 3     50 %"
[1] "number of repositories >0 worst_performer: 2     33,3333333333333 %"
[1] "sum problems added - problems fixed: -19,0994579945799"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 566"
[1] "number of repositories <=-95% top_performer: 29     5,12367491166078 %"
[1] "number of repositories <0 good_performer: 31     5,47703180212014 %"
[1] "number of repositories =0 no_change_with_problems: 445     78,6219081272085 %"
[1] "number of repositories >0 worst_performer: 61     10,7773851590106 %"
[1] "sum problems added - problems fixed: -209,270340246217"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 382"
[1] "number of repositories <=-95% top_performer: 25     6,54450261780105 %"
[1] "number of repositories <0 good_performer: 39     10,2094240837696 %"
[1] "number of repositories =0 no_change_with_problems: 250     65,4450261780105 %"
[1] "number of repositories >0 worst_performer: 68     17,8010471204188 %"
[1] "sum problems added - problems fixed: 100,302694646412"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 1115"
[1] "number of repositories <=-95% top_performer: 75     6,72645739910314 %"
[1] "number of repositories <0 good_performer: 96     8,60986547085202 %"
[1] "number of repositories =0 no_change_with_problems: 799     71,6591928251121 %"
[1] "number of repositories >0 worst_performer: 145     13,0044843049327 %"
[1] "sum problems added - problems fixed: -277,10294004428"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 8784"
[1] "number of repos with problems in this 90 day timeframe: 57"
[1] "number of repositories <=-95% top_performer: 8     14,0350877192982 %"
[1] "number of repositories <0 good_performer: 2     3,50877192982456 %"
[1] "number of repositories =0 no_change_with_problems: 29     50,8771929824561 %"
[1] "number of repositories >0 worst_performer: 18     31,5789473684211 %"
[1] "sum problems added - problems fixed: 11,515972574744"
[1] "number of repos with overall problems in this 700 day timeframe: 1244"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 222"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 111"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 11"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 479"
[1] "number of repos with xss problems in this 700 day timeframe: 382"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 872"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 80"
