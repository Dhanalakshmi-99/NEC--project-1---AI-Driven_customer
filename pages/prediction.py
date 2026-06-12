import streamlit as st

st.title("🛒 Purchase Prediction")

age = st.number_input("Age")

income = st.number_input("Income")

tenure = st.number_input("Tenure")

if st.button("Predict"):

    if income > 80000:
        result = "Likely To Purchase"

    else:
        result = "Less Likely To Purchase"

    st.success(result)