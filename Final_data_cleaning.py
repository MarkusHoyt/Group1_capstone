# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:20:14 2024

@author: markthoyt
"""
import pandas as pd

#loading data
#MH
data1 = pd.read_csv('nhis_adult_2019to2022_short.csv')
data2 = pd.read_csv('nhis_adult_2019to2022.csv')
col = data1.columns

print(col)

data = data2[col]

shape = data.shape
print("Shape = {}".format(shape))



# Counting NaN values in all columns
#MH
nan_count = data1.isna().sum()

print(nan_count)

#dropping NA from all columns that only has 1
#MH
data = data.dropna(subset=['REGION', 'HISP_A', 'SRVY_YR', 'SEX_A', 'AGEP_A', 'HOUTENURE_A', 'FSNAP12M_A', 'SCHCURENR_A', 'PAYWORRY_A', 'PREDIB_A', 'ASEV_A', 'STREV_A', 'MIEV_A', 'ANGEV_A', 'CHDEV_A', 'CHLEV_A', 'HYPEV_A', 'PHSTAT_A', 'POVRATTC_A'])

#dropping columns with vulues 7,8,9 in them. Thes represent Did not acertain, unkown, and Not applicable
#MH
data = data.drop(data[data['SEX_A'] == 9].index)
data = data.drop(data[data['SEX_A'] == 7].index)

data = data.drop(data[data['RACEALLP_A'] == 9].index)
data = data.drop(data[data['RACEALLP_A'] == 8].index)
data = data.drop(data[data['RACEALLP_A'] == 7].index)

data = data.drop(data[data['PHSTAT_A'] == 9].index)
data = data.drop(data[data['PHSTAT_A'] == 7].index)

data = data.drop(data[data['HYPEV_A'] == 9].index)
data = data.drop(data[data['HYPEV_A'] == 7].index)

data = data.drop(data[data['CHLEV_A'] == 9].index)
data = data.drop(data[data['CHLEV_A'] == 7].index)

data = data.drop(data[data['CHDEV_A'] == 9].index)
data = data.drop(data[data['CHDEV_A'] == 8].index)
data = data.drop(data[data['CHDEV_A'] == 7].index)

data = data.drop(data[data['ANGEV_A'] == 9].index)
data = data.drop(data[data['ANGEV_A'] == 7].index)

data = data.drop(data[data['MIEV_A'] == 9].index)
data = data.drop(data[data['MIEV_A'] == 7].index)

data = data.drop(data[data['STREV_A'] == 9].index)
data = data.drop(data[data['STREV_A'] == 7].index)

data = data.drop(data[data['ASEV_A'] == 9].index)

data = data.drop(data[data['NUMCAN_A'] == 9].index)
data = data.drop(data[data['NUMCAN_A'] == 7].index)

data = data.drop(data[data['PREDIB_A'] == 9].index)
data = data.drop(data[data['PREDIB_A'] == 7].index)

data = data.drop(data[data['DIBTYPE_A'] == 9].index)
data = data.drop(data[data['DIBTYPE_A'] == 7].index)


data = data.drop(data[data['HEIGHTTC_A'] == 97].index)
data = data.drop(data[data['HEIGHTTC_A'] == 98].index)
data = data.drop(data[data['HEIGHTTC_A'] == 99].index)

data = data.drop(data[data['BMICAT_A'] == 9].index)

data = data.drop(data[data['DISAB3_A'] == 9].index)

data = data.drop(data[data['NOTCOV_A'] == 9].index)

data = data.drop(data[data['PAYWORRY_A'] == 9].index)
data = data.drop(data[data['PAYWORRY_A'] == 8].index)
data = data.drop(data[data['PAYWORRY_A'] == 7].index)

data = data.drop(data[data['URGNT12MTC_A'] == 9].index)
data = data.drop(data[data['URGNT12MTC_A'] == 8].index)
data = data.drop(data[data['URGNT12MTC_A'] == 7].index)

data = data.drop(data[data['EMERG12MTC_A'] == 9].index)
data = data.drop(data[data['EMERG12MTC_A'] == 8].index)
data = data.drop(data[data['EMERG12MTC_A'] == 7].index)

data = data.drop(data[data['ANXLEVEL_A'] == 9].index)
data = data.drop(data[data['ANXLEVEL_A'] == 8].index)
data = data.drop(data[data['ANXLEVEL_A'] == 7].index)

data = data.drop(data[data['DEPLEVEL_A'] == 9].index)
data = data.drop(data[data['DEPLEVEL_A'] == 8].index)
data = data.drop(data[data['DEPLEVEL_A'] == 7].index)

data = data.drop(data[data['SMKCIGST_A'] == 9].index)

data = data.drop(data[data['SMKECIGST_A'] == 9].index)

data = data.drop(data[data['LEGMSTAT_A'] == 9].index)

data = data.drop(data[data['PARSTAT_A'] == 9].index)

data = data.drop(data[data['CITZNSTP_A'] == 9].index)
data = data.drop(data[data['CITZNSTP_A'] == 8].index)
data = data.drop(data[data['CITZNSTP_A'] == 7].index)

data = data.drop(data[data['SCHCURENR_A'] == 9].index)
data = data.drop(data[data['SCHCURENR_A'] == 8].index)
data = data.drop(data[data['SCHCURENR_A'] == 7].index)

data = data.drop(data[data['FSNAP12M_A'] == 9].index)
data = data.drop(data[data['FSNAP12M_A'] == 8].index)
data = data.drop(data[data['FSNAP12M_A'] == 7].index)


data = data.drop(data[data['FDSCAT4_A'] == 8].index)

data = data.drop(data[data['HOUTENURE_A'] == 9].index)
data = data.drop(data[data['HOUTENURE_A'] == 8].index)
data = data.drop(data[data['HOUTENURE_A'] == 7].index)

data = data.fillna(0)

#saving the cleaned data to a new CSV for ease of use in Future cases
#MH
data.to_csv('Clean_Data.csv', index=False)

# Make NA in DIBTYPE_A 0
#MH
data['DIBTYPE_A'] = data['DIBTYPE_A'].fillna(0)


# Change column A's values to a numeric type to make DIA_STATUS column
#MH
data['Combined'] = data['PREDIB_A'] + data['DIBTYPE_A']

data.loc[data["Combined"] == 2, "Combined"] = 0

data = data.drop(data[data['Combined'] == 5].index)

data.loc[data["Combined"] == 3, "Combined"] = 2

data.loc[data["Combined"] == 4, "Combined"] = 3

data = data.drop(['PREDIB_A', 'DIBTYPE_A'], axis=1)

data.rename(columns = {'Combined':'DIA_STATUS'}, inplace = True)

print(data['DIA_STATUS'].value_counts())


#Changing Dibetes status to categorical for future use
#MH
def get_dia_status(DIA_STATUS):
    if DIA_STATUS == 0:
        return 'Non-Diabetic'
    elif DIA_STATUS == 1:
        return 'Pre-Diabetes'
    elif DIA_STATUS == 2:
        return 'Type 1 Diabetes'
    else:
        return 'Type 2 Diabetes'
    
data['DIA_Group'] = data['DIA_STATUS'].apply(get_dia_status)

#Changing Region status to categorical for future use
#MH
def get_Region(REGION):
    if REGION == 1:
        return 'Northeast'
    elif REGION == 2:
        return 'Midwest'
    elif REGION == 3:
        return 'South'
    else:
        return 'West'
    
data['Region_Group'] = data['REGION'].apply(get_Region)

#Changing Gender status to categorical for future use
#MH
def get_Gender(SEX_A):
    if SEX_A == 1:
        return 'Male'
    else:
        return 'Female'
    
data['Gender_Group'] = data['SEX_A'].apply(get_Gender)

#Changing PH status to categorical for future use
#MH
def Health(PHSTAT_A):
    if PHSTAT_A == 1:
        return 'Excellent'
    if PHSTAT_A == 2:
        return 'Very Good'
    elif PHSTAT_A == 3:
        return 'Good'
    elif PHSTAT_A == 4:
        return 'Fair'
    else:
        return 'Poor'    

data['Health_Status'] = data['PHSTAT_A'].apply(Health)

#Changing BMI Category to categorical for future use
#MH
def BMI(BMICAT_A):
    if BMICAT_A == 1:
        return 'Underweight'
    if BMICAT_A == 2:
        return 'Healthy weight'
    elif BMICAT_A == 3:
        return 'Overweight'
    else:
        return 'Obese'    

data['BMI_Category'] = data['BMICAT_A'].apply(BMI)


#getting a description of the data
#MH
Descriptive = data.describe(include='object')

#precentages
#MH
descriptive2 = data.describe(percentiles=[])

#removign a row
#MH
data = data.iloc[:,:-5]