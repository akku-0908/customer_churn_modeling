import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(
    page_title="Customer Churn Analytics",
    layout="wide"
)

# -------------------
# Load Data
# -------------------
filepath=r"D:\customer_churn\Telco-Customer-Churn.csv"
@st.cache_data

def load_data():
    return pd.read_csv(
        filepath
    )

df = load_data()

# -------------------
# Dashboard Title
# -------------------

st.title("📊 Customer Churn Analytics Dashboard")

st.markdown(
    "Analyze customer churn and identify high-risk customers."
)

# -------------------
# KPI Section
# -------------------

total_customers = len(df)

churn_customers = len(
    df[df["Churn"] == "Yes"]
)

churn_rate = (
    churn_customers
    / total_customers
    * 100
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Customers",
    total_customers
)

col2.metric(
    "Churn Customers",
    churn_customers
)

col3.metric(
    "Churn Rate (%)",
    round(churn_rate, 2)
)

# -------------------
# Churn Distribution
# -------------------

st.subheader(
    "Churn Distribution"
)

fig = px.pie(
    df,
    names="Churn"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------
# Contract Analysis
# -------------------

st.subheader(
    "Contract Type Analysis"
)

contract = (
    df.groupby(
        ["Contract", "Churn"]
    )
    .size()
    .reset_index(name="Count")
)

fig = px.bar(
    contract,
    x="Contract",
    y="Count",
    color="Churn",
    barmode="group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------
# Monthly Charges
# -------------------

st.subheader(
    "Monthly Charges"
)

fig = px.box(
    df,
    x="Churn",
    y="MonthlyCharges"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------
# Raw Data
# -------------------

st.subheader(
    "Dataset Preview"
)

st.dataframe(df.head(50))