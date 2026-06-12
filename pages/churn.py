import streamlit as st

st.title("⚠️ Churn Prediction")

income = st.number_input("Income")

tenure = st.number_input("Tenure")

if st.button("Predict Churn"):

    if tenure < 12:
        st.error(
            "High Churn Risk"
        )

    else:
        st.success(
            "Low Churn Risk"
        )