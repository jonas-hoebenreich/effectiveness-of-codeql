[1] "Log information"
[1] "folder: less_than_5_ontributors"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   1,6                311,6            
Prediction (s.d.)        1,6 (0,014)        321,9 (2,850)    
95% CI                   [1,6, 1,6]         [316,5, 327,7]   
                                                             
Absolute effect (s.d.)   -0,052 (0,014)     -10,376 (2,850)  
95% CI                   [-0,081, -0,025]   [-16,122, -4,911]
                                                             
Relative effect (s.d.)   -3,2% (0,89%)      -3,2% (0,89%)    
95% CI                   [-5%, -1,5%]       [-5%, -1,5%]     

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89827%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,56. By contrast, in the absence of an intervention, we would have expected an average response of 1,61. The 95% interval of this counterfactual prediction is [1,58, 1,64]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,052 with a 95% interval of [-0,081, -0,025]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 311,55. By contrast, had the intervention not taken place, we would have expected a sum of 321,93. The 95% interval of this prediction is [316,46, 327,67].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative        
Actual                   1,5                961,2             
Prediction (s.d.)        1,6 (0,013)        990,5 (7,974)     
95% CI                   [1,6, 1,6]         [975,2, 1006,0]   
                                                              
Absolute effect (s.d.)   -0,047 (0,013)     -29,265 (7,974)   
95% CI                   [-0,072, -0,022]   [-44,776, -13,933]
                                                              
Relative effect (s.d.)   -3% (0,81%)        -3% (0,81%)       
95% CI                   [-4,5%, -1,4%]     [-4,5%, -1,4%]    

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,54. By contrast, in the absence of an intervention, we would have expected an average response of 1,59. The 95% interval of this counterfactual prediction is [1,56, 1,61]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,047 with a 95% interval of [-0,072, -0,022]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 961,25. By contrast, had the intervention not taken place, we would have expected a sum of 990,51. The 95% interval of this prediction is [975,18, 1006,02].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-5%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,2                  40,4              
Prediction (s.d.)        0,21 (0,0015)        41,64 (0,2971)    
95% CI                   [0,21, 0,21]         [41,08, 42,25]    
                                                                
Absolute effect (s.d.)   -0,006 (0,0015)      -1,208 (0,2971)   
95% CI                   [-0,0091, -0,0032]   [-1,8155, -0,6459]
                                                                
Relative effect (s.d.)   -2,9% (0,71%)        -2,9% (0,71%)     
95% CI                   [-4,4%, -1,6%]       [-4,4%, -1,6%]    

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89817%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,20. By contrast, in the absence of an intervention, we would have expected an average response of 0,21. The 95% interval of this counterfactual prediction is [0,21, 0,21]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0060 with a 95% interval of [-0,0091, -0,0032]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 40,44. By contrast, had the intervention not taken place, we would have expected a sum of 41,64. The 95% interval of this prediction is [41,08, 42,25].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-4%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,2                  125,6             
Prediction (s.d.)        0,21 (0,0015)        129,37 (0,9264)   
95% CI                   [0,2, 0,21]          [127,6, 131,16]   
                                                                
Absolute effect (s.d.)   -0,0061 (0,0015)     -3,7787 (0,9264)  
95% CI                   [-0,0089, -0,0031]   [-5,5692, -1,9650]
                                                                
