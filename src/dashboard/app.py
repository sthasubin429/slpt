import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils import load_processed_data, load_model, predict_churn

st.set_page_config(layout="wide")
st.title("📊 Telecom Churn Dashboard")

# Load data and model
df = load_processed_data()
model = load_model()

# Data Overview
st.header("🔍 Data Preview")
st.dataframe(df.head())

# Churn Distribution
st.header("📈 Churn Overview")
churn_counts = df["Churn"].value_counts()
st.bar_chart(churn_counts)

# Monthly Revenue Distribution by Churn
st.subheader("💵 Monthly Revenue Distribution by Churn")
fig1, ax1 = plt.subplots()

# Drop NaNs for MonthlyRevenue
df_clean_rev = df.dropna(subset=["MonthlyRevenue", "Churn"])

sns.boxplot(data=df_clean_rev, x="Churn", y="MonthlyRevenue", ax=ax1)
ax1.set_ylabel("Monthly Revenue ($)")
st.pyplot(fig1)

# Average Calls by Churn
st.subheader("📞 Average Calls by Churn Status")
call_features = ["CustomerCareCalls", "ThreewayCalls", "ReceivedCalls", "OutboundCalls"]
avg_calls = df.groupby("Churn")[call_features].mean().T
st.bar_chart(avg_calls)

# Monthly Minutes Distribution by Churn
st.subheader("🕒 Monthly Minutes Distribution by Churn")
fig2, ax2 = plt.subplots()

# Drop NaNs for MonthlyMinutes
df_clean_minutes = df.dropna(subset=["MonthlyMinutes", "Churn"])

sns.histplot(
    data=df_clean_minutes, x="MonthlyMinutes", hue="Churn", bins=50, kde=True, ax=ax2
)
ax2.set_xlabel("Monthly Minutes")
st.pyplot(fig2)

# Feature: Service Area vs Churn
st.subheader("🌍 Churn Rate by Service Area")
if "ServiceArea" in df.columns:
    df_area = df.dropna(subset=["ServiceArea", "Churn"])
    churn_area = (
        pd.crosstab(df_area["ServiceArea"], df_area["Churn"], normalize="index") * 100
    )
    st.dataframe(churn_area.style.format("{:.2f}"))

# User Prediction
st.header("🤖 Predict Churn for a New Customer")
user_input = st.text_input(
    "Enter comma-separated values for a customer (matching model features):"
)
if st.button("Predict"):
    try:
        input_data = pd.DataFrame(
            [eval(user_input)], columns=df.drop("Churn", axis=1).columns
        )
        prediction = predict_churn(model, input_data)
        st.success(f"Churn Prediction: {'Yes' if prediction[0] else 'No'}")
    except Exception as e:
        st.error(f"Error: {e}")
