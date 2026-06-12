import streamlit as st
import pandas as pd

from analytics.customer_metrics import CustomerMetrics
from analytics.visualization import Visualizations

st.title("📊 Customer Dashboard")

df = pd.read_csv("data/customers.csv")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Customers",
    CustomerMetrics.total_customers(df)
)

col2.metric(
    "Average Income",
    CustomerMetrics.average_income(df)
)

col3.metric(
    "Average Tenure",
    CustomerMetrics.average_tenure(df)
)

st.plotly_chart(
    Visualizations.income_distribution(df),
    use_container_width=True
)

st.plotly_chart(
    Visualizations.city_distribution(df),
    use_container_width=True
)