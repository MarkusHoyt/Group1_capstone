# Team1_capstone

Authors: Scott Bennett, Thomas Dinh, Mark Hoyt

Readme Author: Scott Bennett

Project Title:
Predicting Risk of Type 2 Diabetes based on National Health Interview Survey (NHIS) Questionnaire Responses

Brief background:
Our study question focuses on predicting a patient's diabetes condition from survey data. To tackle the issue of undiagnosed diabetes in the US, this question highlights the critical need for early detection and intervention. Even while the study in this area suggests that our issue may not be wholly original, it is nevertheless critical to deepen our understanding of diabetes to create more potent preventative strategies.

Question:
Can we develop a model to show the risk of Type 2 Diabetes based on information available to undiagnosed patients so that they know to visit their physician?

Hypothesis & Predictions:
Hypothesis: There is a connection between a person’s responses to specific NHIS questions and whether or not they are nondiabetic or have Type 2 diabetes because there are known health and lifestyle indicators previously identified as associated with an increased risk of type 2 diabetes (Diabetes management: How lifestyle, daily routine affect blood sugar 2024).
Prediction: Based on health and lifestyle factors from the NHIS dataset, we predict that we will be able to classify whether or not a patient has Type 2 diabetes based on their responses to specific NHIS questions.


# Data Files

The CSV files were taken from https://www.cdc.gov/nchs/nhis/2022nhis.htm

2019 - 2022 data was used. Methodology changed between 2018 and 2019, so data from 2018 and before were not compatible with 2019-2022
'adult19.csv'
'adult20.csv'
'adult21.csv'
'adult22.csv'

# Data Combination

The R file used to combine the data was:

'NHISData_Total.r'

# Finalized Data Set

Using Excel, we reduced the features to 38 based on research on diabetes causes, along with socioeconomic and other health questions with which we were interested in establishing a relationship. This is captured in 'nhis_adult_2019to2022_short.csv'. The data dictionary for the selected features is in 'NHIS Frequency Codebook - Selected Variables.pdf'

Then, using the file: 

'Final_data_cleaning.py'

the Clean_Data.csv was created which was the final dataset that we used.

# Project Order:

1. NHISData_Total.r
2. Use 'nhis_adult_2019to2022_short.csv'
3. Final_data_cleaning.py
4. TD_Team_1_eda_code.ipynb
5. Team_1_preprocessing_modeling_TD.ipynb
6. Team_1_Final_Model.ipynb

# Custom Function Definitions

'Final_data_cleaning.py':
1. get_dia_status - Changed the numeric values in DIA_STATUS and converted it to string values
2. get_Region - Converted numeric value for region to string value
3. get_Gender - Converted numeric value for sex to string value
4. Health - Converted numeric value for PHSTAT_A to string value
5. BMI - Converted numeric value for BMI to string value

'Team_1_FinalModel.ipynb':
1. categorize_age - Took age ranges and made them into four distinct categories
