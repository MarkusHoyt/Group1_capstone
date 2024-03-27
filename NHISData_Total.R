library(dplyr)

# 2022 Data Load full adult and child data and income
adult22 <- read.csv("adult22.csv") %>%
  mutate(subject_type = "adult") %>%
  mutate(year = 2022)

child22 <- read.csv("child22.csv") %>%
  mutate(subject_type = "child") %>%
  mutate(year = 2022)

### Most of the columns in adult and child have _A or _C so a merger is not that simple

for (col in 1:ncol(adult22)){
  colnames(adult22)[col] <-  sub("_A.*", "", colnames(adult22)[col])
}


for (col in 1:ncol(child22)){
  colnames(child22)[col] <-  sub("_C.*", "", colnames(child22)[col])
}
 
common_col_names <- intersect(names(adult22), names(child22))

total22 <- full_join(adult22, child22, by = common_col_names)
