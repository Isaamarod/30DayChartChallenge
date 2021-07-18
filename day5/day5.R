#install.packages("CGPfunctions")
library(CGPfunctions)
library(reshape)
library(ggrepel)
library(dplyr)

data_covid <- read.csv("covid-tracking-project-data-QueryResult.csv", header = TRUE)
data_covid_1st <- data_covid[data_covid$date == '2021-02-01',]
data_covid_1st


list_states <- c("New York","Florida","New Mexico","Alabama","California")

data_covid_states <- data_covid %>% filter(us_state_or_territory %in% list_states)


data_covid_reduced <- data_covid[,c("us_state_or_territory","positive","negative")]



data_covid_reduced_all <- data_covid[,c("date", "us_state_or_territory","positive","negative","hospitalized")]
ggplot(data = data_covid_reduced_all, aes(x = date, y = positive, group = us_state_or_territory)) +
  geom_line(aes(color = us_state_or_territory, alpha = 1), size = 2) +
  geom_point(aes(color = us_state_or_territory, alpha = 1), size = 4) +
  #  Labelling as desired
  labs(
    title = "New positive between 1st Febrary and 2st February",
    subtitle = "#30dayschallengue",
    caption = ""
  )


# ggplot(data = data_covid_reduced_all, aes(x = date, y = positive, group = us_state_or_territory)) +
#   geom_line(aes(color = us_state_or_territory, alpha = 1), size = 2) +
#   geom_point(aes(color = us_state_or_territory, alpha = 1), size = 4) +
#   geom_text(data = data_covid_reduced_all %>% filter(date == "2021-02-01"), 
#             aes(label = paste0(us_state_or_territory, " - ", positive, "positive Tests")) , 
#             hjust = 1.35, 
#             fontface = "bold", 
#             size = 4) +
#   geom_text(data = data_covid_reduced_all %>% filter(date == "2021-02-02"), 
#             aes(label = paste0(us_state_or_territory, " - ", positive, "positive Tests")) , 
#             hjust = -.35, 
#             fontface = "bold", 
#             size = 4) +
#   # move the x axis labels up top
#   scale_x_discrete(position = "top") +
#   theme_bw() +
#   # Format tweaks
#   # Remove the legend
#   theme(legend.position = "none") +
#   # Remove the panel border
#   theme(panel.border     = element_blank()) +
#   # Remove just about everything from the y axis
#   theme(axis.title.y     = element_blank()) +
#   theme(axis.text.y      = element_blank()) +
#   theme(panel.grid.major.y = element_blank()) +
#   theme(panel.grid.minor.y = element_blank()) +
#   # Remove a few things from the x axis and increase font size
#   theme(axis.title.x     = element_blank()) +
#   theme(panel.grid.major.x = element_blank()) +
#   theme(axis.text.x.top      = element_text(size=12)) +
#   # Remove x & y tick marks
#   theme(axis.ticks       = element_blank()) +
#   # Format title & subtitle
#   theme(plot.title       = element_text(size=14, face = "bold", hjust = 0.5)) +
#   theme(plot.subtitle    = element_text(hjust = 0.5)) +
#   #  Labelling as desired
#   labs(
#     title = "New positives between 1st Febrary and 2st February",
#     subtitle = "#30dayschallengue",
#     caption = ""
#   )
# 
# 
# 
# ggplot(data = data_covid, aes(x = date, y = hospitalizedincrease, group = us_state_or_territory)) +
#   geom_line(aes(color = us_state_or_territory, alpha = 1), size = 2) +
#   geom_point(aes(color = us_state_or_territory, alpha = 1), size = 4) +
#   geom_text_repel(data = data_covid_states %>% filter(date == "2021-02-01"), 
#             aes(label = paste0(us_state_or_territory, " - ", hospitalizedincrease, "hospitalizedincrease")) , 
#             hjust = 1.35, 
#             fontface = "bold", 
#             size = 4,
#             nudge_x = -.45, 
#             direction = "y") +
#   geom_text_repel(data = data_covid_states %>% filter(date == "2021-02-02"), 
#             aes(label = paste0(us_state_or_territory, " - ", hospitalizedincrease, "hospitalizedincrease")) , 
#             hjust = -.35, 
#             fontface = "bold", 
#             size = 4,
#             nudge_x = .5, 
#             direction = "y") +
#   # move the x axis labels up top
#   scale_x_discrete(position = "top") +
#   theme_bw() +
#   # Format tweaks
#   # Remove the legend
#   theme(legend.position = "none") +
#   # Remove the panel border
#   theme(panel.border     = element_blank()) +
#   # Remove just about everything from the y axis
#   theme(axis.title.y     = element_blank()) +
#   theme(axis.text.y      = element_blank()) +
#   theme(panel.grid.major.y = element_blank()) +
#   theme(panel.grid.minor.y = element_blank()) +
#   # Remove a few things from the x axis and increase font size
#   theme(axis.title.x     = element_blank()) +
#   theme(panel.grid.major.x = element_blank()) +
#   theme(axis.text.x.top      = element_text(size=12)) +
#   # Remove x & y tick marks
#   theme(axis.ticks       = element_blank()) +
#   # Format title & subtitle
#   theme(plot.title       = element_text(size=14, face = "bold", hjust = 0.5)) +
#   theme(plot.subtitle    = element_text(hjust = 0.5)) +
#   #  Labelling as desired
#   labs(
#     title = "New hospitalizations between 1st Febrary and 2st February",
#     subtitle = "#30dayschallengue",
#     caption = ""
#   )




ggplot(data = data_covid, aes(x = date, y = hospitalizedincrease, group = us_state_or_territory)) +
  geom_line(aes(color = us_state_or_territory, alpha = 1), size = 2) +
  geom_point(aes(color = us_state_or_territory, alpha = 1), size = 4) +
  geom_text_repel(data = data_covid %>% filter(date == "2021-02-01"), 
                  aes(label = paste0(us_state_or_territory, " - ", hospitalizedincrease," patients hospitalized increase")) , 
                  hjust = 1.35, 
                  fontface = "bold", 
                  size = 3,
                  nudge_x = -.45, 
                  direction = "y") +
  geom_text_repel(data = data_covid %>% filter(date == "2021-02-02"), 
                  aes(label = paste0(us_state_or_territory, " - ", hospitalizedincrease, " patients hospitalized increase")) , 
                  hjust = -.35, 
                  fontface = "bold", 
                  size = 3,
                  nudge_x = .5, 
                  direction = "y") +
  # move the x axis labels up top
  scale_x_discrete(position = "top") +
  theme_bw() +
  # Format tweaks
  # Remove the legend
  theme(legend.position = "none") +
  # Remove the panel border
  theme(panel.border     = element_blank()) +
  # Remove just about everything from the y axis
  theme(axis.title.y     = element_blank()) +
  theme(axis.text.y      = element_blank()) +
  theme(panel.grid.major.y = element_blank()) +
  theme(panel.grid.minor.y = element_blank()) +
  # Remove a few things from the x axis and increase font size
  theme(axis.title.x     = element_blank()) +
  theme(panel.grid.major.x = element_blank()) +
  theme(axis.text.x.top      = element_text(size=12)) +
  # Remove x & y tick marks
  theme(axis.ticks       = element_blank()) +
  # Format title & subtitle
  theme(plot.title       = element_text(size=14, face = "bold", hjust = 0.5)) +
  theme(plot.subtitle    = element_text(hjust = 0.5)) +
  #  Labelling as desired
  labs(
    title = "New hospitalizations between 1st Febrary and 2nd February",
    subtitle = "#30dayschallengue",
    caption = "Isabel Amaya"
  )