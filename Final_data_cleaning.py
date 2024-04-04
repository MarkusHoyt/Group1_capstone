# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:20:14 2024

@author: markt
"""
import pandas as pd

#data = pd.read_csv("/Users/markt/Downloads/Final_Data.csv")

#---
#data = data[['points', 'blocks']]

data1 = pd.read_csv('nhis_adult_2019to2022_short.csv')
data2 = pd.read_csv('nhis_adult_2019to2022.csv')
col = data1.columns

print(col)

data = data2[col]

shape = data.shape
print("Shape = {}".format(shape))
#


# Counting NaN values in all columns
nan_count = data1.isna().sum()

print(nan_count)

#dropping NA from all columns that only has 1
#data = data.dropna(subset=['REGION', 'HISP_A', 'SRVY_YR', 'SEX_A', 'AGEP_A', 'HOUTENURE_A', 'FSNAP12M_A', 'SCHCURENR_A', 'PAYWORRY_A', 'PREDIB_A', 'ASEV_A', 'STREV_A', 'MIEV_A', 'ANGEV_A', 'CHDEV_A', 'CHLEV_A', 'HYPEV_A', 'PHSTAT_A', 'POVRATTC_A'])

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

data.to_csv('Clean_Data.csv', index=False)
# Make NA in DIBTYPE_A 0
data['DIBTYPE_A'] = data['DIBTYPE_A'].fillna(0)


# Change column A's values to a numeric type
#data['DIBTYPE_A'] = pd.to_numeric(data['DIBTYPE_A'])

data['Combined'] = data['PREDIB_A'] + data['DIBTYPE_A']

data.loc[data["Combined"] == 2, "Combined"] = 0

data = data.drop(data[data['Combined'] == 5].index)

data.loc[data["Combined"] == 3, "Combined"] = 2

data.loc[data["Combined"] == 4, "Combined"] = 3

data = data.drop(['PREDIB_A', 'DIBTYPE_A'], axis=1)

data.rename(columns = {'Combined':'DIA_STATUS'}, inplace = True)

print(data['DIA_STATUS'].value_counts())

#Visualization
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.catplot(data=data, x="REGION", y="POVRATTC_A", hue="DIA_STATUS")

# Select ratio
ratio = 0.99
 
total_rows = data.shape[0]
train_size = int(total_rows*ratio)
 
# Split data into test and train
train = data[0:train_size]
test = data[train_size:]

sns.catplot(data=test, x="REGION", y="POVRATTC_A", hue="DIA_Group")

sns.boxplot(x="REGION", y="POVRATTC_A", data=data,palette='rainbow')


from tableone import TableOne, load_dataset

for col in data.columns:
    print(col)
    
    
columns = ['SRVY_YR','URBRRL','REGION','AGEP_A','SEX_A','HISP_A','RACEALLP_A','MLTFAMFLG_A','PHSTAT_A','HYPEV_A','CHLEV_A','ANGEV_A','MIEV_A','STREV_A','ASEV_A','NUMCAN_A','HEIGHTTC_A','WEIGHTLBTC_A','BMICAT_A','DISAB3_A','NOTCOV_A','PAYWORRY_A','URGNT12MTC_A','EMERG12MTC_A','ANXLEVEL_A','DEPLEVEL_A','SMKCIGST_A','SMKECIGST_A','LEGMSTAT_A','PARSTAT_A','CITZNSTP_A','SCHCURENR_A','POVRATTC_A','FSNAP12M_A','FDSCAT4_A','HOUTENURE_A','CHDEV_A','DIA_STATUS']
categorical = ['DIA_STATUS', 'SRVY_YR']

groupby = ['DIA_STATUS', 'SRVY_YR']
mytable = TableOne(data, columns=columns, categorical=categorical, groupby=groupby, pval=False)

print(mytable.tabulate(tablefmt = "fancy_grid"))

mytable.to_excel('mytable.xlsx')


from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

y, X = dmatrices('DIA_STATUS ~ SRVY_YR+URBRRL+REGION+AGEP_A+SEX_A+HISP_A+RACEALLP_A+MLTFAMFLG_A+PHSTAT_A+HYPEV_A+CHLEV_A+ANGEV_A+MIEV_A+STREV_A+ASEV_A+NUMCAN_A+HEIGHTTC_A+WEIGHTLBTC_A+BMICAT_A+DISAB3_A+NOTCOV_A+PAYWORRY_A+URGNT12MTC_A+EMERG12MTC_A+ANXLEVEL_A+DEPLEVEL_A+SMKCIGST_A+SMKECIGST_A+LEGMSTAT_A+PARSTAT_A+CITZNSTP_A+SCHCURENR_A+POVRATTC_A+FSNAP12M_A+FDSCAT4_A+HOUTENURE_A+CHDEV_A+DIA_STATUS', data=data, return_type='dataframe')

vif_df = pd.DataFrame()
vif_df['variable'] = X.columns

vif_df['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_df)
vif_df.to_excel('vif_df.xlsx')

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

def get_Gender(SEX_A):
    if SEX_A == 1:
        return 'Male'
    else:
        return 'Female'
    
data['Gender_Group'] = data['SEX_A'].apply(get_Gender)

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



Descriptive = data.describe(include='object')

descriptive2 = data.describe(percentiles=[])

data = data.iloc[:,:-5]

sns.pairplot(data)
plt.show()