# Scott Bennett

# Data found on https://www.cdc.gov/nchs/nhis/2022nhis.htm

# In this R file, we took all the downloaded CSVs for the data that we were interested in combined them into one final data frame which was then exported as a .csv and further cleaned during EDA.

library(dplyr)

# 2022 Data Load full adult data
adult22 <- read.csv("adult22.csv")

#2021 Data

adult21 <- read.csv("adult21.csv")

#2020 Data

adult20 <- read.csv("adult20.csv")

#2019 Data

adult19 <- read.csv("adult19.csv")

#2018 Data

adult18 <- read.csv("samadult.csv")

# The CDC Changed it's survey after 2018, so after loading 2018 data, it was apparent that it was too different
# For this reason, we did not include 2018 data, just 2019 - 2022


# Merge data

# Merge 22 and 21 data together

common_col_names <- intersect(names(adult22), names(adult21))

total_adult=rbind(adult22[,common_col_names], adult21[,common_col_names])

# Merge 20 data to total

common_col_names <- intersect(names(total_adult), names(adult20))

total_adult=rbind(total_adult[,common_col_names], adult20[,common_col_names])

# Merge 19 data to total

common_col_names <- intersect(names(total_adult), names(adult19))

total_adult=rbind(total_adult[,common_col_names], adult19[,common_col_names])

write.csv(total_adult, 'nhis_adult_2019to2022.csv')
