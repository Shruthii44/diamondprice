import streamlit as st
import pandas as pd
import pickle
import joblib
from sklearn.pipeline import Pipeline


model = joblib.load("dmodel.pkl")

st.title('Diamond Price Prediction')

# numerical inputs
depth=st.number_input('Depth Percentage',value=61.0)
carat=st.number_input('Carat Weight',min_value=0.1,max_value=5.0,value=0.7)
table=st.number_input('Table Width',value=55.0)

# categorical inputs
color=st.selectbox('Color',['E','I','J','D','H','F','G'])
clarity=st.selectbox('Clarity',["SI1","SI2","VS1","VS2","VVS1","VVS2","IF", "I1"])
cut=st.selectbox('Cut',['Ideal','Premium','Good','Very Good','Fair'])

#create input dataframe
input_data=pd.DataFrame({
    'depth':[float(depth)],
    'carat':[float(carat)],
    'table':[float(table)],
    'color':[color],
    'clarity':[clarity],
    'cut':[cut]})

#prediction
if st.button("Predict Price"):
    prediction=model.predict(input_data)
    st.success(f"The estimated price is ${prediction[0]:.2f}")
    









