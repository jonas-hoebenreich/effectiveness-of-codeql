[1] "Log information"
[1] "folder: not_trigger_push"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative     
Actual                   1,7              345,2          
Prediction (s.d.)        1,8 (0,073)      368,0 (14,620) 
95% CI                   [1,7, 2]         [340,6, 398]   
                                                         
Absolute effect (s.d.)   -0,11 (0,073)    -22,82 (14,620)
95% CI                   [-0,26, 0,023]   [-52,70, 4,590]
                                                         
Relative effect (s.d.)   -6,2% (4%)       -6,2% (4%)     
95% CI                   [-14%, 1,2%]     [-14%, 1,2%]   

Posterior tail-area probability p:   0,05726
Posterior prob. of a causal effect:  94%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,73. In the absence of an intervention, we would have expected an average response of 1,84. The 95% interval of this counterfactual prediction is [1,70, 1,99]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,11 with a 95% interval of [-0,26, 0,023]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 345,22. Had the intervention not taken place, we would have expected a sum of 368,04. The 95% interval of this prediction is [340,63, 397,93].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -6%. The 95% interval of this percentage is [-14%, +1%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,057. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative       
Actual                   1,7              1073,1           
Prediction (s.d.)        1,9 (0,089)      1162,1 (55,285)  
95% CI                   [1,7, 2]         [1052,4, 1271]   
                                                           
Absolute effect (s.d.)   -0,14 (0,089)    -89,02 (55,285)  
95% CI                   [-0,32, 0,033]   [-197,73, 20,620]
                                                           
Relative effect (s.d.)   -7,7% (4,8%)     -7,7% (4,8%)     
95% CI                   [-17%, 1,8%]     [-17%, 1,8%]     

Posterior tail-area probability p:   0,05216
Posterior prob. of a causal effect:  95%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 1,72. In the absence of an intervention, we would have expected an average response of 1,86. The 95% interval of this counterfactual prediction is [1,69, 2,04]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,14 with a 95% interval of [-0,32, 0,033]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 1,07K. Had the intervention not taken place, we would have expected a sum of 1,16K. The 95% interval of this prediction is [1,05K, 1,27K].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -8%. The 95% interval of this percentage is [-17%, +2%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,052. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0,18              36,55          
Prediction (s.d.)        0,21 (0,0061)     42,92 (1,2209) 
95% CI                   [0,2, 0,23]       [40,5, 45,41]  
                                                          
Absolute effect (s.d.)   -0,032 (0,0061)   -6,368 (1,2209)
95% CI                   [-0,044, -0,02]   [-8,857, -3,98]
                                                          
Relative effect (s.d.)   -15% (2,8%)       -15% (2,8%)    
95% CI                   [-21%, -9,3%]     [-21%, -9,3%]  

Posterior tail-area probability p:   0,00107
Posterior prob. of a causal effect:  99,89339%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,18. By contrast, in the absence of an intervention, we would have expected an average response of 0,21. The 95% interval of this counterfactual prediction is [0,20, 0,23]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,032 with a 95% interval of [-0,044, -0,020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 36,55. By contrast, had the intervention not taken place, we would have expected a sum of 42,92. The 95% interval of this prediction is [40,54, 45,41].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -15%. The 95% interval of this percentage is [-21%, -9%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,18               111,72           
Prediction (s.d.)        0,22 (0,012)       134,60 (7,225)   
95% CI                   [0,19, 0,24]       [120,20, 148,46] 
                                                             
Absolute effect (s.d.)   -0,037 (0,012)     -22,881 (7,225)  
95% CI                   [-0,059, -0,014]   [-36,740, -8,480]
                                                             
Relative effect (s.d.)   -17% (5,4%)        -17% (5,4%)      
95% CI                   [-27%, -6,3%]      [-27%, -6,3%]    

Posterior tail-area probability p:   0,00302
Posterior prob. of a causal effect:  99,69819%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,18. By contrast, in the absence of an intervention, we would have expected an average response of 0,22. The 95% interval of this counterfactual prediction is [0,19, 0,24]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,037 with a 95% interval of [-0,059, -0,014]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 111,72. By contrast, had the intervention not taken place, we would have expected a sum of 134,60. The 95% interval of this prediction is [120,20, 148,46].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -17%. The 95% interval of this percentage is [-27%, -6%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,003). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,051              10,133          
Prediction (s.d.)        0,043 (0,005)      8,615 (0,999)   
95% CI                   [0,034, 0,053]     [6,714, 10,606] 
                                                            
Absolute effect (s.d.)   0,0076 (0,005)     1,5179 (0,999)  
95% CI                   [-0,0024, 0,017]   [-0,4735, 3,418]
                                                            
Relative effect (s.d.)   18% (12%)          18% (12%)       
95% CI                   [-5,5%, 40%]       [-5,5%, 40%]    

Posterior tail-area probability p:   0,06212
Posterior prob. of a causal effect:  94%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,051. In the absence of an intervention, we would have expected an average response of 0,043. The 95% interval of this counterfactual prediction is [0,034, 0,053]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0076 with a 95% interval of [-0,0024, 0,017]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 10,13. Had the intervention not taken place, we would have expected a sum of 8,61. The 95% interval of this prediction is [6,71, 10,61].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +18%. The 95% interval of this percentage is [-5%, +40%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,062. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,053             33,228          
Prediction (s.d.)        0,042 (0,0019)    26,174 (1,2142) 
95% CI                   [0,038, 0,046]    [23,745, 28,530]
                                                           
Absolute effect (s.d.)   0,011 (0,0019)    7,054 (1,2142)  
95% CI                   [0,0075, 0,015]   [4,6982, 9,483] 
                                                           
Relative effect (s.d.)   27% (4,6%)        27% (4,6%)      
95% CI                   [18%, 36%]        [18%, 36%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,8995%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,053. By contrast, in the absence of an intervention, we would have expected an average response of 0,042. The 95% interval of this counterfactual prediction is [0,038, 0,046]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,011 with a 95% interval of [0,0075, 0,015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 33,23. By contrast, had the intervention not taken place, we would have expected a sum of 26,17. The 95% interval of this prediction is [23,74, 28,53].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +27%. The 95% interval of this percentage is [+18%, +36%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,011) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: stored_xss aggregate function: mean"
[1] "CausalImpact:  mean "
[1] "ERROR collum: stored_xss aggregate function: mean"
List of 2
 $ message: chr "inference was aborted; cannot create plot"
 $ call   : NULL
 - attr(*, "class")= chr [1:4] "assertError" "simpleError" "error" "condition"
[1] "Results for the column: unsafe_jquery_plugin aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average             Cumulative       
Actual                   0,5                 100,0            
Prediction (s.d.)        0,51 (0,0041)       102,14 (0,8101)  
95% CI                   [0,5, 0,52]         [100,6, 103,53]  
                                                              
Absolute effect (s.d.)   -0,011 (0,0041)     -2,103 (0,8101)  
95% CI                   [-0,017, -0,0026]   [-3,495, -0,5231]
                                                              
Relative effect (s.d.)   -2,1% (0,79%)       -2,1% (0,79%)    
95% CI                   [-3,4%, -0,51%]     [-3,4%, -0,51%]  

Posterior tail-area probability p:   0,01754
Posterior prob. of a causal effect:  98,246%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,50. By contrast, in the absence of an intervention, we would have expected an average response of 0,51. The 95% interval of this counterfactual prediction is [0,50, 0,52]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,011 with a 95% interval of [-0,017, -0,0026]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 100,04. By contrast, had the intervention not taken place, we would have expected a sum of 102,14. The 95% interval of this prediction is [100,56, 103,53].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -2%. The 95% interval of this percentage is [-3%, -1%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,018). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   0,5               313,5            
Prediction (s.d.)        0,5 (0,036)       312,9 (22,631)   
95% CI                   [0,43, 0,57]      [268,29, 357,48] 
                                                            
Absolute effect (s.d.)   0,00088 (0,036)   0,55092 (22,631) 
95% CI                   [-0,071, 0,072]   [-44,029, 45,166]
                                                            
Relative effect (s.d.)   0,18% (7,2%)      0,18% (7,2%)     
95% CI                   [-14%, 14%]       [-14%, 14%]      

Posterior tail-area probability p:   0,5005
Posterior prob. of a causal effect:  50%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,50. In the absence of an intervention, we would have expected an average response of 0,50. The 95% interval of this counterfactual prediction is [0,43, 0,57]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00088 with a 95% interval of [-0,071, 0,072]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 313,45. Had the intervention not taken place, we would have expected a sum of 312,90. The 95% interval of this prediction is [268,29, 357,48].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +0%. The 95% interval of this percentage is [-14%, +14%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,501. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,039              7,830           
Prediction (s.d.)        0,033 (0,002)      6,676 (0,404)   
95% CI                   [0,03, 0,038]      [5,90, 7,521]   
                                                            
Absolute effect (s.d.)   0,0058 (0,002)     1,1542 (0,404)  
95% CI                   [0,0015, 0,0096]   [0,3094, 1,9265]
                                                            
Relative effect (s.d.)   17% (6%)           17% (6%)        
95% CI                   [4,6%, 29%]        [4,6%, 29%]     

Posterior tail-area probability p:   0,00305
Posterior prob. of a causal effect:  99,6945%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,039. By contrast, in the absence of an intervention, we would have expected an average response of 0,033. The 95% interval of this counterfactual prediction is [0,030, 0,038]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0058 with a 95% interval of [0,0015, 0,0096]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 7,83. By contrast, had the intervention not taken place, we would have expected a sum of 6,68. The 95% interval of this prediction is [5,90, 7,52].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +17%. The 95% interval of this percentage is [+5%, +29%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0058) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,003). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,036             22,473          
Prediction (s.d.)        0,034 (0,0066)    21,090 (4,1476) 
95% CI                   [0,021, 0,047]    [12,897, 29,099]
                                                           
Absolute effect (s.d.)   0,0022 (0,0066)   1,3826 (4,1476) 
95% CI                   [-0,011, 0,015]   [-6,626, 9,576] 
                                                           
Relative effect (s.d.)   6,6% (20%)        6,6% (20%)      
95% CI                   [-31%, 45%]       [-31%, 45%]     

Posterior tail-area probability p:   0,35807
Posterior prob. of a causal effect:  64%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,036. In the absence of an intervention, we would have expected an average response of 0,034. The 95% interval of this counterfactual prediction is [0,021, 0,047]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0022 with a 95% interval of [-0,011, 0,015]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 22,47. Had the intervention not taken place, we would have expected a sum of 21,09. The 95% interval of this prediction is [12,90, 29,10].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +7%. The 95% interval of this percentage is [-31%, +45%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,358. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,95              190,67          
Prediction (s.d.)        1 (0,049)         209 (9,727)     
95% CI                   [0,95, 1,1]       [189,70, 229,2] 
                                                           
Absolute effect (s.d.)   -0,091 (0,049)    -18,214 (9,727) 
95% CI                   [-0,19, 0,0048]   [-38,57, 0,9659]
                                                           
Relative effect (s.d.)   -8,7% (4,7%)      -8,7% (4,7%)    
95% CI                   [-18%, 0,46%]     [-18%, 0,46%]   

Posterior tail-area probability p:   0,02953
Posterior prob. of a causal effect:  97,047%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,95. In the absence of an intervention, we would have expected an average response of 1,04. The 95% interval of this counterfactual prediction is [0,95, 1,15]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,091 with a 95% interval of [-0,19, 0,0048]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 190,67. Had the intervention not taken place, we would have expected a sum of 208,88. The 95% interval of this prediction is [189,70, 229,24].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -9%. The 95% interval of this percentage is [-18%, +0%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,03). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative        
Actual                   0,95              592,19            
Prediction (s.d.)        1,1 (0,05)        669,3 (31,02)     
95% CI                   [0,97, 1,2]       [607,59, 729,8]   
                                                             
Absolute effect (s.d.)   -0,12 (0,05)      -77,12 (31,02)    
95% CI                   [-0,22, -0,025]   [-137,56, -15,403]
                                                             
Relative effect (s.d.)   -12% (4,6%)       -12% (4,6%)       
95% CI                   [-21%, -2,3%]     [-21%, -2,3%]     

Posterior tail-area probability p:   0,01003
Posterior prob. of a causal effect:  98,997%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,95. By contrast, in the absence of an intervention, we would have expected an average response of 1,07. The 95% interval of this counterfactual prediction is [0,97, 1,17]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,12 with a 95% interval of [-0,22, -0,025]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 592,19. By contrast, had the intervention not taken place, we would have expected a sum of 669,31. The 95% interval of this prediction is [607,59, 729,76].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -12%. The 95% interval of this percentage is [-21%, -2%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,01). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0                 0              
Prediction (s.d.)        -0,0038 (0,024)   -0,7541 (4,784)
95% CI                   [-0,049, 0,045]   [-9,870, 8,919]
                                                          
Absolute effect (s.d.)   0,0038 (0,024)    0,7541 (4,784) 
95% CI                   [-0,045, 0,049]   [-8,919, 9,870]
                                                          
Relative effect (s.d.)   -100% (-634%)     -100% (-634%)  
95% CI                   [1183%, -1309%]   [1183%, -1309%]

Posterior tail-area probability p:   0,43268
Posterior prob. of a causal effect:  57%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of -0,0038. The 95% interval of this counterfactual prediction is [-0,049, 0,045]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0038 with a 95% interval of [-0,045, 0,049]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of -0,75. The 95% interval of this prediction is [-9,87, 8,92].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [+1183%, -1309%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is p = 0,433. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0                  0                
Prediction (s.d.)        -0,00089 (0,012)   -0,55811 (7,226) 
95% CI                   [-0,024, 0,021]    [-15,037, 13,228]
                                                             
Absolute effect (s.d.)   0,00089 (0,012)    0,55811 (7,226)  
95% CI                   [-0,021, 0,024]    [-13,228, 15,037]
                                                             
Relative effect (s.d.)   -100% (-1295%)     -100% (-1295%)   
95% CI                   [2370%, -2694%]    [2370%, -2694%]  

Posterior tail-area probability p:   0,4794
Posterior prob. of a causal effect:  52%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of -0,00089. The 95% interval of this counterfactual prediction is [-0,024, 0,021]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00089 with a 95% interval of [-0,021, 0,024]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of -0,56. The 95% interval of this prediction is [-15,04, 13,23].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [+2370%, -2694%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is p = 0,479. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 37"
[1] "number of repositories <=-95% top_performer: 4     10,8108108108108 %"
[1] "number of repositories <0 good_performer: 2     5,40540540540541 %"
[1] "number of repositories =0 no_change_with_problems: 26     70,2702702702703 %"
[1] "number of repositories >0 worst_performer: 5     13,5135135135135 %"
[1] "sum problems added - problems fixed: -33,7942063492064"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 11"
[1] "number of repositories <=-95% top_performer: 2     18,1818181818182 %"
[1] "number of repositories <0 good_performer: 1     9,09090909090909 %"
[1] "number of repositories =0 no_change_with_problems: 8     72,7272727272727 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -4,9"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 2"
[1] "number of repositories <=-95% top_performer: 1     50 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 1     50 %"
[1] "sum problems added - problems fixed: 0,298412698412698"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 0"
[1] "number of repositories <=-95% top_performer: 0     NaN %"
[1] "number of repositories <0 good_performer: 0     NaN %"
[1] "number of repositories =0 no_change_with_problems: 0     NaN %"
[1] "number of repositories >0 worst_performer: 0     NaN %"
[1] "sum problems added - problems fixed: 0"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 12"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 1     8,33333333333333 %"
[1] "number of repositories =0 no_change_with_problems: 11     91,6666666666667 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -4,75277777777778"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 5"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 1     20 %"
[1] "number of repositories =0 no_change_with_problems: 2     40 %"
[1] "number of repositories >0 worst_performer: 2     40 %"
[1] "sum problems added - problems fixed: 0,702380952380953"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 31"
[1] "number of repositories <=-95% top_performer: 2     6,45161290322581 %"
[1] "number of repositories <0 good_performer: 2     6,45161290322581 %"
[1] "number of repositories =0 no_change_with_problems: 23     74,1935483870968 %"
[1] "number of repositories >0 worst_performer: 4     12,9032258064516 %"
[1] "sum problems added - problems fixed: -25,1422222222222"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 147"
[1] "number of repos with problems in this 90 day timeframe: 0"
[1] "number of repositories <=-95% top_performer: 0     NaN %"
[1] "number of repositories <0 good_performer: 0     NaN %"
[1] "number of repositories =0 no_change_with_problems: 0     NaN %"
[1] "number of repositories >0 worst_performer: 0     NaN %"
[1] "sum problems added - problems fixed: 0"
[1] "number of repos with overall problems in this 700 day timeframe: 31"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 11"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 2"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 0"
[1] "repos_individual_development ERROR collum: stored_xss"
List of 2
 $ message: chr "object 'value' not found"
 $ call   : language FUN(X[[i]], ...)
 - attr(*, "class")= chr [1:3] "simpleError" "error" "condition"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 12"
[1] "number of repos with xss problems in this 700 day timeframe: 8"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 27"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 1"
