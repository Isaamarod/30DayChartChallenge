library(tidyverse)
library(ggpubr)
library(cluster)
library(factoextra)
library(plyr)
library(NbClust)


data_covid <- read.csv("anage_data.csv", header = TRUE)
data_covid
data_covid_res <- data_covid[,c("Species","Maximum.longevity..yrs.","Gestation.Incubation..days.")]
#groupbyspecies and logevity mean
data_covid_res_grouped <- ddply(data_covid_res, .(Species), summarize,  MeanLong=mean(Maximum.longevity..yrs.), MeanGestation=mean(Gestation.Incubation..days.))
result <- mydf[-1]

row.names(data_covid_res_grouped) <- data_covid_res_grouped$Species
data_covid_res_grouped <- data_covid_res_grouped[-1]


data_covid_res_grouped_final <- data_covid_res_grouped[complete.cases(data_covid_res_grouped), ]
set.seed(123)
##find the best option
set.seed(1234)
nc <- NbClust(data_covid_res_grouped_final, min.nc=2, max.nc=10, method="kmeans")

km_clusters <- kmeans(x = na.omit(data_covid_res_grouped_final), centers = 3, nstart = 50)

# Las funciones del paquete factoextra emplean el nombre de las filas del
# dataframe que contiene los datos como identificador de las observaciones.
# Esto permite añadir labels a los gráficos.
fviz_cluster(object = km_clusters, data = data_covid_res_grouped_final, show.clust.cent = TRUE,
             ellipse.type = "euclid", star.plot = TRUE, repel = TRUE) +
  labs(title = "Data from Database of Animal Ageing and Longevity clustering K-means",
       subtitle = "Isabel Amaya ~(^-^~) 8-9th Days of #30DayChartChallenge: Animals&Stadistical || kmeans|nbclust|factoextra",
       caption = "Data source: Human Ageing Genomic Resources") +
  theme_bw() +
  theme(legend.position = "none")