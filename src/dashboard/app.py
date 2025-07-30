import streamlit as st
import seaborn as sns

from chart import average_calls_by_churn_chart, churn_by_location, churn_overview_chart, credit_rating_distribution_chart, monthly_revenue_distribution_chart, monthly_revenue_vs_months_chart, retention_team_calls_vs_churn_chart, stats
from utils import load_processed_data, load_model
import numpy as np
import plotly.figure_factory as ff

st.set_page_config(
  layout="wide",
  page_title="Telecom Churn Dashboard",
  page_icon="📊",
  initial_sidebar_state="auto",
)

hide_streamlit_style = """
  <style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
  """
  <style>
  .stApp {
    background-color: #ffffff;
    color: #222222;
    padding-top: 0rem !important;
  }
  .block-container {
    padding-top: 0rem !important;
  }
  </style>
  """,
  unsafe_allow_html=True,
)
st.markdown(
  "<h1 style='text-align: center;'> Telecom Churn Dashboard</h1>",
  unsafe_allow_html=True,
)

# Pastel color palette
pastel_palette = sns.color_palette("pastel").as_hex()

# Load data and model
df = load_processed_data()
model = load_model()

stats(df)

row1 = st.columns(3, gap="large")
row2 = st.columns(3, gap="large")

# --- Row 1 ---
with row1[0]:
    churn_overview_chart(df, pastel_palette)
with row1[1]:
    churn_by_location(df, pastel_palette)
with row1[2]:
    monthly_revenue_vs_months_chart(df, pastel_palette)

# --- Row 2 ---
with row2[0]:
    credit_rating_distribution_chart(df, pastel_palette)
with row2[1]:
    retention_team_calls_vs_churn_chart(df, pastel_palette)
with row2[2]:
    average_calls_by_churn_chart(df, pastel_palette)

# --- Full Width: Revenue Distribution ---
monthly_revenue_distribution_chart(df, pastel_palette)
