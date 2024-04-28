# Scott Bennett

# Data found on https://www.cdc.gov/nchs/nhis/2022nhis.htm

# In this R file, we took all the downloaded CSVs for the data that we were interested in and combined them into one final data frame, which was then exported as a .csv and further cleaned during EDA.

# After creating the combined data set, the team went through the features one at a time on Excel and trimmed down from 400 features to 38 features
# URBRRL	RACEALLP_A	DISAB3_A	CITZNSTP_A	LEGMSTAT_A	FDSCAT4_A	SMKECIGST_A	SMKCIGST_A	BMICAT_A	WEIGHTLBTC_A	HEIGHTTC_A	URGNT12MTC_A	EMERG12MTC_A	NOTCOV_A	
# PARSTAT_A	MLTFAMFLG_A	NUMCAN_A	HISP_A	REGION SRVY_YR	SEX_A	AGEP_A	HOUTENURE_A	FSNAP12M_A	SCHCURENR_A	DEPLEVEL_A	ANXLEVEL_A	PAYWORRY_A	DIBTYPE_A	PREDIB_A	
# ASEV_A	STREV_A	MIEV_A	ANGEV_A	CHDEV_A	CHLEV_A	HYPEV_A	PHSTAT_A	POVRATTC_A

# These features were selected due to their relevance with socioeconomic data and general demographic data that we were interested in modeling. Many variables within the 400 were redundant or ways of 
# representing similar data.

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
