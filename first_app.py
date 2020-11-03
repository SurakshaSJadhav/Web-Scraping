import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd



expectancyData=pd.read_csv("Life Expectancy Data.csv")
#########################################################################################################
model = pickle.load( open( "save.p", "rb" ) )



option = st.sidebar.selectbox(
    'Adult Mortality',
     expectancyData['Adult Mortality'].unique())
'You selected:', option
option2 = st.sidebar.selectbox(
    'nfant deaths',
     expectancyData['infant deaths'].unique())
'You selected:', option2

option3 = st.sidebar.selectbox(
    'Alcohol',
     expectancyData['Alcohol'].unique())
'You selected:', option3
option4 = st.sidebar.selectbox(
    'percentage expenditure',
     expectancyData['percentage expenditure'].unique())
'You selected:', option4

option5 = st.sidebar.selectbox(
    'Hepatitis B',
     expectancyData['Hepatitis B'].unique())
'You selected:', option5
option6 = st.sidebar.selectbox(
    'Measles ',
     expectancyData['Measles '].unique())
'You selected:', option6
option7 = st.sidebar.selectbox(
    ' BMI ',
     expectancyData[' BMI '].unique())
'You selected:', option7
option8 = st.sidebar.selectbox(
    'under-five deaths ',
     expectancyData['under-five deaths '].unique())
'You selected:', option8
option9 = st.sidebar.selectbox(
    'Polio',
     expectancyData['Polio'].unique())
'You selected:', option9
option10 = st.sidebar.selectbox(
    'Total expenditure',
     expectancyData['Total expenditure'].unique())
'You selected:', option10
option11 = st.sidebar.selectbox(
    'Diphtheria ',
     expectancyData['Diphtheria '].unique())
'You selected:', option11
option12 = st.sidebar.selectbox(
    ' HIV/AIDS',
     expectancyData[' HIV/AIDS'].unique())
'You selected:', option12
option13 = st.sidebar.selectbox(
    'GDP',
     expectancyData['GDP'].unique())
'You selected:', option13
option14 = st.sidebar.selectbox(
    'Population',
     expectancyData['Population'].unique())
'You selected:', option14
option15 = st.sidebar.selectbox(
    ' thinness  1-19 years',
     expectancyData[' thinness  1-19 years'].unique())
'You selected:', option15
option16 = st.sidebar.selectbox(
    ' thinness 5-9 years',
     expectancyData[' thinness 5-9 years'].unique())
'You selected:', option16
option17 = st.sidebar.selectbox(
    'Income composition of resources',
     expectancyData['Income composition of resources'].unique())
'You selected:', option17
option18 = st.sidebar.selectbox(
    'Schooling',
     expectancyData['Schooling'].unique())
'You selected:', option18
option19 = 1
# st.sidebar.selectbox(
#     'Status Code',
#      expectancyData['Status Code'].unique())
'You selected:', option19




st.title('Consuming model...')

st.title('Prediction ready')


['Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure',
       'Hepatitis B', 'Measles', 'BMI', 'under-five deaths', 'Polio',
       'Total expenditure', 'Diphtheria', 'HIV/AIDS', 'GDP', 'Population',
       'thinness  1-19 years', 'thinness 5-9 years',
       'Income composition of resources', 'Schooling', 'Status Code']