setwd("C:/Users/vijaya sindhu/Desktop")
library(readxl)
library(ggplot2)
library(xlsx)

applicants=read_xlsx("dataset1.xlsx", sheet = 1)
team_existing=read_xlsx("dataset1.xlsx", sheet = 2)
set.seed(20)
team_cluster<- kmeans(team_existing[,2:26], 1, nstart = 1)
mean_value <- team_cluster$centers
val <- applicants
val[,2:26] <- (val[,2:26]-mean_value[1:25])*10
val
user <- val[val$User_url=="USER_ID 111110007",]
x <- user[,2:26]
write.xlsx(x =  user, file = "test.xlsx",
           sheetName = "TestSheet", row.names = FALSE)

