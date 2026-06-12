import streamlit as st
import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler

st.title("🎯 Customer Segmentation")

df = pd.read_csv("data/customers.csv")

features = [
    'age',
    'income',
    'tenure'
]

X = df[features]

scaler = joblib.load(
    "saved_models/scaler.pkl"
)

model = joblib.load(
    "saved_models/segment_model.pkl"
)

X_scaled = scaler.transform(X)

df['segment'] = model.predict(X_scaled)

st.dataframe(df)

st.success(
    "Customer Segments Generated Successfully"
)