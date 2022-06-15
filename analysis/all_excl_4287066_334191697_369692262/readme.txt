[1] "Log information"
[1] "folder: all_excl_4287066_334191697_369692262"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,8                359,9            
Prediction (s.d.)        1,9 (0,015)        371,7 (2,922)    
95% CI                   [1,8, 1,9]         [366,2, 377,7]   
                                                             
Absolute effect (s.d.)   -0,059 (0,015)     -11,794 (2,922)  
95% CI                   [-0,089, -0,031]   [-17,755, -6,286]
                                                             
Relative effect (s.d.)   -3,2% (0,79%)      -3,2% (0,79%)    
95% CI                   [-4,8%, -1,7%]     [-4,8%, -1,7%]   

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89848%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,80. By contrast, in the absence of an intervention, we would have expected an average response of 1,86. The 95% interval of this counterfactual prediction is [1,83, 1,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,059 with a 95% interval of [-0,089, -0,031]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 359,95. By contrast, had the intervention not taken place, we would have expected a sum of 371,74. The 95% interval of this prediction is [366,24, 377,70].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative        
Actual                   1,8                1116,7            
Prediction (s.d.)        1,8 (0,014)        1151,7 (8,819)    
95% CI                   [1,8, 1,9]         [1134,0, 1168,9]  
                                                              
Absolute effect (s.d.)   -0,056 (0,014)     -35,029 (8,819)   
95% CI                   [-0,084, -0,028]   [-52,188, -17,342]
                                                              
Relative effect (s.d.)   -3% (0,77%)        -3% (0,77%)       
95% CI                   [-4,5%, -1,5%]     [-4,5%, -1,5%]    

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89691%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,79. By contrast, in the absence of an intervention, we would have expected an average response of 1,85. The 95% interval of this counterfactual prediction is [1,82, 1,87]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,056 with a 95% interval of [-0,084, -0,028]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,12K. By contrast, had the intervention not taken place, we would have expected a sum of 1,15K. The 95% interval of this prediction is [1,13K, 1,17K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,25                50,76            
Prediction (s.d.)        0,26 (0,0027)       51,15 (0,5452)   
95% CI                   [0,25, 0,26]        [50,09, 52,25]   
                                                              
Absolute effect (s.d.)   -0,0019 (0,0027)    -0,3833 (0,5452) 
95% CI                   [-0,0075, 0,0034]   [-1,4908, 0,6763]
                                                              
Relative effect (s.d.)   -0,75% (1,1%)       -0,75% (1,1%)    
95% CI                   [-2,9%, 1,3%]       [-2,9%, 1,3%]    

Posterior tail-area probability p:   0,23732
Posterior prob. of a causal effect:  76%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,25. In the absence of an intervention, we would have expected an average response of 0,26. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0019 with a 95% interval of [-0,0075, 0,0034]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 50,76. Had the intervention not taken place, we would have expected a sum of 51,15. The 95% interval of this prediction is [50,09, 52,25].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-3%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,237. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,26                159,46           
Prediction (s.d.)        0,25 (0,0028)       158,63 (1,7707)  
95% CI                   [0,25, 0,26]        [155,16, 162,03] 
                                                              
Absolute effect (s.d.)   0,0013 (0,0028)     0,8355 (1,7707)  
95% CI                   [-0,0041, 0,0069]   [-2,5656, 4,3032]
                                                              
Relative effect (s.d.)   0,53% (1,1%)        0,53% (1,1%)     
95% CI                   [-1,6%, 2,7%]       [-1,6%, 2,7%]    

Posterior tail-area probability p:   0,2993
Posterior prob. of a causal effect:  70%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,26. In the absence of an intervention, we would have expected an average response of 0,25. The 95% interval of this counterfactual prediction is [0,25, 0,26]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0013 with a 95% interval of [-0,0041, 0,0069]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 159,46. Had the intervention not taken place, we would have expected a sum of 158,63. The 95% interval of this prediction is [155,16, 162,03].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +1%. The 95% interval of this percentage is [-2%, +3%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,299. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average               Cumulative         
Actual                   0,02                  4,07               
Prediction (s.d.)        0,022 (0,00054)       4,394 (0,10834)    
95% CI                   [0,021, 0,023]        [4,191, 4,616]     
                                                                  
Absolute effect (s.d.)   -0,0016 (0,00054)     -0,3253 (0,10834)  
95% CI                   [-0,0027, -0,00061]   [-0,5469, -0,12248]
                                                                  
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
Actual                   0,021                 13,032             
Prediction (s.d.)        0,022 (0,0004)        13,920 (0,2490)    
95% CI                   [0,022, 0,023]        [13,422, 14,398]   
                                                                  
Absolute effect (s.d.)   -0,0014 (0,0004)      -0,8876 (0,2490)   
95% CI                   [-0,0022, -0,00062]   [-1,3663, -0,38976]
                                                                  
Relative effect (s.d.)   -6,4% (1,8%)          -6,4% (1,8%)       
95% CI                   [-9,8%, -2,8%]        [-9,8%, -2,8%]     

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89868%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,021. By contrast, in the absence of an intervention, we would have expected an average response of 0,022. The 95% interval of this counterfactual prediction is [0,022, 0,023]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0014 with a 95% interval of [-0,0022, -0,00062]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 13,03. By contrast, had the intervention not taken place, we would have expected a sum of 13,92. The 95% interval of this prediction is [13,42, 14,40].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -6%. The 95% interval of this percentage is [-10%, -3%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0024               0,4846            
Prediction (s.d.)        0,0044 (0,00015)     0,8784 (0,02902)  
95% CI                   [0,0041, 0,0047]     [0,8218, 0,9341]  
                                                                
Absolute effect (s.d.)   -0,002 (0,00015)     -0,394 (0,02902)  
95% CI                   [-0,0022, -0,0017]   [-0,4495, -0,3372]
                                                                
Relative effect (s.d.)   -45% (3,3%)          -45% (3,3%)       
95% CI                   [-51%, -38%]         [-51%, -38%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89463%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0024. By contrast, in the absence of an intervention, we would have expected an average response of 0,0044. The 95% interval of this counterfactual prediction is [0,0041, 0,0047]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0020 with a 95% interval of [-0,0022, -0,0017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,48. By contrast, had the intervention not taken place, we would have expected a sum of 0,88. The 95% interval of this prediction is [0,82, 0,93].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -45%. The 95% interval of this percentage is [-51%, -38%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0026               1,5984            
Prediction (s.d.)        0,0043 (0,0001)      2,6555 (0,0653)   
95% CI                   [0,004, 0,0045]      [2,524, 2,7812]   
                                                                
Absolute effect (s.d.)   -0,0017 (0,0001)     -1,0570 (0,0653)  
95% CI                   [-0,0019, -0,0015]   [-1,1828, -0,9256]
                                                                
Relative effect (s.d.)   -40% (2,5%)          -40% (2,5%)       
95% CI                   [-45%, -35%]         [-45%, -35%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89474%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0026. By contrast, in the absence of an intervention, we would have expected an average response of 0,0043. The 95% interval of this counterfactual prediction is [0,0040, 0,0045]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0017 with a 95% interval of [-0,0019, -0,0015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,60. By contrast, had the intervention not taken place, we would have expected a sum of 2,66. The 95% interval of this prediction is [2,52, 2,78].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -40%. The 95% interval of this percentage is [-45%, -35%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,56                112,61           
Prediction (s.d.)        0,58 (0,0042)       116,16 (0,8363)  
95% CI                   [0,57, 0,59]        [114,55, 117,90] 
                                                              
Absolute effect (s.d.)   -0,018 (0,0042)     -3,548 (0,8363)  
95% CI                   [-0,026, -0,0097]   [-5,289, -1,9412]
                                                              
Relative effect (s.d.)   -3,1% (0,72%)       -3,1% (0,72%)    
95% CI                   [-4,6%, -1,7%]      [-4,6%, -1,7%]   

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89744%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,58. The 95% interval of this counterfactual prediction is [0,57, 0,59]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,018 with a 95% interval of [-0,026, -0,0097]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 112,61. By contrast, had the intervention not taken place, we would have expected a sum of 116,16. The 95% interval of this prediction is [114,55, 117,90].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,56               347,67           
Prediction (s.d.)        0,58 (0,0049)      361,91 (3,0831)  
95% CI                   [0,57, 0,59]       [355,77, 367,92] 
                                                             
Absolute effect (s.d.)   -0,023 (0,0049)    -14,238 (3,0831) 
95% CI                   [-0,032, -0,013]   [-20,256, -8,098]
                                                             
Relative effect (s.d.)   -3,9% (0,85%)      -3,9% (0,85%)    
95% CI                   [-5,6%, -2,2%]     [-5,6%, -2,2%]   

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,56. By contrast, in the absence of an intervention, we would have expected an average response of 0,58. The 95% interval of this counterfactual prediction is [0,57, 0,59]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,023 with a 95% interval of [-0,032, -0,013]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 347,67. By contrast, had the intervention not taken place, we would have expected a sum of 361,91. The 95% interval of this prediction is [355,77, 367,92].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,1                  20,3              
Prediction (s.d.)        0,1 (0,0021)         21,0 (0,4290)     
95% CI                   [0,1, 0,11]          [20,1, 21,85]     
                                                                
Absolute effect (s.d.)   -0,0032 (0,0021)     -0,6500 (0,4290)  
95% CI                   [-0,0077, 0,00096]   [-1,5325, 0,19266]
                                                                
Relative effect (s.d.)   -3,1% (2%)           -3,1% (2%)        
95% CI                   [-7,3%, 0,92%]       [-7,3%, 0,92%]    

Posterior tail-area probability p:   0,05779
Posterior prob. of a causal effect:  94%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,10. In the absence of an intervention, we would have expected an average response of 0,10. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0032 with a 95% interval of [-0,0077, 0,00096]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 20,32. Had the intervention not taken place, we would have expected a sum of 20,97. The 95% interval of this prediction is [20,13, 21,85].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-7%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,058. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,1                  62,8              
Prediction (s.d.)        0,11 (0,0016)        65,70 (1,0003)    
95% CI                   [0,1, 0,11]          [63,7, 67,61]     
                                                                
Absolute effect (s.d.)   -0,0047 (0,0016)     -2,9331 (1,0003)  
95% CI                   [-0,0078, -0,0016]   [-4,8435, -0,9752]
                                                                
Relative effect (s.d.)   -4,5% (1,5%)         -4,5% (1,5%)      
95% CI                   [-7,4%, -1,5%]       [-7,4%, -1,5%]    

Posterior tail-area probability p:   0,00719
Posterior prob. of a causal effect:  99,28058%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,10. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,10, 0,11]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0047 with a 95% interval of [-0,0078, -0,0016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 62,77. By contrast, had the intervention not taken place, we would have expected a sum of 65,70. The 95% interval of this prediction is [63,74, 67,61].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-7%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,007). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,84               168,63          
Prediction (s.d.)        0,87 (0,0079)      174,97 (1,5741) 
95% CI                   [0,86, 0,89]       [172,02, 178,02]
                                                            
Absolute effect (s.d.)   -0,032 (0,0079)    -6,336 (1,5741) 
95% CI                   [-0,047, -0,017]   [-9,391, -3,388]
                                                            
Relative effect (s.d.)   -3,6% (0,9%)       -3,6% (0,9%)    
95% CI                   [-5,4%, -1,9%]     [-5,4%, -1,9%]  

Posterior tail-area probability p:   0,00104
Posterior prob. of a causal effect:  99,89594%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,86, 0,89]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,032 with a 95% interval of [-0,047, -0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 168,63. By contrast, had the intervention not taken place, we would have expected a sum of 174,97. The 95% interval of this prediction is [172,02, 178,02].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,84               522,33           
Prediction (s.d.)        0,87 (0,0073)      539,81 (4,5718)  
95% CI                   [0,85, 0,88]       [530,90, 548,63] 
                                                             
Absolute effect (s.d.)   -0,028 (0,0073)    -17,483 (4,5718) 
95% CI                   [-0,042, -0,014]   [-26,297, -8,575]
                                                             
Relative effect (s.d.)   -3,2% (0,85%)      -3,2% (0,85%)    
95% CI                   [-4,9%, -1,6%]     [-4,9%, -1,6%]   

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89785%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,84. By contrast, in the absence of an intervention, we would have expected an average response of 0,87. The 95% interval of this counterfactual prediction is [0,85, 0,88]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,028 with a 95% interval of [-0,042, -0,014]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 522,33. By contrast, had the intervention not taken place, we would have expected a sum of 539,81. The 95% interval of this prediction is [530,90, 548,63].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,015               3,072            
Prediction (s.d.)        0,015 (0,00094)     2,944 (0,18730)  
95% CI                   [0,013, 0,017]      [2,595, 3,330]   
                                                              
Absolute effect (s.d.)   0,00064 (0,00094)   0,12782 (0,18730)
95% CI                   [-0,0013, 0,0024]   [-0,2589, 0,4762]
                                                              
Relative effect (s.d.)   4,3% (6,4%)         4,3% (6,4%)      
95% CI                   [-8,8%, 16%]        [-8,8%, 16%]     

Posterior tail-area probability p:   0,23046
Posterior prob. of a causal effect:  77%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,015. In the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,013, 0,017]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00064 with a 95% interval of [-0,0013, 0,0024]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,07. Had the intervention not taken place, we would have expected a sum of 2,94. The 95% interval of this prediction is [2,60, 3,33].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +4%. The 95% interval of this percentage is [-9%, +16%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,23. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,016               9,841            
Prediction (s.d.)        0,015 (0,00051)     9,148 (0,31528)  
95% CI                   [0,014, 0,016]      [8,530, 9,755]   
                                                              
Absolute effect (s.d.)   0,0011 (0,00051)    0,6926 (0,31528) 
95% CI                   [0,00014, 0,0021]   [0,08522, 1,3102]
                                                              
Relative effect (s.d.)   7,6% (3,4%)         7,6% (3,4%)      
95% CI                   [0,93%, 14%]        [0,93%, 14%]     

Posterior tail-area probability p:   0,01104
Posterior prob. of a causal effect:  98,896%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,016. By contrast, in the absence of an intervention, we would have expected an average response of 0,015. The 95% interval of this counterfactual prediction is [0,014, 0,016]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0011 with a 95% interval of [0,00014, 0,0021]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 9,84. By contrast, had the intervention not taken place, we would have expected a sum of 9,15. The 95% interval of this prediction is [8,53, 9,76].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +8%. The 95% interval of this percentage is [+1%, +14%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0011) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,011). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 1591"
[1] "number of repositories <=-95% top_performer: 102     6,41106222501571 %"
[1] "number of repositories <0 good_performer: 152     9,55373978629792 %"
[1] "number of repositories =0 no_change_with_problems: 1077     67,6932746700189 %"
[1] "number of repositories >0 worst_performer: 260     16,3419233186675 %"
[1] "sum problems added - problems fixed: -575,442174512284"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 255"
[1] "number of repositories <=-95% top_performer: 25     9,80392156862745 %"
[1] "number of repositories <0 good_performer: 14     5,49019607843137 %"
[1] "number of repositories =0 no_change_with_problems: 192     75,2941176470588 %"
[1] "number of repositories >0 worst_performer: 24     9,41176470588235 %"
[1] "sum problems added - problems fixed: -22,7354479444902"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 112"
[1] "number of repositories <=-95% top_performer: 14     12,5 %"
[1] "number of repositories <0 good_performer: 12     10,7142857142857 %"
[1] "number of repositories =0 no_change_with_problems: 63     56,25 %"
[1] "number of repositories >0 worst_performer: 23     20,5357142857143 %"
[1] "sum problems added - problems fixed: -17,3155920118102"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 6"
[1] "number of repositories <=-95% top_performer: 1     16,6666666666667 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 3     50 %"
[1] "number of repositories >0 worst_performer: 2     33,3333333333333 %"
[1] "sum problems added - problems fixed: -19,0994579945799"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 578"
[1] "number of repositories <=-95% top_performer: 29     5,01730103806228 %"
[1] "number of repositories <0 good_performer: 32     5,5363321799308 %"
[1] "number of repositories =0 no_change_with_problems: 456     78,8927335640138 %"
[1] "number of repositories >0 worst_performer: 61     10,5536332179931 %"
[1] "sum problems added - problems fixed: -214,023118023994"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 385"
[1] "number of repositories <=-95% top_performer: 25     6,49350649350649 %"
[1] "number of repositories <0 good_performer: 40     10,3896103896104 %"
[1] "number of repositories =0 no_change_with_problems: 252     65,4545454545455 %"
[1] "number of repositories >0 worst_performer: 68     17,6623376623377 %"
[1] "sum problems added - problems fixed: -11,3949244012069"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 1145"
[1] "number of repositories <=-95% top_performer: 77     6,72489082969432 %"
[1] "number of repositories <0 good_performer: 98     8,5589519650655 %"
[1] "number of repositories =0 no_change_with_problems: 822     71,7903930131004 %"
[1] "number of repositories >0 worst_performer: 148     12,9257641921397 %"
[1] "sum problems added - problems fixed: -302,389606710946"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 8929"
[1] "number of repos with problems in this 90 day timeframe: 57"
[1] "number of repositories <=-95% top_performer: 8     14,0350877192982 %"
[1] "number of repositories <0 good_performer: 2     3,50877192982456 %"
[1] "number of repositories =0 no_change_with_problems: 29     50,8771929824561 %"
[1] "number of repositories >0 worst_performer: 18     31,5789473684211 %"
[1] "sum problems added - problems fixed: 11,515972574744"
[1] "number of repos with overall problems in this 700 day timeframe: 1273"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 233"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 113"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 11"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 491"
[1] "number of repos with xss problems in this 700 day timeframe: 388"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 898"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 81"
