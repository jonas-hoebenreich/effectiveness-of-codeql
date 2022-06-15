[1] "Log information"
[1] "folder: not_weekly"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   1,6               312,2           
Prediction (s.d.)        1,5 (0,02)        303,6 (3,93)    
95% CI                   [1,5, 1,6]        [296,1, 311,2]  
                                                           
Absolute effect (s.d.)   0,043 (0,02)      8,617 (3,93)    
95% CI                   [0,0049, 0,081]   [0,9811, 16,121]
                                                           
Relative effect (s.d.)   2,8% (1,3%)       2,8% (1,3%)     
95% CI                   [0,32%, 5,3%]     [0,32%, 5,3%]   

Posterior tail-area probability p:   0,01515
Posterior prob. of a causal effect:  98,485%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,56. By contrast, in the absence of an intervention, we would have expected an average response of 1,52. The 95% interval of this counterfactual prediction is [1,48, 1,56]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,043 with a 95% interval of [0,0049, 0,081]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 312,19. By contrast, had the intervention not taken place, we would have expected a sum of 303,58. The 95% interval of this prediction is [296,07, 311,21].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +3%. The 95% interval of this percentage is [+0%, +5%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,043) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,015). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   1,5               945,7            
Prediction (s.d.)        1,5 (0,024)       952,1 (15,078)   
95% CI                   [1,5, 1,6]        [922,0, 981,3]   
                                                            
Absolute effect (s.d.)   -0,01 (0,024)     -6,42 (15,078)   
95% CI                   [-0,057, 0,038]   [-35,672, 23,623]
                                                            
Relative effect (s.d.)   -0,67% (1,6%)     -0,67% (1,6%)    
95% CI                   [-3,7%, 2,5%]     [-3,7%, 2,5%]    

