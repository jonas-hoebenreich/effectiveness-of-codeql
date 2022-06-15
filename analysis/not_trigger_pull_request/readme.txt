[1] "Log information"
[1] "folder: not_trigger_pull_request"
[1] 0
[1] "\n   \t\t  p.status = 1\n      and pm.fork is false\n      and c.scans_javascript = 1\n      and a.timediff < 0 and a.timediff >= -43200000\n      and p.gid in (select distinct gid from Analysis_TABLE a1 where timediff >= 0 and timediff <= 17280000)\n      and deleted_at is null\n      and p.gid not in (4287066, 334191697, 369692262)\n"
list()
[1] "Results for the column: overall aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,69             138,13          
Prediction (s.d.)        0,76 (0,055)     151,41 (11,048) 
95% CI                   [0,65, 0,87]     [130,26, 173,78]
                                                          
Absolute effect (s.d.)   -0,066 (0,055)   -13,280 (11,048)
95% CI                   [-0,18, 0,039]   [-35,66, 7,864] 
                                                          
Relative effect (s.d.)   -8,8% (7,3%)     -8,8% (7,3%)    
95% CI                   [-24%, 5,2%]     [-24%, 5,2%]    

Posterior tail-area probability p:   0,10972
Posterior prob. of a causal effect:  89%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,69. In the absence of an intervention, we would have expected an average response of 0,76. The 95% interval of this counterfactual prediction is [0,65, 0,87]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,066 with a 95% interval of [-0,18, 0,039]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 138,13. Had the intervention not taken place, we would have expected a sum of 151,41. The 95% interval of this prediction is [130,26, 173,78].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -9%. The 95% interval of this percentage is [-24%, +5%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,11. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative      
Actual                   0,71             440,76          
Prediction (s.d.)        0,76 (0,092)     474,89 (57,441) 
95% CI                   [0,58, 0,94]     [360,75, 586,08]
                                                          
Absolute effect (s.d.)   -0,055 (0,092)   -34,131 (57,441)
95% CI                   [-0,23, 0,13]    [-145,32, 80,01]
                                                          
Relative effect (s.d.)   -7,2% (12%)      -7,2% (12%)     
95% CI                   [-31%, 17%]      [-31%, 17%]     

Posterior tail-area probability p:   0,27024
Posterior prob. of a causal effect:  73%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,71. In the absence of an intervention, we would have expected an average response of 0,76. The 95% interval of this counterfactual prediction is [0,58, 0,94]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,055 with a 95% interval of [-0,23, 0,13]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 440,76. Had the intervention not taken place, we would have expected a sum of 474,89. The 95% interval of this prediction is [360,75, 586,08].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -7%. The 95% interval of this percentage is [-31%, +17%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,27. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: html_constructed_from_input aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,082              16,425          
Prediction (s.d.)        0,11 (0,005)       21,69 (1,005)   
95% CI                   [0,099, 0,12]      [19,718, 23,75] 
                                                            
Absolute effect (s.d.)   -0,026 (0,005)     -5,263 (1,005)  
95% CI                   [-0,037, -0,016]   [-7,327, -3,294]
                                                            
Relative effect (s.d.)   -24% (4,6%)        -24% (4,6%)     
95% CI                   [-34%, -15%]       [-34%, -15%]    

Posterior tail-area probability p:   0,00107
Posterior prob. of a causal effect:  99,89259%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,082. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,099, 0,12]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,026 with a 95% interval of [-0,037, -0,016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 16,42. By contrast, had the intervention not taken place, we would have expected a sum of 21,69. The 95% interval of this prediction is [19,72, 23,75].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -24%. The 95% interval of this percentage is [-34%, -15%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average             Cumulative        
Actual                   0,082               51,069            
Prediction (s.d.)        0,11 (0,01)         67,75 (6,30)      
95% CI                   [0,089, 0,13]       [55,268, 79,88]   
                                                               
Absolute effect (s.d.)   -0,027 (0,01)       -16,682 (6,30)    
95% CI                   [-0,046, -0,0067]   [-28,809, -4,1989]
                                                               
Relative effect (s.d.)   -25% (9,3%)         -25% (9,3%)       
95% CI                   [-43%, -6,2%]       [-43%, -6,2%]     

Posterior tail-area probability p:   0,01005
Posterior prob. of a causal effect:  98,995%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,082. By contrast, in the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,089, 0,13]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,027 with a 95% interval of [-0,046, -0,0067]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 51,07. By contrast, had the intervention not taken place, we would have expected a sum of 67,75. The 95% interval of this prediction is [55,27, 79,88].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -25%. The 95% interval of this percentage is [-43%, -6%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,01). This means the causal effect can be considered statistically significant. 
[1] "Results for the column: reflected_xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average          Cumulative    
Actual                   0,049            9,733         
Prediction (s.d.)        0,034 (0,0024)   6,707 (0,4750)
95% CI                   [0,029, 0,038]   [5,804, 7,666]
                                                        
Absolute effect (s.d.)   0,015 (0,0024)   3,026 (0,4750)
95% CI                   [0,01, 0,02]     [2,07, 3,93]  
                                                        
Relative effect (s.d.)   45% (7,1%)       45% (7,1%)    
95% CI                   [31%, 59%]       [31%, 59%]    

Posterior tail-area probability p:   0,00103
Posterior prob. of a causal effect:  99,89659%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,049. By contrast, in the absence of an intervention, we would have expected an average response of 0,034. The 95% interval of this counterfactual prediction is [0,029, 0,038]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,015 with a 95% interval of [0,010, 0,020]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 9,73. By contrast, had the intervention not taken place, we would have expected a sum of 6,71. The 95% interval of this prediction is [5,80, 7,67].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +45%. The 95% interval of this percentage is [+31%, +59%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,015) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative     
Actual                   0,054            33,758         
Prediction (s.d.)        0,032 (0,0012)   19,988 (0,7291)
95% CI                   [0,03, 0,034]    [18,53, 21,409]
                                                         
Absolute effect (s.d.)   0,022 (0,0012)   13,770 (0,7291)
95% CI                   [0,02, 0,024]    [12,35, 15,227]
                                                         
Relative effect (s.d.)   69% (3,6%)       69% (3,6%)     
95% CI                   [62%, 76%]       [62%, 76%]     

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89879%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,054. By contrast, in the absence of an intervention, we would have expected an average response of 0,032. The 95% interval of this counterfactual prediction is [0,030, 0,034]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,022 with a 95% interval of [0,020, 0,024]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 33,76. By contrast, had the intervention not taken place, we would have expected a sum of 19,99. The 95% interval of this prediction is [18,53, 21,41].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +69%. The 95% interval of this percentage is [+62%, +76%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,022) to the original goal of the underlying intervention.

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

                         Average          Cumulative     
Actual                   0,12             24,56          
Prediction (s.d.)        0,11 (0,022)     21,64 (4,499)  
95% CI                   [0,073, 0,16]    [14,590, 32,30]
                                                         
Absolute effect (s.d.)   0,015 (0,022)    2,923 (4,499)  
95% CI                   [-0,039, 0,05]   [-7,734, 9,97] 
                                                         
Relative effect (s.d.)   14% (21%)        14% (21%)      
95% CI                   [-36%, 46%]      [-36%, 46%]    

Posterior tail-area probability p:   0,2093
Posterior prob. of a causal effect:  79%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. In the absence of an intervention, we would have expected an average response of 0,11. The 95% interval of this counterfactual prediction is [0,073, 0,16]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,015 with a 95% interval of [-0,039, 0,050]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 24,56. Had the intervention not taken place, we would have expected a sum of 21,64. The 95% interval of this prediction is [14,59, 32,30].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +14%. The 95% interval of this percentage is [-36%, +46%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,209. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average           Cumulative       
Actual                   0,12              77,87            
Prediction (s.d.)        0,12 (0,04)       77,06 (24,72)    
95% CI                   [0,046, 0,2]      [28,511, 125,9]  
                                                            
Absolute effect (s.d.)   0,0013 (0,04)     0,8094 (24,72)   
95% CI                   [-0,077, 0,079]   [-48,056, 49,362]
                                                            
Relative effect (s.d.)   1,1% (32%)        1,1% (32%)       
95% CI                   [-62%, 64%]       [-62%, 64%]      

Posterior tail-area probability p:   0,49495
Posterior prob. of a causal effect:  51%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,12. In the absence of an intervention, we would have expected an average response of 0,12. The 95% interval of this counterfactual prediction is [0,046, 0,20]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0013 with a 95% interval of [-0,077, 0,079]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 77,87. Had the intervention not taken place, we would have expected a sum of 77,06. The 95% interval of this prediction is [28,51, 125,93].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +1%. The 95% interval of this percentage is [-62%, +64%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,495. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: xss aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0,018              3,535           
Prediction (s.d.)        0,013 (0,0011)     2,541 (0,2209)  
95% CI                   [0,011, 0,015]     [2,116, 2,985]  
                                                            
Absolute effect (s.d.)   0,005 (0,0011)     0,994 (0,2209)  
95% CI                   [0,0027, 0,0071]   [0,5492, 1,4189]
                                                            
Relative effect (s.d.)   39% (8,7%)         39% (8,7%)      
95% CI                   [22%, 56%]         [22%, 56%]      

Posterior tail-area probability p:   0,00101
Posterior prob. of a causal effect:  99,89858%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,018. By contrast, in the absence of an intervention, we would have expected an average response of 0,013. The 95% interval of this counterfactual prediction is [0,011, 0,015]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0050 with a 95% interval of [0,0027, 0,0071]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 3,53. By contrast, had the intervention not taken place, we would have expected a sum of 2,54. The 95% interval of this prediction is [2,12, 2,99].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +39%. The 95% interval of this percentage is [+22%, +56%].

This means that the positive effect observed during the intervention period is statistically significant and unlikely to be due to random fluctuations. It should be noted, however, that the question of whether this increase also bears substantive significance can only be answered by comparing the absolute effect (0,0050) to the original goal of the underlying intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,001). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative       
Actual                   0,015              9,072            
Prediction (s.d.)        0,012 (0,0066)     7,345 (4,1215)   
95% CI                   [-0,0014, 0,025]   [-0,8465, 15,303]
                                                             
Absolute effect (s.d.)   0,0028 (0,0066)    1,7271 (4,1215)  
95% CI                   [-0,01, 0,016]     [-6,23, 9,919]   
                                                             
Relative effect (s.d.)   24% (56%)          24% (56%)        
95% CI                   [-85%, 135%]       [-85%, 135%]     

Posterior tail-area probability p:   0,33233
Posterior prob. of a causal effect:  67%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,015. In the absence of an intervention, we would have expected an average response of 0,012. The 95% interval of this counterfactual prediction is [-0,0014, 0,025]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0028 with a 95% interval of [-0,0100, 0,016]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 9,07. Had the intervention not taken place, we would have expected a sum of 7,35. The 95% interval of this prediction is [-0,85, 15,30].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed an increase of +24%. The 95% interval of this percentage is [-85%, +135%].

This means that, although the intervention appears to have caused a positive effect, this effect is not statistically significant when considering the entire post-intervention period as a whole. Individual days or shorter stretches within the intervention period may of course still have had a significant effect, as indicated whenever the lower limit of the impact time series (lower plot) was above zero. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,332. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: xss_through_dom aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative      
Actual                   0,42              83,87           
Prediction (s.d.)        0,5 (0,024)       99,0 (4,743)    
95% CI                   [0,45, 0,54]      [90,10, 108,45] 
                                                           
Absolute effect (s.d.)   -0,076 (0,024)    -15,170 (4,743) 
95% CI                   [-0,12, -0,031]   [-24,58, -6,224]
                                                           
Relative effect (s.d.)   -15% (4,8%)       -15% (4,8%)     
95% CI                   [-25%, -6,3%]     [-25%, -6,3%]   

Posterior tail-area probability p:   0,00204
Posterior prob. of a causal effect:  99,79592%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,42. By contrast, in the absence of an intervention, we would have expected an average response of 0,50. The 95% interval of this counterfactual prediction is [0,45, 0,54]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,076 with a 95% interval of [-0,12, -0,031]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 83,87. By contrast, had the intervention not taken place, we would have expected a sum of 99,04. The 95% interval of this prediction is [90,10, 108,45].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -15%. The 95% interval of this percentage is [-25%, -6%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is very small (Bayesian one-sided tail-area probability p = 0,002). This means the causal effect can be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average          Cumulative       
Actual                   0,43             268,99           
Prediction (s.d.)        0,5 (0,048)      313,8 (29,823)   
95% CI                   [0,41, 0,59]     [254,60, 371,27] 
                                                           
Absolute effect (s.d.)   -0,072 (0,048)   -44,772 (29,823) 
95% CI                   [-0,16, 0,023]   [-102,28, 14,388]
                                                           
Relative effect (s.d.)   -14% (9,5%)      -14% (9,5%)      
95% CI                   [-33%, 4,6%]     [-33%, 4,6%]     

Posterior tail-area probability p:   0,0672
Posterior prob. of a causal effect:  93%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,43. In the absence of an intervention, we would have expected an average response of 0,50. The 95% interval of this counterfactual prediction is [0,41, 0,59]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is -0,072 with a 95% interval of [-0,16, 0,023]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 268,99. Had the intervention not taken place, we would have expected a sum of 313,76. The 95% interval of this prediction is [254,60, 371,27].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -14%. The 95% interval of this percentage is [-33%, +5%].

This means that, although it may look as though the intervention has exerted a negative effect on the response variable when considering the intervention period as a whole, this effect is not statistically significant, and so cannot be meaningfully interpreted. The apparent effect could be the result of random fluctuations that are unrelated to the intervention. This is often the case when the intervention period is very long and includes much of the time when the effect has already worn off. It can also be the case when the intervention period is too short to distinguish the signal from the noise. Finally, failing to find a significant effect can happen when there are not enough control variables or when these variables do not correlate well with the response variable during the learning period.

The probability of obtaining this effect by chance is p = 0,067. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "Results for the column: xss_through_exception aggregate function: mean"
[1] "CausalImpact:  mean "
Posterior inference {CausalImpact}

                         Average           Cumulative     
Actual                   0                 0              
Prediction (s.d.)        -0,0035 (0,022)   -0,6972 (4,424)
95% CI                   [-0,046, 0,041]   [-9,178, 8,256]
                                                          
Absolute effect (s.d.)   0,0035 (0,022)    0,6972 (4,424) 
95% CI                   [-0,041, 0,046]   [-8,256, 9,178]
                                                          
Relative effect (s.d.)   -100% (-635%)     -100% (-635%)  
95% CI                   [1184%, -1316%]   [1184%, -1316%]

Posterior tail-area probability p:   0,43577
Posterior prob. of a causal effect:  56%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of -0,0035. The 95% interval of this counterfactual prediction is [-0,046, 0,041]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,0035 with a 95% interval of [-0,041, 0,046]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of -0,70. The 95% interval of this prediction is [-9,18, 8,26].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [+1184%, -1316%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is p = 0,436. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "CausalImpact:  mean _all"
Posterior inference {CausalImpact}

                         Average            Cumulative      
Actual                   0                  0               
Prediction (s.d.)        -0,00083 (0,011)   -0,51599 (6,683)
95% CI                   [-0,022, 0,02]     [-13,906, 12,19]
                                                            
Absolute effect (s.d.)   0,00083 (0,011)    0,51599 (6,683) 
95% CI                   [-0,02, 0,022]     [-12,19, 13,906]
                                                            
Relative effect (s.d.)   -100% (-1295%)     -100% (-1295%)  
95% CI                   [2362%, -2695%]    [2362%, -2695%] 

Posterior tail-area probability p:   0,4794
Posterior prob. of a causal effect:  52%

For more details, type: summary(impact, "report")

Analysis report {CausalImpact}


During the post-intervention period, the response variable had an average value of approx. 0,00. By contrast, in the absence of an intervention, we would have expected an average response of -0,00083. The 95% interval of this counterfactual prediction is [-0,022, 0,020]. Subtracting this prediction from the observed response yields an estimate of the causal effect the intervention had on the response variable. This effect is 0,00083 with a 95% interval of [-0,020, 0,022]. For a discussion of the significance of this effect, see below.

Summing up the individual data points during the post-intervention period (which can only sometimes be meaningfully interpreted), the response variable had an overall value of 0,00. By contrast, had the intervention not taken place, we would have expected a sum of -0,52. The 95% interval of this prediction is [-13,91, 12,19].

The above results are given in terms of absolute numbers. In relative terms, the response variable showed a decrease of -100%. The 95% interval of this percentage is [+2362%, -2695%].

This means that the negative effect observed during the intervention period is statistically significant. If the experimenter had expected a positive effect, it is recommended to double-check whether anomalies in the control variables may have caused an overly optimistic expectation of what should have happened in the response variable in the absence of the intervention.

The probability of obtaining this effect by chance is p = 0,479. This means the effect may be spurious and would generally not be considered statistically significant. 
[1] "avg_problems_vs_jssize.svg: blue trend line: locally estimated scatterplot smoothing (moving regression)"
[1] "repos_before_after_comparison, column: overall"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 30"
[1] "number of repositories <=-95% top_performer: 2     6,66666666666667 %"
[1] "number of repositories <0 good_performer: 2     6,66666666666667 %"
[1] "number of repositories =0 no_change_with_problems: 22     73,3333333333333 %"
[1] "number of repositories >0 worst_performer: 4     13,3333333333333 %"
[1] "sum problems added - problems fixed: -30,1947522920832"
[1] "repos_before_after_comparison, column: html_constructed_from_input"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 9"
[1] "number of repositories <=-95% top_performer: 2     22,2222222222222 %"
[1] "number of repositories <0 good_performer: 1     11,1111111111111 %"
[1] "number of repositories =0 no_change_with_problems: 6     66,6666666666667 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -4,9"
[1] "repos_before_after_comparison, column: reflected_xss"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 1"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 0     0 %"
[1] "number of repositories >0 worst_performer: 1     100 %"
[1] "sum problems added - problems fixed: 0,553968253968254"
[1] "repos_before_after_comparison, column: stored_xss"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 0"
[1] "number of repositories <=-95% top_performer: 0     NaN %"
[1] "number of repositories <0 good_performer: 0     NaN %"
[1] "number of repositories =0 no_change_with_problems: 0     NaN %"
[1] "number of repositories >0 worst_performer: 0     NaN %"
[1] "sum problems added - problems fixed: 0"
[1] "repos_before_after_comparison, column: unsafe_jquery_plugin"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 5"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 1     20 %"
[1] "number of repositories =0 no_change_with_problems: 4     80 %"
[1] "number of repositories >0 worst_performer: 0     0 %"
[1] "sum problems added - problems fixed: -4,75277777777778"
[1] "repos_before_after_comparison, column: xss"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 3"
[1] "number of repositories <=-95% top_performer: 0     0 %"
[1] "number of repositories <0 good_performer: 0     0 %"
[1] "number of repositories =0 no_change_with_problems: 2     66,6666666666667 %"
[1] "number of repositories >0 worst_performer: 1     33,3333333333333 %"
[1] "sum problems added - problems fixed: 0,155555555555556"
[1] "repos_before_after_comparison, column: xss_through_dom"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 26"
[1] "number of repositories <=-95% top_performer: 1     3,84615384615385 %"
[1] "number of repositories <0 good_performer: 3     11,5384615384615 %"
[1] "number of repositories =0 no_change_with_problems: 19     73,0769230769231 %"
[1] "number of repositories >0 worst_performer: 3     11,5384615384615 %"
[1] "sum problems added - problems fixed: -21,2514983238293"
[1] "repos_before_after_comparison, column: xss_through_exception"
[1] "number of repositories examined: 159"
[1] "number of repos with problems in this 90 day timeframe: 0"
[1] "number of repositories <=-95% top_performer: 0     NaN %"
[1] "number of repositories <0 good_performer: 0     NaN %"
[1] "number of repositories =0 no_change_with_problems: 0     NaN %"
[1] "number of repositories >0 worst_performer: 0     NaN %"
[1] "sum problems added - problems fixed: 0"
[1] "number of repos with overall problems in this 700 day timeframe: 40"
[1] "number of repos with html_constructed_from_input problems in this 700 day timeframe: 9"
[1] "number of repos with reflected_xss problems in this 700 day timeframe: 2"
[1] "number of repos with stored_xss problems in this 700 day timeframe: 0"
[1] "repos_individual_development ERROR collum: stored_xss"
List of 2
 $ message: chr "object 'value' not found"
 $ call   : language FUN(X[[i]], ...)
 - attr(*, "class")= chr [1:3] "simpleError" "error" "condition"
[1] "number of repos with unsafe_jquery_plugin problems in this 700 day timeframe: 12"
[1] "number of repos with xss problems in this 700 day timeframe: 5"
[1] "number of repos with xss_through_dom problems in this 700 day timeframe: 38"
[1] "number of repos with xss_through_exception problems in this 700 day timeframe: 1"
