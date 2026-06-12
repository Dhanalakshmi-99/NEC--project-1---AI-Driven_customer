import streamlit as st

from models.recommendation import RecommendationEngine

st.title("🎁 Product Recommendations")

income = st.number_input("Customer Income")

if st.button("Generate Recommendations"):

    recommender = RecommendationEngine()

    products = recommender.recommend({
        "income": income
    })

    st.subheader("Recommended Offers")

    for product in products:
        st.write("✅", product)