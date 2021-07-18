set.seed(345)
library(ggplot2)
library(RColorBrewer)
ngroup=56
names=paste("G_",seq(1,ngroup),sep="")
DAT=data.frame()

for(i in seq(1:30)){
  data=data.frame( matrix(0, ngroup , 3))
  data[,1]=i
  data[,2]=sample(names, nrow(data))
  data[,3]=prop.table(sample( c(rep(0,100),c(1:ngroup)) ,nrow(data)))
  DAT=rbind(DAT,data)
}
colnames(DAT)=c("Year","Group","Value")
DAT=DAT[order( DAT$Year, DAT$Group) , ]
DAT

coul = brewer.pal(12, "Paired") 
coul = colorRampPalette(coul)(ngroup)
coul=coul[sample(c(1:length(coul)) , size=length(coul) ) ]


data_covid <- read.csv("covid-tracking-project-data-QueryResult.csv", header = TRUE)

data_covid$DateNum <- as.integer(gsub(pattern = "-", replacement="", x = data_covid$date))

data_covid_reduced <- data_covid[,c("DateNum","us_state_or_territory","positiveincrease")]




ggplot(data_covid_reduced, aes(x=DateNum, y=positiveincrease, fill=us_state_or_territory )) + 
  geom_area(alpha=1  )+
  theme_bw() +
  #scale_fill_brewer(colour="red", breaks=rev(levels(DAT$Group)))+
  scale_fill_manual(values = coul)+
  theme(
    text = element_text(hjust = 0.5, size = 14),
    line = element_blank(),
    title = element_text(hjust = 0.5),
    legend.position="none",
    panel.border = element_blank(),
    panel.background = element_blank()) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5)) +
  scale_x_continuous("Day", labels = as.character(data_covid$DateNum), breaks = data_covid$DateNum)+
  scale_y_continuous("Number of positives increase per day",labels = scales::comma) +
  labs(title = "Abstract Chart about Confirmed Increase COVID19 patients evolution in February 2021 in US by State",
       subtitle = "Isabel Amaya ~(^-^~) 10th Day of #30DayChartChallenge: Abstract || ggplot2|RColorBrewer",
       caption = "Data source: data.world | COVID Tracking Project data")

plot
