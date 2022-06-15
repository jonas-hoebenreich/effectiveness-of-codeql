[1] "Log information"
[1] "folder: best_performing"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   4,6            915,6           
Prediction (s.d.)        6,8 (0,25)     1362,0 (49,86)  
95% CI                   [6,3, 7,3]     [1266,6, 1467,7]
                                                        
Absolute effect (s.d.)   -2,2 (0,25)    -446,4 (49,86)  
95% CI                   [-2,8, -1,8]   [-552,1, -351,0]
                                                        
Relative effect (s.d.)   -33% (3,7%)    -33% (3,7%)     
95% CI                   [-41%, -26%]   [-41%, -26%]    

Posterior tail-area probability p:   0,00104
Posterior prob. of a causal effect:  99,89648%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 4,58. By contrast, in the absence of an intervention, we would have expected an average response of 6,81. The 95% interval of this counterfactual prediction is [6,33, 7,34]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -2,23 with a 95% interval of [-2,76, -1,75]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 915,61. By contrast, had the intervention not taken place, we would have expected a sum of 1361,98. The 95% interval of this prediction is [1266,56, 1467,67].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -33%. The 95% interval of this percentage is [-41%, -26%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   4,4            2766,3          
Prediction (s.d.)        7,1 (0,18)     4422,6 (113,83) 
95% CI                   [6,7, 7,4]     [4198,9, 4643,1]
                                                        
Absolute effect (s.d.)   -2,7 (0,18)    -1656,2 (113,83)
95% CI                   [-3, -2,3]     [-1877, -1432,6]
                                                        
Relative effect (s.d.)   -37% (2,6%)    -37% (2,6%)     
95% CI                   [-42%, -32%]   [-42%, -32%]    

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89879%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 4,43. By contrast, in the absence of an intervention, we would have expected an average response of 7,09. The 95% interval of this counterfactual prediction is [6,73, 7,44]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -2,65 with a 95% interval of [-3,01, -2,30]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 2,77K. By contrast, had the intervention not taken place, we would have expected a sum of 4,42K. The 95% interval of this prediction is [4,20K, 4,64K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -37%. The 95% interval of this percentage is [-42%, -32%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   0,47              93,65            
Prediction (s.d.)        0,61 (0,027)      121,59 (5,306)   
95% CI                   [0,55, 0,66]      [110,99, 131,65] 
                                                            
Absolute effect (s.d.)   -0,14 (0,027)     -27,94 (5,306)   
95% CI                   [-0,19, -0,087]   [-38,00, -17,345]
                                                            
Relative effect (s.d.)   -23% (4,4%)       -23% (4,4%)      
95% CI                   [-31%, -14%]      [-31%, -14%]     

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89796%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,47. By contrast, in the absence of an intervention, we would have expected an average response of 0,61. The 95% interval of this counterfactual prediction is [0,55, 0,66]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,14 with a 95% interval of [-0,19, -0,087]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 93,65. By contrast, had the intervention not taken place, we would have expected a sum of 121,59. The 95% interval of this prediction is [110,99, 131,65].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -23%. The 95% interval of this percentage is [-31%, -14%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative       
Actual                   0,46             288,58           
Prediction (s.d.)        0,65 (0,022)     405,63 (13,699)  
95% CI                   [0,61, 0,69]     [378,26, 432,19] 
                                                           
Absolute effect (s.d.)   -0,19 (0,022)    -117,05 (13,699) 
95% CI                   [-0,23, -0,14]   [-143,62, -89,68]
                                                           
Relative effect (s.d.)   -29% (3,4%)      -29% (3,4%)      
95% CI                   [-35%, -22%]     [-35%, -22%]     

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8995%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,46. By contrast, in the absence of an intervention, we would have expected an average response of 0,65. The 95% interval of this counterfactual prediction is [0,61, 0,69]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,19 with a 95% interval of [-0,23, -0,14]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 288,58. By contrast, had the intervention not taken place, we would have expected a sum of 405,63. The 95% interval of this prediction is [378,26, 432,19].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -29%. The 95% interval of this percentage is [-35%, -22%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   0,078             15,651           
Prediction (s.d.)        0,18 (0,012)      35,78 (2,359)    
95% CI                   [0,16, 0,2]       [31,17, 40,7]    
                                                            
Absolute effect (s.d.)   -0,1 (0,012)      -20,1 (2,359)    
95% CI                   [-0,13, -0,078]   [-25,02, -15,520]
                                                            
Relative effect (s.d.)   -56% (6,6%)       -56% (6,6%)      
95% CI                   [-70%, -43%]      [-70%, -43%]     

Posterior tail-area probability p:   0,00106
Posterior prob. of a causal effect:  99,89407%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,078. By contrast, in the absence of an intervention, we would have expected an average response of 0,18. The 95% interval of this counterfactual prediction is [0,16, 0,20]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,10 with a 95% interval of [-0,13, -0,078]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 15,65. By contrast, had the intervention not taken place, we would have expected a sum of 35,78. The 95% interval of this prediction is [31,17, 40,67].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -56%. The 95% interval of this percentage is [-70%, -43%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,081            50,770          
Prediction (s.d.)        0,2 (0,0067)     122,1 (4,1841)  
95% CI                   [0,18, 0,21]     [113,75, 130,14]
                                                          
Absolute effect (s.d.)   -0,11 (0,0067)   -71,30 (4,1841) 
95% CI                   [-0,13, -0,1]    [-79,37, -63,0] 
                                                          
Relative effect (s.d.)   -58% (3,4%)      -58% (3,4%)     
95% CI                   [-65%, -52%]     [-65%, -52%]    

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89899%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,081. By contrast, in the absence of an intervention, we would have expected an average response of 0,20. The 95% interval of this counterfactual prediction is [0,18, 0,21]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,11 with a 95% interval of [-0,13, -0,10]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 50,77. By contrast, had the intervention not taken place, we would have expected a sum of 122,07. The 95% interval of this prediction is [113,75, 130,14].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -58%. The 95% interval of this percentage is [-65%, -52%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0                  0                
Prediction (s.d.)        0,047 (0,0027)     9,323 (0,5379)   
95% CI                   [0,041, 0,052]     [8,260, 10,403]  
                                                             
Absolute effect (s.d.)   -0,047 (0,0027)    -9,323 (0,5379)  
95% CI                   [-0,052, -0,041]   [-10,403, -8,260]
                                                             
Relative effect (s.d.)   -100% (5,8%)       -100% (5,8%)     
95% CI                   [-112%, -89%]      [-112%, -89%]    

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89817%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 0,047. The 95% interval of this counterfactual prediction is [0,041, 0,052]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,047 with a 95% interval of [-0,052, -0,041]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 9,32. The 95% interval of this prediction is [8,26, 10,40].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-112%, -89%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative        
Actual                   0                  0                 
Prediction (s.d.)        0,047 (0,0022)     29,254 (1,4024)   
95% CI                   [0,042, 0,051]     [26,518, 31,950]  
                                                              
Absolute effect (s.d.)   -0,047 (0,0022)    -29,254 (1,4024)  
95% CI                   [-0,051, -0,042]   [-31,950, -26,518]
                                                              
Relative effect (s.d.)   -100% (4,8%)       -100% (4,8%)      
95% CI                   [-109%, -91%]      [-109%, -91%]     

Posterior tail-area probability p:   0,00106
Posterior prob. of a causal effect:  99,89429%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of 0,047. The 95% interval of this counterfactual prediction is [0,042, 0,051]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,047 with a 95% interval of [-0,051, -0,042]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of 29,25. The 95% interval of this prediction is [26,52, 31,95].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [-109%, -91%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average         Cumulative      
Actual                   1,5             297,6           
Prediction (s.d.)        2,1 (0,088)     411,0 (17,579)  
95% CI                   [1,9, 2,2]      [376,7, 447,3]  
                                                         
Absolute effect (s.d.)   -0,57 (0,088)   -113,43 (17,579)
95% CI                   [-0,75, -0,4]   [-149,72, -79,2]
                                                         
Relative effect (s.d.)   -28% (4,3%)     -28% (4,3%)     
95% CI                   [-36%, -19%]    [-36%, -19%]    

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89785%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,49. By contrast, in the absence of an intervention, we would have expected an average response of 2,05. The 95% interval of this counterfactual prediction is [1,88, 2,24]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,57 with a 95% interval of [-0,75, -0,40]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 297,55. By contrast, had the intervention not taken place, we would have expected a sum of 410,98. The 95% interval of this prediction is [376,73, 447,27].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -28%. The 95% interval of this percentage is [-36%, -19%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average         Cumulative       
Actual                   1,5             909,2            
Prediction (s.d.)        2,2 (0,069)     1365,5 (42,890)  
95% CI                   [2,1, 2,3]      [1281,2, 1449,0] 
                                                          
Absolute effect (s.d.)   -0,73 (0,069)   -456,33 (42,890) 
95% CI                   [-0,87, -0,6]   [-539,82, -372,0]
                                                          
Relative effect (s.d.)   -33% (3,1%)     -33% (3,1%)      
95% CI                   [-40%, -27%]    [-40%, -27%]     

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89868%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,46. By contrast, in the absence of an intervention, we would have expected an average response of 2,19. The 95% interval of this counterfactual prediction is [2,05, 2,32]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,73 with a 95% interval of [-0,87, -0,60]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 909,18. By contrast, had the intervention not taken place, we would have expected a sum of 1365,52. The 95% interval of this prediction is [1281,19, 1449,00].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -33%. The 95% interval of this percentage is [-40%, -27%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   0,13              26,45            
Prediction (s.d.)        0,29 (0,032)      57,40 (6,491)    
95% CI                   [0,22, 0,35]      [44,98, 70,72]   
                                                            
Absolute effect (s.d.)   -0,15 (0,032)     -30,95 (6,491)   
95% CI                   [-0,22, -0,093]   [-44,28, -18,531]
                                                            
Relative effect (s.d.)   -54% (11%)        -54% (11%)       
95% CI                   [-77%, -32%]      [-77%, -32%]     

Posterior tail-area probability p:   0,00104
Posterior prob. of a causal effect:  99,89583%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,13. By contrast, in the absence of an intervention, we would have expected an average response of 0,29. The 95% interval of this counterfactual prediction is [0,22, 0,35]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,15 with a 95% interval of [-0,22, -0,093]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 26,45. By contrast, had the intervention not taken place, we would have expected a sum of 57,40. The 95% interval of this prediction is [44,98, 70,72].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -54%. The 95% interval of this percentage is [-77%, -32%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative        
Actual                   0,12             74,41             
Prediction (s.d.)        0,33 (0,021)     207,68 (13,026)   
95% CI                   [0,29, 0,37]     [181,71, 232,98]  
                                                            
Absolute effect (s.d.)   -0,21 (0,021)    -133,27 (13,026)  
95% CI                   [-0,25, -0,17]   [-158,57, -107,29]
                                                            
Relative effect (s.d.)   -64% (6,3%)      -64% (6,3%)       
95% CI                   [-76%, -52%]     [-76%, -52%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89909%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. By contrast, in the absence of an intervention, we would have expected an average response of 0,33. The 95% interval of this counterfactual prediction is [0,29, 0,37]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,21 with a 95% interval of [-0,25, -0,17]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 74,41. By contrast, had the intervention not taken place, we would have expected a sum of 207,68. The 95% interval of this prediction is [181,71, 232,98].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -64%. The 95% interval of this percentage is [-76%, -52%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average         Cumulative       
Actual                   2,4             477,6            
Prediction (s.d.)        3,5 (0,13)      694,3 (26,04)    
95% CI                   [3,2, 3,7]      [643,3, 746,9]   
                                                          
Absolute effect (s.d.)   -1,1 (0,13)     -216,6 (26,04)   
95% CI                   [-1,3, -0,83]   [-269,3, -165,69]
                                                          
Relative effect (s.d.)   -31% (3,8%)     -31% (3,8%)      
95% CI                   [-39%, -24%]    [-39%, -24%]     

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89796%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 2,39. By contrast, in the absence of an intervention, we would have expected an average response of 3,47. The 95% interval of this counterfactual prediction is [3,22, 3,73]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -1,08 with a 95% interval of [-1,35, -0,83]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 477,63. By contrast, had the intervention not taken place, we would have expected a sum of 694,26. The 95% interval of this prediction is [643,32, 746,89].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -31%. The 95% interval of this percentage is [-39%, -24%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average        Cumulative      
Actual                   2,3            1426,1          
Prediction (s.d.)        3,6 (0,091)    2254,1 (56,585) 
95% CI                   [3,4, 3,8]     [2143,0, 2363,8]
                                                        
Absolute effect (s.d.)   -1,3 (0,091)   -828,0 (56,585) 
95% CI                   [-1,5, -1,1]   [-937,7, -716,9]
                                                        
Relative effect (s.d.)   -37% (2,5%)    -37% (2,5%)     
95% CI                   [-42%, -32%]   [-42%, -32%]    

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8994%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 2,29. By contrast, in the absence of an intervention, we would have expected an average response of 3,61. The 95% interval of this counterfactual prediction is [3,43, 3,79]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -1,33 with a 95% interval of [-1,50, -1,15]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,43K. By contrast, had the intervention not taken place, we would have expected a sum of 2,25K. The 95% interval of this prediction is [2,14K, 2,36K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -37%. The 95% interval of this percentage is [-42%, -32%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,023              4,685            
Prediction (s.d.)        0,028 (0,018)      5,578 (3,680)    
95% CI                   [-0,0065, 0,066]   [-1,2903, 13,190]
                                                             
Absolute effect (s.d.)   -0,0045 (0,018)    -0,8932 (3,680)  
95% CI                   [-0,043, 0,03]     [-8,506, 5,98]   
                                                             
Relative effect (s.d.)   -16% (66%)         -16% (66%)       
95% CI                   [-152%, 107%]      [-152%, 107%]    

Posterior tail-area probability p:   0,40745
Posterior prob. of a causal effect:  59%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,023. In the absence of an intervention, we would have expected an average response of 0,028. The 95% interval of this counterfactual prediction is [-0,0065, 0,066]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0045 with a 95% interval of [-0,043, 0,030]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 4,68. Had the intervention not taken place, we would have expected a sum of 5,58. The 95% interval of this prediction is [-1,29, 13,19].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -16%. The 95% interval of this percentage is [-152%, +107%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,407. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative         
Actual                   0,028                17,309             
Prediction (s.d.)        0,047 (0,0096)       29,468 (6,0076)    
95% CI                   [0,028, 0,066]       [17,466, 40,962]   
                                                                 
Absolute effect (s.d.)   -0,019 (0,0096)      -12,159 (6,0076)   
95% CI                   [-0,038, -0,00025]   [-23,654, -0,15725]
                                                                 
Relative effect (s.d.)   -41% (20%)           -41% (20%)         
95% CI                   [-80%, -0,53%]       [-80%, -0,53%]     

Posterior tail-area probability p:   0,02319
Posterior prob. of a causal effect:  97,681%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,028. By contrast, in the absence of an intervention, we would have expected an average response of 0,047. The 95% interval of this counterfactual prediction is [0,028, 0,066]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,019 with a 95% interval of [-0,038, -0,00025]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 17,31. By contrast, had the intervention not taken place, we would have expected a sum of 29,47. The 95% interval of this prediction is [17,47, 40,96].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -41%. The 95% interval of this percentage is [-80%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,023). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 303"
[1] "number of repositories <=-95% top_performer: 99     32,6732673267327 %"
[1] "number of repositories <0 good_performer: 116     38,2838283828383 %"
[1] "number of repositories =0 no_change_with_problems: 80     26,4026402640264 %"
[1] "number of repositories >0 worst_performer: 8     2,64026402640264 %"
[1] "sum problems added - problems fixed: -1159,21795938255"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 61"
[1] "number of repositories <=-95% top_performer: 25     40,9836065573771 %"
[1] "number of repositories <0 good_performer: 11     18,0327868852459 %"
[1] "number of repositories =0 no_change_with_problems: 24     39,344262295082 %"
[1] "number of repositories >0 worst_performer: 1     1,63934426229508 %"
[1] "sum problems added - problems fixed: -93,5813144342791"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 30"
[1] "number of repositories <=-95% top_performer: 12     40 %"
[1] "number of repositories <0 good_performer: 9     30 %"
[1] "number of repositories =0 no_change_with_problems: 7     23,3333333333333 %"
[1] "number of repositories >0 worst_performer: 2     6,66666666666667 %"
[1] "sum problems added - problems fixed: -48,3013431013431"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 1     100 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -20"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 110"
[1] "number of repositories <=-95% top_performer: 29     26,3636363636364 %"
[1] "number of repositories <0 good_performer: 31     28,1818181818182 %"
[1] "number of repositories =0 no_change_with_problems: 50     45,4545454545455 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -354,483359718936"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 67"
[1] "number of repositories <=-95% top_performer: 25     37,3134328358209 %"
[1] "number of repositories <0 good_performer: 24     35,8208955223881 %"
[1] "number of repositories =0 no_change_with_problems: 14     20,8955223880597 %"
[1] "number of repositories >0 worst_performer: 4     5,97014925373134 %"
[1] "sum problems added - problems fixed: -81,9806847346042"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 223"
[1] "number of repositories <=-95% top_performer: 71     31,8385650224215 %"
[1] "number of repositories <0 good_performer: 76     34,0807174887892 %"
[1] "number of repositories =0 no_change_with_problems: 72     32,2869955156951 %"
[1] "number of repositories >0 worst_performer: 4     1,79372197309417 %"
[1] "sum problems added - problems fixed: -550,135701837836"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 410"
[1] "number of repos with problems in this 90 day timeframe: 11"
[1] "number of repositories <=-95% top_performer: 6     54,5454545454545 %"
[1] "number of repositories <0 good_performer: 2     18,1818181818182 %"
[1] "number of repositories =0 no_change_with_problems: 2     18,1818181818182 %"
[1] "number of repositories >0 worst_performer: 1     9,09090909090909 %"
[1] "sum problems added - problems fixed: -10,7355555555556"
[1] "number of repos with overall problems in this 700 day timeframe: 410"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 94"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 44"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 3"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 163"
[1] "number of repos with xss problems in this 700 day timeframe: 119"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 283"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 35"
