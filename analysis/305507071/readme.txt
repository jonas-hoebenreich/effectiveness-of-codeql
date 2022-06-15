[1] "Log information"
[1] "folder: 305507071"
[1] 1
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n      and p.gid = 305507071\n"
[1] 305507071
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   11             2214            
Prediction (s.d.)        93 (3,2)       18654 (632,8)   
95% CI                   [88, 100]      [17514, 20000]  
                                                        
Absolute effect (s.d.)   -82 (3,2)      -16440 (632,8)  
95% CI                   [-89, -77]     [-17786, -15300]
                                                        
Relative effect (s.d.)   -88% (3,4%)    -88% (3,4%)     
95% CI                   [-95%, -82%]   [-95%, -82%]    

Posterior tail-area probability p:   0,00107
Posterior prob. of a causal effect:  99,8927%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 11,07. By contrast, in the absence of an intervention, we would have expected an average response of 93,27. The 95% interval of this counterfactual prediction is [87,57, 100,00]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -82,20 with a 95% interval of [-88,93, -76,50]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 2,21K. By contrast, had the intervention not taken place, we would have expected a sum of 18,65K. The 95% interval of this prediction is [17,51K, 20,00K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -88%. The 95% interval of this percentage is [-95%, -82%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average         Cumulative      
Actual                   11              6876            
Prediction (s.d.)        93 (5,7)        58071 (3576,8)  
95% CI                   [81, 104]       [50638, 64754]  
                                                         
Absolute effect (s.d.)   -82 (5,7)       -51195 (3576,8) 
95% CI                   [-93, -70]      [-57878, -43762]
                                                         
Relative effect (s.d.)   -88% (6,2%)     -88% (6,2%)     
95% CI                   [-100%, -75%]   [-100%, -75%]   

Posterior tail-area probability p:   0,00196
Posterior prob. of a causal effect:  99,80392%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 11,02. By contrast, in the absence of an intervention, we would have expected an average response of 93,06. The 95% interval of this counterfactual prediction is [81,15, 103,77]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -82,04 with a 95% interval of [-92,75, -70,13]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 6,88K. By contrast, had the intervention not taken place, we would have expected a sum of 58,07K. The 95% interval of this prediction is [50,64K, 64,75K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -88%. The 95% interval of this percentage is [-100%, -75%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average         Cumulative      
Actual                   0               0               
Prediction (s.d.)        1,8 (0,026)     365,9 (5,292)   
95% CI                   [1,8, 1,9]      [355,6, 376,4]  
                                                         
Absolute effect (s.d.)   -1,8 (0,026)    -365,9 (5,292)  
95% CI                   [-1,9, -1,8]    [-376,4, -355,6]
                                                         
Relative effect (s.d.)   -100% (1,4%)    -100% (1,4%)    
95% CI                   [-103%, -97%]   [-103%, -97%]   

Posterior tail-area probability p:   0,00108
Posterior prob. of a causal effect:  99,89236%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 1,83. The 95% interval of this counterfactual prediction is [1,78, 1,88]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -1,83 with a 95% interval of [-1,88, -1,78]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 365,94. The 95% interval of this prediction is [355,62, 376,42].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-103%, -97%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average         Cumulative       
Actual                   0               0                
Prediction (s.d.)        1,8 (0,17)      1104,1 (105,36)  
95% CI                   [1,4, 2,1]      [887,1, 1300,7]  
                                                          
Absolute effect (s.d.)   -1,8 (0,17)     -1104,1 (105,36) 
95% CI                   [-2,1, -1,4]    [-1300,7, -887,1]
                                                          
Relative effect (s.d.)   -100% (9,5%)    -100% (9,5%)     
95% CI                   [-118%, -80%]   [-118%, -80%]    

Posterior tail-area probability p:   0,00174
Posterior prob. of a causal effect:  99,82609%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 1,77. The 95% interval of this counterfactual prediction is [1,42, 2,08]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -1,77 with a 95% interval of [-2,08, -1,42]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 1104,13. The 95% interval of this prediction is [887,11, 1300,73].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-118%, -80%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
[1] "ERROR collum: reflected_xss aggregate function: mean"
List of 2
 $ message: chr "inference was aborted; cannot create plot"
 $ call   : NULL
 - attr(*, "class")= chr [1:4] "assertError" "simpleError" "error" "condition"
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average         Cumulative    
Actual                   0               0             
Prediction (s.d.)        20 (0,87)       3904 (173,58) 
95% CI                   [18, 21]        [3563, 4258]  
                                                       
Absolute effect (s.d.)   -20 (0,87)      -3904 (173,58)
95% CI                   [-21, -18]      [-4258, -3563]
                                                       
Relative effect (s.d.)   -100% (4,4%)    -100% (4,4%)  
95% CI                   [-109%, -91%]   [-109%, -91%] 

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89474%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 19,52. The 95% interval of this counterfactual prediction is [17,81, 21,29]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -19,52 with a 95% interval of [-21,29, -17,81]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 3904,20. The 95% interval of this prediction is [3562,51, 4258,11].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-109%, -91%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average         Cumulative      
Actual                   0               0               
Prediction (s.d.)        19 (0,79)       12093 (495,36)  
95% CI                   [18, 21]        [11126, 13049]  
                                                         
Absolute effect (s.d.)   -19 (0,79)      -12093 (495,36) 
95% CI                   [-21, -18]      [-13049, -11126]
                                                         
Relative effect (s.d.)   -100% (4,1%)    -100% (4,1%)    
95% CI                   [-108%, -92%]   [-108%, -92%]   

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89733%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 19,38. The 95% interval of this counterfactual prediction is [17,83, 20,91]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -19,38 with a 95% interval of [-20,91, -17,83]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 12093,36. The 95% interval of this prediction is [11126,07, 13049,29].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-108%, -92%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average         Cumulative    
Actual                   0               0             
Prediction (s.d.)        16 (0,24)       3293 (47,24)  
95% CI                   [16, 17]        [3197, 3388]  
                                                       
Absolute effect (s.d.)   -16 (0,24)      -3293 (47,24) 
95% CI                   [-17, -16]      [-3388, -3197]
                                                       
Relative effect (s.d.)   -100% (1,4%)    -100% (1,4%)  
95% CI                   [-103%, -97%]   [-103%, -97%] 

Posterior tail-area probability p:   0,00108
Posterior prob. of a causal effect:  99,89236%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 16,47. The 95% interval of this counterfactual prediction is [15,98, 16,94]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -16,47 with a 95% interval of [-16,94, -15,98]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 3293,44. The 95% interval of this prediction is [3196,98, 3387,83].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-103%, -97%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average         Cumulative     
Actual                   0               0              
Prediction (s.d.)        16 (1,4)        9907 (904,2)   
95% CI                   [13, 19]        [8068, 11578]  
                                                        
Absolute effect (s.d.)   -16 (1,4)       -9907 (904,2)  
95% CI                   [-19, -13]      [-11578, -8068]
                                                        
Relative effect (s.d.)   -100% (9,1%)    -100% (9,1%)   
95% CI                   [-117%, -81%]   [-117%, -81%]  

Posterior tail-area probability p:   0,00161
Posterior prob. of a causal effect:  99,83897%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 15,88. The 95% interval of this counterfactual prediction is [12,93, 18,55]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -15,88 with a 95% interval of [-18,55, -12,93]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 9907,22. The 95% interval of this prediction is [8067,86, 11577,95].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-117%, -81%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average         Cumulative    
Actual                   3               600           
Prediction (s.d.)        26 (2)          5153 (405)    
95% CI                   [22, 29]        [4346, 5892]  
                                                       
Absolute effect (s.d.)   -23 (2)         -4553 (405)   
95% CI                   [-26, -19]      [-5292, -3746]
                                                       
Relative effect (s.d.)   -88% (7,9%)     -88% (7,9%)   
95% CI                   [-103%, -73%]   [-103%, -73%] 

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89507%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 3,00. By contrast, in the absence of an intervention, we would have expected an average response of 25,76. The 95% interval of this counterfactual prediction is [21,73, 29,46]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -22,76 with a 95% interval of [-26,46, -18,73]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 600,00. By contrast, had the intervention not taken place, we would have expected a sum of 5152,99. The 95% interval of this prediction is [4346,12, 5891,70].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -88%. The 95% interval of this percentage is [-103%, -73%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   3              1872            
Prediction (s.d.)        22 (1)         13955 (631)     
95% CI                   [20, 24]       [12685, 15157]  
                                                        
Absolute effect (s.d.)   -19 (1)        -12083 (631)    
95% CI                   [-21, -17]     [-13285, -10813]
                                                        
Relative effect (s.d.)   -87% (4,5%)    -87% (4,5%)     
95% CI                   [-95%, -77%]   [-95%, -77%]    

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 3,00. By contrast, in the absence of an intervention, we would have expected an average response of 22,36. The 95% interval of this counterfactual prediction is [20,33, 24,29]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -19,36 with a 95% interval of [-21,29, -17,33]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,87K. By contrast, had the intervention not taken place, we would have expected a sum of 13,95K. The 95% interval of this prediction is [12,68K, 15,16K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -87%. The 95% interval of this percentage is [-95%, -77%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average        Cumulative    
Actual                   8,1            1614,0        
Prediction (s.d.)        32 (1,3)       6488 (251,8)  
95% CI                   [30, 35]       [6014, 6985]  
                                                      
Absolute effect (s.d.)   -24 (1,3)      -4874 (251,8) 
95% CI                   [-27, -22]     [-5371, -4400]
                                                      
Relative effect (s.d.)   -75% (3,9%)    -75% (3,9%)   
95% CI                   [-83%, -68%]   [-83%, -68%]  

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89712%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 8,07. By contrast, in the absence of an intervention, we would have expected an average response of 32,44. The 95% interval of this counterfactual prediction is [30,07, 34,93]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -24,37 with a 95% interval of [-26,86, -22,00]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,61K. By contrast, had the intervention not taken place, we would have expected a sum of 6,49K. The 95% interval of this prediction is [6,01K, 6,99K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -75%. The 95% interval of this percentage is [-83%, -68%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   8              5004            
Prediction (s.d.)        32 (2,9)       19871 (1815,6)  
95% CI                   [26, 37]       [16091, 23277]  
                                                        
Absolute effect (s.d.)   -24 (2,9)      -14867 (1815,6) 
95% CI                   [-29, -18]     [-18273, -11087]
                                                        
Relative effect (s.d.)   -75% (9,1%)    -75% (9,1%)     
95% CI                   [-92%, -56%]   [-92%, -56%]    

Posterior tail-area probability p:   0,00216
Posterior prob. of a causal effect:  99,78448%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 8,02. By contrast, in the absence of an intervention, we would have expected an average response of 31,84. The 95% interval of this counterfactual prediction is [25,79, 37,30]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -23,82 with a 95% interval of [-29,28, -17,77]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 5,00K. By contrast, had the intervention not taken place, we would have expected a sum of 19,87K. The 95% interval of this prediction is [16,09K, 23,28K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -75%. The 95% interval of this percentage is [-92%, -56%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
[1] "ERROR collum: xss_through_exception aggregate function: mean"
List of 2
 $ message: chr "inference was aborted; cannot create plot"
 $ call   : NULL
 - attr(*, "class")= chr [1:4] "assertError" "simpleError" "error" "condition"
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 1     100 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -87,6888888888889"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 1     100 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -2"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 0"
[1] "number of repositories <=-95% top_performer: 0     NaN %"
[1] "number of repositories <0 good_performer: 0     NaN %"
[1] "number of repositories =0 no_change_with_problems: 0     NaN %"
[1] "number of repositories >0 worst_performer: 0     NaN %"
[1] "sum problems added - problems fixed: 0"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 1     100 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -20"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 1     100 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -18"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 1     100 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -20"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 1     100 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -27,6888888888889"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 1"
[1] "number of repos with problems in this 90 day timeframe: 0"
[1] "number of repositories <=-95% top_performer: 0     NaN %"
[1] "number of repositories <0 good_performer: 0     NaN %"
[1] "number of repositories =0 no_change_with_problems: 0     NaN %"
[1] "number of repositories >0 worst_performer: 0     NaN %"
[1] "sum problems added - problems fixed: 0"
[1] "number of repos with overall problems in this 700 day timeframe: 1"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 1"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 0"
[1] "repos_individual_development ERROR collum: reflected_xss"
List of 2
 $ message: chr "object 'value' not found"
 $ call   : language FUN(X[[i]], ...)
 - attr(*, "class")= chr [1:3] "simpleError" "error" "condition"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 1"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 1"
[1] "number of repos with xss problems in this 700 day timeframe: 1"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 1"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 0"
[1] "repos_individual_development ERROR collum: xss_through_exception"
List of 2
 $ message: chr "object 'value' not found"
 $ call   : language FUN(X[[i]], ...)
 - attr(*, "class")= chr [1:3] "simpleError" "error" "condition"
