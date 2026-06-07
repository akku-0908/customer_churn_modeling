import streamlit as st
import pandas as pd
import joblib

st.title("Predict Customer Churn")

model = joblib.load(
    "D:\customer_churn\models\churn.pkl"
)

tenure = st.slider(
    "Tenure",
    0,
    72,
    12
)

monthly_charges = st.slider(
    "Monthly Charges",
    0.0,
    150.0,
    50.0
)

total_charges = st.number_input(
    "Total Charges",
    value=500.0
)

if st.button("Predict"):

    sample = pd.DataFrame(
        {
            "tenure":[tenure],
            "MonthlyCharges":[monthly_charges],
            "TotalCharges":[total_charges]
        }
    )

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error(
            "High Churn Risk"
        )
    else:
        st.success(
            "Low Churn Risk"
        )