Relative effect (s.d.)   -2,9% (0,72%)        -2,9% (0,72%)     
95% CI                   [-4,3%, -1,5%]       [-4,3%, -1,5%]    

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89899%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,20. By contrast, in the absence of an intervention, we would have expected an average response of 0,21. The 95% interval of this counterfactual prediction is [0,20, 0,21]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0061 with a 95% interval of [-0,0089, -0,0031]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 125,59. By contrast, had the intervention not taken place, we would have expected a sum of 129,37. The 95% interval of this prediction is [127,56, 131,16].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -3%. The 95% interval of this percentage is [-4%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,02                 4,04              
Prediction (s.d.)        0,023 (0,00034)      4,687 (0,06718)   
95% CI                   [0,023, 0,024]       [4,559, 4,823]    
                                                                
Absolute effect (s.d.)   -0,0032 (0,00034)    -0,6497 (0,06718) 
95% CI                   [-0,0039, -0,0026]   [-0,7851, -0,5215]
                                                                
Relative effect (s.d.)   -14% (1,4%)          -14% (1,4%)       
95% CI                   [-17%, -11%]         [-17%, -11%]      

Posterior tail-area probability p:   0,00107
Posterior prob. of a causal effect:  99,89282%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,023. The 95% interval of this counterfactual prediction is [0,023, 0,024]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0032 with a 95% interval of [-0,0039, -0,0026]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 4,04. By contrast, had the intervention not taken place, we would have expected a sum of 4,69. The 95% interval of this prediction is [4,56, 4,82].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -14%. The 95% interval of this percentage is [-17%, -11%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,02                 12,28             
Prediction (s.d.)        0,024 (0,00027)      14,677 (0,16832)  
95% CI                   [0,023, 0,024]       [14,343, 15,000]  
                                                                
Absolute effect (s.d.)   -0,0038 (0,00027)    -2,3934 (0,16832) 
95% CI                   [-0,0044, -0,0033]   [-2,7158, -2,0595]
                                                                
Relative effect (s.d.)   -16% (1,1%)          -16% (1,1%)       
95% CI                   [-19%, -14%]         [-19%, -14%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89889%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,020. By contrast, in the absence of an intervention, we would have expected an average response of 0,024. The 95% interval of this counterfactual prediction is [0,023, 0,024]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0038 with a 95% interval of [-0,0044, -0,0033]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 12,28. By contrast, had the intervention not taken place, we would have expected a sum of 14,68. The 95% interval of this prediction is [14,34, 15,00].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -16%. The 95% interval of this percentage is [-19%, -14%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0028               0,5656            
Prediction (s.d.)        0,0058 (0,00019)     1,1687 (0,03808)  
95% CI                   [0,0055, 0,0062]     [1,1004, 1,2446]  
                                                                
Absolute effect (s.d.)   -0,003 (0,00019)     -0,603 (0,03808)  
95% CI                   [-0,0034, -0,0027]   [-0,6790, -0,5349]
                                                                
Relative effect (s.d.)   -52% (3,3%)          -52% (3,3%)       
95% CI                   [-58%, -46%]         [-58%, -46%]      

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89848%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0028. By contrast, in the absence of an intervention, we would have expected an average response of 0,0058. The 95% interval of this counterfactual prediction is [0,0055, 0,0062]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0030 with a 95% interval of [-0,0034, -0,0027]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,57. By contrast, had the intervention not taken place, we would have expected a sum of 1,17. The 95% interval of this prediction is [1,10, 1,24].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -52%. The 95% interval of this percentage is [-58%, -46%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average              Cumulative        
Actual                   0,0029               1,8036            
Prediction (s.d.)        0,0056 (0,00013)     3,4680 (0,07878)  
95% CI                   [0,0053, 0,0058]     [3,3108, 3,6191]  
                                                                
Absolute effect (s.d.)   -0,0027 (0,00013)    -1,6644 (0,07878) 
95% CI                   [-0,0029, -0,0024]   [-1,8155, -1,5072]
                                                                
Relative effect (s.d.)   -48% (2,3%)          -48% (2,3%)       
95% CI                   [-52%, -43%]         [-52%, -43%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89451%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,0029. By contrast, in the absence of an intervention, we would have expected an average response of 0,0056. The 95% interval of this counterfactual prediction is [0,0053, 0,0058]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,0027 with a 95% interval of [-0,0029, -0,0024]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,80. By contrast, had the intervention not taken place, we would have expected a sum of 3,47. The 95% interval of this prediction is [3,31, 3,62].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -48%. The 95% interval of this percentage is [-52%, -43%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,5                 99,6             
Prediction (s.d.)        0,52 (0,0049)       103,39 (0,9898)  
95% CI                   [0,51, 0,53]        [101,50, 105,43] 
                                                              
Absolute effect (s.d.)   -0,019 (0,0049)     -3,752 (0,9898)  
95% CI                   [-0,029, -0,0093]   [-5,794, -1,8563]
                                                              
Relative effect (s.d.)   -3,6% (0,96%)       -3,6% (0,96%)    
95% CI                   [-5,6%, -1,8%]      [-5,6%, -1,8%]   

Posterior tail-area probability p:   0,00102
Posterior prob. of a causal effect:  99,89817%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,50. By contrast, in the absence of an intervention, we would have expected an average response of 0,52. The 95% interval of this counterfactual prediction is [0,51, 0,53]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,019 with a 95% interval of [-0,029, -0,0093]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 99,64. By contrast, had the intervention not taken place, we would have expected a sum of 103,39. The 95% interval of this prediction is [101,50, 105,43].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,49               306,41           
Prediction (s.d.)        0,51 (0,0051)      319,97 (3,1882)  
95% CI                   [0,5, 0,52]        [313,7, 326,18]  
                                                             
Absolute effect (s.d.)   -0,022 (0,0051)    -13,566 (3,1882) 
95% CI                   [-0,032, -0,012]   [-19,775, -7,287]
                                                             
Relative effect (s.d.)   -4,2% (1%)         -4,2% (1%)       
95% CI                   [-6,2%, -2,3%]     [-6,2%, -2,3%]   

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,49. By contrast, in the absence of an intervention, we would have expected an average response of 0,51. The 95% interval of this counterfactual prediction is [0,50, 0,52]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,022 with a 95% interval of [-0,032, -0,012]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 306,41. By contrast, had the intervention not taken place, we would have expected a sum of 319,97. The 95% interval of this prediction is [313,69, 326,18].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,11             22,13           
Prediction (s.d.)        0,091 (0,0011)   18,169 (0,2196) 
95% CI                   [0,089, 0,093]   [17,739, 18,601]
                                                          
Absolute effect (s.d.)   0,02 (0,0011)    3,96 (0,2196)   
95% CI                   [0,018, 0,022]   [3,528, 4,390]  
                                                          
Relative effect (s.d.)   22% (1,2%)       22% (1,2%)      
95% CI                   [19%, 24%]       [19%, 24%]      

Posterior tail-area probability p:   0,00107
Posterior prob. of a causal effect:  99,89259%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,11. By contrast, in the absence of an intervention, we would have expected an average response of 0,091. The 95% interval of this counterfactual prediction is [0,089, 0,093]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,020 with a 95% interval of [0,018, 0,022]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 22,13. By contrast, had the intervention not taken place, we would have expected a sum of 18,17. The 95% interval of this prediction is [17,74, 18,60].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +22%. The 95% interval of this percentage is [+19%, +24%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,020) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,11             69,45           
Prediction (s.d.)        0,09 (0,0007)    55,93 (0,4399)  
95% CI                   [0,088, 0,091]   [55,070, 56,771]
                                                          
Absolute effect (s.d.)   0,022 (0,0007)   13,522 (0,4399) 
95% CI                   [0,02, 0,023]    [12,68, 14,377] 
                                                          
Relative effect (s.d.)   24% (0,79%)      24% (0,79%)     
95% CI                   [23%, 26%]       [23%, 26%]      

Posterior tail-area probability p:   0,001
Posterior prob. of a causal effect:  99,8999%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,11. By contrast, in the absence of an intervention, we would have expected an average response of 0,090. The 95% interval of this counterfactual prediction is [0,088, 0,091]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,022 with a 95% interval of [0,020, 0,023]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 69,45. By contrast, had the intervention not taken place, we would have expected a sum of 55,93. The 95% interval of this prediction is [55,07, 56,77].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +24%. The 95% interval of this percentage is [+23%, +26%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,022) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,71               141,21          
Prediction (s.d.)        0,74 (0,0076)      147,69 (1,5159) 
95% CI                   [0,72, 0,75]       [144,81, 150,80]
                                                            
Absolute effect (s.d.)   -0,032 (0,0076)    -6,487 (1,5159) 
95% CI                   [-0,048, -0,018]   [-9,593, -3,601]
                                                            
Relative effect (s.d.)   -4,4% (1%)         -4,4% (1%)      
95% CI                   [-6,5%, -2,4%]     [-6,5%, -2,4%]  

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,8954%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,71. By contrast, in the absence of an intervention, we would have expected an average response of 0,74. The 95% interval of this counterfactual prediction is [0,72, 0,75]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,032 with a 95% interval of [-0,048, -0,018]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 141,21. By contrast, had the intervention not taken place, we would have expected a sum of 147,69. The 95% interval of this prediction is [144,81, 150,80].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -4%. The 95% interval of this percentage is [-6%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative        
Actual                   0,7                434,7             
Prediction (s.d.)        0,73 (0,0062)      455,74 (3,8749)   
95% CI                   [0,72, 0,74]       [448,22, 463,20]  
                                                              
Absolute effect (s.d.)   -0,034 (0,0062)    -21,071 (3,8749)  
95% CI                   [-0,046, -0,022]   [-28,534, -13,548]
                                                              
Relative effect (s.d.)   -4,6% (0,85%)      -4,6% (0,85%)     
95% CI                   [-6,3%, -3%]       [-6,3%, -3%]      

Posterior tail-area probability p:   0,00105
Posterior prob. of a causal effect:  99,89451%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,70. By contrast, in the absence of an intervention, we would have expected an average response of 0,73. The 95% interval of this counterfactual prediction is [0,72, 0,74]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,034 with a 95% interval of [-0,046, -0,022]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 434,67. By contrast, had the intervention not taken place, we would have expected a sum of 455,74. The 95% interval of this prediction is [448,22, 463,20].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -5%. The 95% interval of this percentage is [-6%, -3%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,018               3,536            
Prediction (s.d.)        0,017 (0,00081)     3,465 (0,16217)  
95% CI                   [0,016, 0,019]      [3,163, 3,797]   
                                                              
Absolute effect (s.d.)   0,00035 (0,00081)   0,07082 (0,16217)
95% CI                   [-0,0013, 0,0019]   [-0,2616, 0,3727]
                                                              
Relative effect (s.d.)   2% (4,7%)           2% (4,7%)        
95% CI                   [-7,6%, 11%]        [-7,6%, 11%]     

Posterior tail-area probability p:   0,31947
Posterior prob. of a causal effect:  68%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,018. In the absence of an intervention, we would have expected an average response of 0,017. The 95% interval of this counterfactual prediction is [0,016, 0,019]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00035 with a 95% interval of [-0,0013, 0,0019]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,54. Had the intervention not taken place, we would have expected a sum of 3,46. The 95% interval of this prediction is [3,16, 3,80].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +2%. The 95% interval of this percentage is [-8%, +11%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,319. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,018               11,042           
Prediction (s.d.)        0,017 (0,00046)     10,451 (0,28419) 
95% CI                   [0,016, 0,018]      [9,893, 10,998]  
                                                              
Absolute effect (s.d.)   0,00095 (0,00046)   0,59079 (0,28419)
95% CI                   [7,1e-05, 0,0018]   [4,4e-02, 1,1494]
                                                              
Relative effect (s.d.)   5,7% (2,7%)         5,7% (2,7%)      
95% CI                   [0,42%, 11%]        [0,42%, 11%]     

Posterior tail-area probability p:   0,01822
Posterior prob. of a causal effect:  98,178%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,018. By contrast, in the absence of an intervention, we would have expected an average response of 0,017. The 95% interval of this counterfactual prediction is [0,016, 0,018]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00095 with a 95% interval of [0,000071, 0,0018]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 11,04. By contrast, had the intervention not taken place, we would have expected a sum of 10,45. The 95% interval of this prediction is [9,89, 11,00].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +6%. The 95% interval of this percentage is [+0%, +11%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,00095) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,018). This means the causal effect can be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 1082"
[1] "number of repositories <=-95% top_performer: 71     6,56192236598891 %"
[1] "number of repositories <0 good_performer: 87     8,04066543438078 %"
[1] "number of repositories =0 no_change_with_problems: 737     68,1146025878004 %"
[1] "number of repositories >0 worst_performer: 187     17,2828096118299 %"
[1] "sum problems added - problems fixed: -321,813884161074"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 160"
[1] "number of repositories <=-95% top_performer: 17     10,625 %"
[1] "number of repositories <0 good_performer: 8     5 %"
[1] "number of repositories =0 no_change_with_problems: 122     76,25 %"
[1] "number of repositories >0 worst_performer: 13     8,125 %"
[1] "sum problems added - problems fixed: -30,356734992479"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 78"
[1] "number of repositories <=-95% top_performer: 9     11,5384615384615 %"
[1] "number of repositories <0 good_performer: 10     12,8205128205128 %"
[1] "number of repositories =0 no_change_with_problems: 43     55,1282051282051 %"
[1] "number of repositories >0 worst_performer: 16     20,5128205128205 %"
[1] "sum problems added - problems fixed: -18,6763978726161"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 5"
[1] "number of repositories <=-95% top_performer: 1     20 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 2     40 %"
[1] "number of repositories >0 worst_performer: 2     40 %"
[1] "sum problems added - problems fixed: -19,0994579945799"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 391"
[1] "number of repositories <=-95% top_performer: 18     4,60358056265985 %"
[1] "number of repositories <0 good_performer: 21     5,37084398976982 %"
[1] "number of repositories =0 no_change_with_problems: 308     78,772378516624 %"
[1] "number of repositories >0 worst_performer: 44     11,2531969309463 %"
[1] "sum problems added - problems fixed: -142,124609495602"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 231"
[1] "number of repositories <=-95% top_performer: 13     5,62770562770563 %"
[1] "number of repositories <0 good_performer: 21     9,09090909090909 %"
[1] "number of repositories =0 no_change_with_problems: 142     61,4718614718615 %"
[1] "number of repositories >0 worst_performer: 55     23,8095238095238 %"
[1] "sum problems added - problems fixed: 119,412400110491"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 750"
[1] "number of repositories <=-95% top_performer: 54     7,2 %"
[1] "number of repositories <0 good_performer: 54     7,2 %"
[1] "number of repositories =0 no_change_with_problems: 538     71,7333333333333 %"
[1] "number of repositories >0 worst_performer: 104     13,8666666666667 %"
[1] "sum problems added - problems fixed: -240,420612046587"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 6661"
[1] "number of repos with problems in this 90 day timeframe: 40"
[1] "number of repositories <=-95% top_performer: 5     12,5 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 22     55 %"
[1] "number of repositories >0 worst_performer: 13     32,5 %"
[1] "sum problems added - problems fixed: 9,45152813029951"
[1] "number of repos with overall problems in this 700 day timeframe: 685"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 97"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 59"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 5"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 234"
[1] "number of repos with xss problems in this 700 day timeframe: 177"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 455"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 41"