Posterior tail-area probability p:   0,334
Posterior prob. of a causal effect:  67%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,52. In the absence of an intervention, we would have expected an average response of 1,53. The 95% interval of this counterfactual prediction is [1,48, 1,57]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,010 with a 95% interval of [-0,057, 0,038]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 945,65. Had the intervention not taken place, we would have expected a sum of 952,07. The 95% interval of this prediction is [922,03, 981,32].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -1%. The 95% interval of this percentage is [-4%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,334. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,16               32,28           
Prediction (s.d.)        0,16 (0,0012)      31,51 (0,2377)  
95% CI                   [0,16, 0,16]       [31,05, 31,98]  
                                                            
Absolute effect (s.d.)   0,0039 (0,0012)    0,7721 (0,2377) 
95% CI                   [0,0015, 0,0061]   [0,2959, 1,2270]
                                                            
Relative effect (s.d.)   2,5% (0,75%)       2,5% (0,75%)    
95% CI                   [0,94%, 3,9%]      [0,94%, 3,9%]   

Posterior tail-area probability p:   0,00204
Posterior prob. of a causal effect:  99,79571%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,16. By contrast, in the absence of an intervention, we would have expected an average response of 0,16. The 95% interval of this counterfactual prediction is [0,16, 0,16]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0039 with a 95% interval of [0,0015, 0,0061]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 32,28. By contrast, had the intervention not taken place, we would have expected a sum of 31,51. The 95% interval of this prediction is [31,05, 31,98].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +2%. The 95% interval of this percentage is [+1%, +4%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0039) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,16                96,94            
Prediction (s.d.)        0,16 (0,0024)       98,93 (1,5136)   
95% CI                   [0,15, 0,16]        [95,94, 101,84]  
                                                              
Absolute effect (s.d.)   -0,0032 (0,0024)    -1,9895 (1,5136) 
95% CI                   [-0,0078, 0,0016]   [-4,8963, 1,0094]
                                                              
Relative effect (s.d.)   -2% (1,5%)          -2% (1,5%)       
95% CI                   [-4,9%, 1%]         [-4,9%, 1%]      

Posterior tail-area probability p:   0,09027
Posterior prob. of a causal effect:  91%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,16. In the absence of an intervention, we would have expected an average response of 0,16. The 95% interval of this counterfactual prediction is [0,15, 0,16]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0032 with a 95% interval of [-0,0078, 0,0016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 96,94. Had the intervention not taken place, we would have expected a sum of 98,93. The 95% interval of this prediction is [95,94, 101,84].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-5%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,09. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,035              7,083           
Prediction (s.d.)        0,034 (0,0019)     6,792 (0,3731)  
95% CI                   [0,03, 0,038]      [6,08, 7,523]   
                                                            
Absolute effect (s.d.)   0,0015 (0,0019)    0,2913 (0,3731) 
95% CI                   [-0,0022, 0,005]   [-0,4402, 1,004]
                                                            
Relative effect (s.d.)   4,3% (5,5%)        4,3% (5,5%)     
95% CI                   [-6,5%, 15%]       [-6,5%, 15%]    

Posterior tail-area probability p:   0,23009
Posterior prob. of a causal effect:  77%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,035. In the absence of an intervention, we would have expected an average response of 0,034. The 95% interval of this counterfactual prediction is [0,030, 0,038]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0015 with a 95% interval of [-0,0022, 0,0050]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 7,08. Had the intervention not taken place, we would have expected a sum of 6,79. The 95% interval of this prediction is [6,08, 7,52].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +4%. The 95% interval of this percentage is [-6%, +15%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,23. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,037              23,231          
Prediction (s.d.)        0,033 (0,00093)    20,502 (0,58335)
95% CI                   [0,031, 0,035]     [19,326, 21,643]
                                                            
Absolute effect (s.d.)   0,0044 (0,00093)   2,7292 (0,58335)
95% CI                   [0,0025, 0,0063]   [1,5886, 3,9050]
                                                            
Relative effect (s.d.)   13% (2,8%)         13% (2,8%)      
95% CI                   [7,7%, 19%]        [7,7%, 19%]     

Posterior tail-area probability p:   0,00104
Posterior prob. of a causal effect:  99,89562%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,037. By contrast, in the absence of an intervention, we would have expected an average response of 0,033. The 95% interval of this counterfactual prediction is [0,031, 0,035]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0044 with a 95% interval of [0,0025, 0,0063]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 23,23. By contrast, had the intervention not taken place, we would have expected a sum of 20,50. The 95% interval of this prediction is [19,33, 21,64].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +13%. The 95% interval of this percentage is [+8%, +19%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0044) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,0025              0,5025           
Prediction (s.d.)        0,0022 (0,0017)     0,4406 (0,3427)  
95% CI                   [-0,0011, 0,0057]   [-0,2249, 1,1488]
                                                              
Absolute effect (s.d.)   0,00031 (0,0017)    0,06192 (0,3427) 
95% CI                   [-0,0032, 0,0036]   [-0,6463, 0,7274]
                                                              
Relative effect (s.d.)   14% (78%)           14% (78%)        
95% CI                   [-147%, 165%]       [-147%, 165%]    

Posterior tail-area probability p:   0,42782
Posterior prob. of a causal effect:  57%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0025. In the absence of an intervention, we would have expected an average response of 0,0022. The 95% interval of this counterfactual prediction is [-0,0011, 0,0057]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00031 with a 95% interval of [-0,0032, 0,0036]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,50. Had the intervention not taken place, we would have expected a sum of 0,44. The 95% interval of this prediction is [-0,22, 1,15].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +14%. The 95% interval of this percentage is [-147%, +165%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,428. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,0025              1,5678           
Prediction (s.d.)        0,0024 (0,00094)    1,5157 (0,58557) 
95% CI                   [0,00052, 0,0043]   [0,32755, 2,6752]
                                                              
Absolute effect (s.d.)   8,4e-05 (0,00094)   5,2e-02 (0,58557)
95% CI                   [-0,0018, 0,002]    [-1,1074, 1,240] 
                                                              
Relative effect (s.d.)   3,4% (39%)          3,4% (39%)       
95% CI                   [-73%, 82%]         [-73%, 82%]      

Posterior tail-area probability p:   0,4662
Posterior prob. of a causal effect:  53%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0025. In the absence of an intervention, we would have expected an average response of 0,0024. The 95% interval of this counterfactual prediction is [0,00052, 0,0043]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,000084 with a 95% interval of [-0,0018, 0,0020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,57. Had the intervention not taken place, we would have expected a sum of 1,52. The 95% interval of this prediction is [0,33, 2,68].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +3%. The 95% interval of this percentage is [-73%, +82%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,466. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,52             104,06          
Prediction (s.d.)        0,44 (0,0036)    88,78 (0,7102)  
95% CI                   [0,44, 0,45]     [87,45, 90,20]  
                                                          
Absolute effect (s.d.)   0,076 (0,0036)   15,288 (0,7102) 
95% CI                   [0,069, 0,083]   [13,867, 16,610]
                                                          
Relative effect (s.d.)   17% (0,8%)       17% (0,8%)      
95% CI                   [16%, 19%]       [16%, 19%]      

Posterior tail-area probability p:   0,00107
Posterior prob. of a causal effect:  99,8927%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,52. By contrast, in the absence of an intervention, we would have expected an average response of 0,44. The 95% interval of this counterfactual prediction is [0,44, 0,45]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,076 with a 95% interval of [0,069, 0,083]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 104,06. By contrast, had the intervention not taken place, we would have expected a sum of 88,78. The 95% interval of this prediction is [87,45, 90,20].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +17%. The 95% interval of this percentage is [+16%, +19%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,076) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,49             307,86          
Prediction (s.d.)        0,45 (0,012)     279,29 (7,253)  
95% CI                   [0,42, 0,47]     [264,79, 293,59]
                                                          
Absolute effect (s.d.)   0,046 (0,012)    28,568 (7,253)  
95% CI                   [0,023, 0,069]   [14,271, 43,075]
                                                          
Relative effect (s.d.)   10% (2,6%)       10% (2,6%)      
95% CI                   [5,1%, 15%]      [5,1%, 15%]     

Posterior tail-area probability p:   0,00104
Posterior prob. of a causal effect:  99,89616%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,49. By contrast, in the absence of an intervention, we would have expected an average response of 0,45. The 95% interval of this counterfactual prediction is [0,42, 0,47]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,046 with a 95% interval of [0,023, 0,069]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 307,86. By contrast, had the intervention not taken place, we would have expected a sum of 279,29. The 95% interval of this prediction is [264,79, 293,59].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +10%. The 95% interval of this percentage is [+5%, +15%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,046) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,078               15,656           
Prediction (s.d.)        0,09 (0,0046)       18,08 (0,9228)   
95% CI                   [0,082, 0,1]        [16,381, 19,9]   
                                                              
Absolute effect (s.d.)   -0,012 (0,0046)     -2,424 (0,9228)  
95% CI                   [-0,021, -0,0036]   [-4,282, -0,7251]
                                                              
Relative effect (s.d.)   -13% (5,1%)         -13% (5,1%)      
95% CI                   [-24%, -4%]         [-24%, -4%]      

Posterior tail-area probability p:   0,00202
Posterior prob. of a causal effect:  99,79757%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,078. By contrast, in the absence of an intervention, we would have expected an average response of 0,090. The 95% interval of this counterfactual prediction is [0,082, 0,100]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,012 with a 95% interval of [-0,021, -0,0036]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 15,66. By contrast, had the intervention not taken place, we would have expected a sum of 18,08. The 95% interval of this prediction is [16,38, 19,94].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -13%. The 95% interval of this percentage is [-24%, -4%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   0,067             42,114           
Prediction (s.d.)        0,091 (0,0035)    56,920 (2,1668)  
95% CI                   [0,084, 0,098]    [52,601, 61,061] 
                                                            
Absolute effect (s.d.)   -0,024 (0,0035)   -14,805 (2,1668) 
95% CI                   [-0,03, -0,017]   [-18,95, -10,487]
                                                            
Relative effect (s.d.)   -26% (3,8%)       -26% (3,8%)      
95% CI                   [-33%, -18%]      [-33%, -18%]     

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8994%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,067. By contrast, in the absence of an intervention, we would have expected an average response of 0,091. The 95% interval of this counterfactual prediction is [0,084, 0,098]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,024 with a 95% interval of [-0,030, -0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 42,11. By contrast, had the intervention not taken place, we would have expected a sum of 56,92. The 95% interval of this prediction is [52,60, 61,06].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -26%. The 95% interval of this percentage is [-33%, -18%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,76              152,43          
Prediction (s.d.)        0,8 (0,011)       160,3 (2,144)   
95% CI                   [0,78, 0,82]      [155,99, 164,49]
                                                           
Absolute effect (s.d.)   -0,039 (0,011)    -7,884 (2,144)  
95% CI                   [-0,06, -0,018]   [-12,06, -3,561]
                                                           
Relative effect (s.d.)   -4,9% (1,3%)      -4,9% (1,3%)    
95% CI                   [-7,5%, -2,2%]    [-7,5%, -2,2%]  

Posterior tail-area probability p:   0,00203
Posterior prob. of a causal effect:  99,79654%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,76. By contrast, in the absence of an intervention, we would have expected an average response of 0,80. The 95% interval of this counterfactual prediction is [0,78, 0,82]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,039 with a 95% interval of [-0,060, -0,018]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 152,43. By contrast, had the intervention not taken place, we would have expected a sum of 160,32. The 95% interval of this prediction is [155,99, 164,49].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -5%. The 95% interval of this percentage is [-8%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative        
Actual                   0,76                473,59            
Prediction (s.d.)        0,79 (0,014)        495,11 (8,756)    
95% CI                   [0,77, 0,82]        [477,62, 511,99]  
                                                               
Absolute effect (s.d.)   -0,034 (0,014)      -21,519 (8,756)   
95% CI                   [-0,062, -0,0065]   [-38,396, -4,0299]
                                                               
Relative effect (s.d.)   -4,3% (1,8%)        -4,3% (1,8%)      
95% CI                   [-7,8%, -0,81%]     [-7,8%, -0,81%]   

Posterior tail-area probability p:   0,01103
Posterior prob. of a causal effect:  98,897%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,76. By contrast, in the absence of an intervention, we would have expected an average response of 0,79. The 95% interval of this counterfactual prediction is [0,77, 0,82]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,034 with a 95% interval of [-0,062, -0,0065]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 473,59. By contrast, had the intervention not taken place, we would have expected a sum of 495,11. The 95% interval of this prediction is [477,62, 511,99].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-8%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,011). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,00089            0,17839         
Prediction (s.d.)        -0,0025 (0,0086)   -0,5083 (1,7260)
95% CI                   [-0,019, 0,015]    [-3,864, 3,052] 
                                                            
Absolute effect (s.d.)   0,0034 (0,0086)    0,6867 (1,7260) 
95% CI                   [-0,014, 0,02]     [-2,874, 4,04]  
                                                            
Relative effect (s.d.)   -135% (-340%)      -135% (-340%)   
95% CI                   [565%, -795%]      [565%, -795%]   

Posterior tail-area probability p:   0,33648
Posterior prob. of a causal effect:  66%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00089. By contrast, in the absence of an intervention, we would have expected an average response of -0,0025. The 95% interval of this counterfactual prediction is [-0,019, 0,015]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0034 with a 95% interval of [-0,014, 0,020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,18. By contrast, had the intervention not taken place, we would have expected a sum of -0,51. The 95% interval of this prediction is [-3,86, 3,05].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -135%. The 95% interval of this percentage is [+565%, -795%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is p = 0,336. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,00054             0,33794          
Prediction (s.d.)        -0,00047 (0,0043)   -0,29162 (2,6809)
95% CI                   [-0,0091, 0,0078]   [-5,6662, 4,8969]
                                                              
Absolute effect (s.d.)   0,001 (0,0043)      0,630 (2,6809)   
95% CI                   [-0,0073, 0,0096]   [-4,5589, 6,0041]
                                                              
Relative effect (s.d.)   -216% (-919%)       -216% (-919%)    
95% CI                   [1563%, -2059%]     [1563%, -2059%]  

Posterior tail-area probability p:   0,40644
Posterior prob. of a causal effect:  59%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00054. By contrast, in the absence of an intervention, we would have expected an average response of -0,00047. The 95% interval of this counterfactual prediction is [-0,0091, 0,0078]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0010 with a 95% interval of [-0,0073, 0,0096]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,34. By contrast, had the intervention not taken place, we would have expected a sum of -0,29. The 95% interval of this prediction is [-5,67, 4,90].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -216%. The 95% interval of this percentage is [+1563%, -2059%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is p = 0,406. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 65"
[1] "number of repositories <=-95% top_performer: 4     6,15384615384615 %"
[1] "number of repositories <0 good_performer: 14     21,5384615384615 %"
[1] "number of repositories =0 no_change_with_problems: 42     64,6153846153846 %"
[1] "number of repositories >0 worst_performer: 5     7,69230769230769 %"
[1] "sum problems added - problems fixed: -22,4584824508134"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 16"
[1] "number of repositories <=-95% top_performer: 1     6,25 %"
[1] "number of repositories <0 good_performer: 1     6,25 %"
[1] "number of repositories =0 no_change_with_problems: 11     68,75 %"
[1] "number of repositories >0 worst_performer: 3     18,75 %"
[1] "sum problems added - problems fixed: -0,345679012345678"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 7"
[1] "number of repositories <=-95% top_performer: 2     28,5714285714286 %"
[1] "number of repositories <0 good_performer: 1     14,2857142857143 %"
[1] "number of repositories =0 no_change_with_problems: 3     42,8571428571429 %"
[1] "number of repositories >0 worst_performer: 1     14,2857142857143 %"
[1] "sum problems added - problems fixed: -1,91269841269841"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 1     100 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: 0"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 19"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 2     10,5263157894737 %"
[1] "number of repositories =0 no_change_with_problems: 15     78,9473684210526 %"
[1] "number of repositories >0 worst_performer: 2     10,5263157894737 %"
[1] "sum problems added - problems fixed: 7,61851851851852"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 17"
[1] "number of repositories <=-95% top_performer: 1     5,88235294117647 %"
[1] "number of repositories <0 good_performer: 4     23,5294117647059 %"
[1] "number of repositories =0 no_change_with_problems: 11     64,7058823529412 %"
[1] "number of repositories >0 worst_performer: 1     5,88235294117647 %"
[1] "sum problems added - problems fixed: -2,73650793650794"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 48"
[1] "number of repositories <=-95% top_performer: 4     8,33333333333333 %"
[1] "number of repositories <0 good_performer: 9     18,75 %"
[1] "number of repositories =0 no_change_with_problems: 32     66,6666666666667 %"
[1] "number of repositories >0 worst_performer: 3     6,25 %"
[1] "sum problems added - problems fixed: -25,0821156077799"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 398"
[1] "number of repos with problems in this 90 day timeframe: 0"
[1] "number of repositories <=-95% top_performer: 0     NaN %"
[1] "number of repositories <0 good_performer: 0     NaN %"
[1] "number of repositories =0 no_change_with_problems: 0     NaN %"
[1] "number of repositories >0 worst_performer: 0     NaN %"
[1] "sum problems added - problems fixed: 0"
[1] "number of repos with overall problems in this 700 day timeframe: 73"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 13"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 8"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 1"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 22"
[1] "number of repos with xss problems in this 700 day timeframe: 20"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 59"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 7"
