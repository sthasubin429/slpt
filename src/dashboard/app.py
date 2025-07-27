import streamlit as st
import pandas as pd
from utils import load_processed_data, load_model, predict_churn

st.title("Telecom Churn Dashboard")

# Load data and model
df = load_processed_data()
model = load_model()

st.write("## Data Preview")
st.dataframe(df.head())

st.write("## Predict Churn")
user_input = st.text_input(
    "Enter comma-separated values for a customer (matching model features):"
)
if st.button("Predict"):
    try:
        input_data = pd.DataFrame(
            [eval(user_input)], columns=df.drop("Churn", axis=1).columns
        )
        prediction = predict_churn(model, input_data)
        st.write(f"Churn Prediction: {'Yes' if prediction[0] else 'No'}")
    except Exception as e:
        st.error(f"Error: {e}")
