###########################
##########  4TH DAY #######
###########################

##diabetes
##install.packages("mlbench")
library(mlbench)
library(gganatogram)
library(dplyr)
library(viridis)
library(gridExtra)

data(PimaIndiansDiabetes)


PimaIndiansDiabetes

compareGroups_diabetics <- rbind(data.frame(organ = c("pancreas", "nerve","liver"), 
                                            colour = c("red", "red","purple"), 
                                            value = c(PimaIndiansDiabetes[15,][['insulin']], PimaIndiansDiabetes[15,][['pressure']],PimaIndiansDiabetes[15,][['glucose']]),
                                            type = rep('Diabetic patient', 3), 
                                            stringsAsFactors=F),
                                 data.frame(organ =  c("pancreas", "nerve","liver"), 
                                            colour = c("red", "red","purple"), 
                                            value = c(PimaIndiansDiabetes[4,][['insulin']], PimaIndiansDiabetes[4,][['pressure']],PimaIndiansDiabetes[4,][['glucose']]),
                                            type = rep('No diabetic patient', 3), 
                                            stringsAsFactors=F))



gganatogram(data=compareGroups_diabetics, fillOutline='#a6bddb', organism='human', sex='female', fill="value") + 
  theme_void() +
  facet_wrap(~type) +
  scale_fill_viridis()