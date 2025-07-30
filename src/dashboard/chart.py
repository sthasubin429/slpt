import streamlit as st
import matplotlib.pyplot as plt

import numpy as np
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.graph_objects as go

def stats(df):
    total_customers = len(df)
    churn_counts = df["Churn"].value_counts()
    churned_customers = (
      churn_counts.get("Yes", 0)
      if df["Churn"].dtype == object
      else churn_counts.get(1, 0)
    )
    churn_rate = churned_customers / total_customers * 100 if total_customers else 0
    avg_monthly_revenue = df["MonthlyRevenue"].mean()
    avg_monthly_minutes = df["MonthlyMinutes"].mean()
    retention_calls = df[df["RetentionCalls"] == 1]
    total_retention_calls = len(retention_calls)
    retention_offers_accepted = retention_calls["RetentionOffersAccepted"].sum()
    retention_offer_success_rate = (
      retention_offers_accepted / total_retention_calls * 100 if total_retention_calls else 0
    )

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Total Customers", f"{total_customers:,}")
    col2.metric("Churned Customers", f"{churned_customers:,}")
    col3.metric("Churn Rate", f"{churn_rate:.2f}%")
    col4.metric("Avg. Monthly Revenue", f"${avg_monthly_revenue:,.2f}")
    col5.metric("Avg. Monthly Minutes", f"{avg_monthly_minutes:,.2f}")
    col6.metric("Retention Offer Success Rate", f"{retention_offer_success_rate:.2f}%")

def churn_overview_chart(df, pastel_palette):
    st.markdown("#### Churn Overview")
    churn_counts = df["Churn"].value_counts()

    fig = go.Figure(
      data=[
        go.Pie(
          labels=churn_counts.index,
          values=churn_counts.values,
          marker=dict(colors=pastel_palette[: len(churn_counts)]),
          hole=0.3,
          textinfo="percent+label",
        )
      ]
    )
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)


def churn_by_location(df, pastel_palette):
    st.markdown("#### Churn by Location")
    churn_labels = df["Churn"].unique()
    fig = make_subplots(rows=1, cols=len(churn_labels), subplot_titles=[f"Churn: {label}" for label in churn_labels], specs=[[{"type": "domain"}]*len(churn_labels)])

    for i, churn_status in enumerate(churn_labels):
      credit_counts = df[df["Churn"] == churn_status]["PrizmCode"].value_counts()
      fig.add_trace(
        go.Pie(
          labels=credit_counts.index,
          values=credit_counts.values,
          marker=dict(colors=pastel_palette[: len(credit_counts)]),
          hole=0.4,
          textinfo="percent+label"
        ),
        row=1,
        col=i+1
      )

    fig.update_layout(height=350, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


def monthly_revenue_vs_months_chart(df, pastel_palette):
    st.markdown("#### Avg. Revenue vs. Months in Service")
    avg_revenue = (
        df.groupby(["MonthsInService", "Churn"])["MonthlyRevenue"]
        .mean()
        .reset_index()
        .pivot(index="MonthsInService", columns="Churn", values="MonthlyRevenue")
    )
    st.line_chart(
        avg_revenue,
        use_container_width=True,
        color=pastel_palette[: len(avg_revenue.columns)],
    )


def credit_rating_distribution_chart(df, pastel_palette):
    st.markdown("#### Credit Rating Distribution")
    credit_rating_counts = (
        df.groupby(["CreditRatingLabel", "Churn"]).size().reset_index(name="Count")
    )
    credit_rating_pivot = credit_rating_counts.pivot(
        index="CreditRatingLabel", columns="Churn", values="Count"
    ).fillna(0)
    st.area_chart(
        credit_rating_pivot,
        use_container_width=True,
        color=pastel_palette[: len(credit_rating_pivot.columns)],
    )


def retention_team_calls_vs_churn_chart(df, pastel_palette):
    st.markdown("#### Retention Team Calls vs. Churn")

    retention_labels = df["MadeCallToRetentionTeam"].unique()
    fig = make_subplots(
      rows=1,
      cols=len(retention_labels),
      subplot_titles=[f"Made Call: {label}" for label in retention_labels],
      specs=[[{"type": "domain"}] * len(retention_labels)],
    )

    for i, made_call in enumerate(retention_labels):
      subset = df[df["MadeCallToRetentionTeam"] == made_call]
      churn_counts = subset["Churn"].value_counts()
      total = churn_counts.sum()
      churn_rate = (
        churn_counts.get("Yes", churn_counts.get(1, 0)) / total * 100
        if total else 0
      )
      fig.add_trace(
        go.Pie(
          labels=churn_counts.index,
          values=churn_counts.values,
          marker=dict(colors=pastel_palette[: len(churn_counts)]),
          hole=0.4,
          textinfo="percent+label",
          title=dict(
            text=f"{churn_rate:.2f}%",
            font=dict(size=24),
          ),
        ),
        row=1,
        col=i + 1,
      )

    fig.update_layout(height=350, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


def average_calls_by_churn_chart(df, pastel_palette):
    st.markdown("#### Average Calls by Churn Status")
    call_features = [
        "DroppedCalls",
        "CustomerCareCalls",
        "ThreewayCalls",
        "ReceivedCalls",
        "OutboundCalls",
        "InboundCalls",
    ]
    avg_calls = df.groupby("Churn")[call_features].mean().T
    st.bar_chart(avg_calls, color=pastel_palette[: len(avg_calls.columns)])


def monthly_revenue_distribution_chart(df, pastel_palette):
    st.markdown("#### Monthly Revenue Distribution by Churn Status")
    df_clean_revenue = df.dropna(subset=["MonthlyRevenue", "Churn"])
    churn_labels = df_clean_revenue["Churn"].unique()
    hist_data = [
        df_clean_revenue[df_clean_revenue["Churn"] == label]["MonthlyRevenue"]
        for label in churn_labels
    ]
    group_labels = [f"Churn: {label}" for label in churn_labels]

    fig = make_subplots(rows=1, cols=len(churn_labels), subplot_titles=group_labels)
    for i, (data, label) in enumerate(zip(hist_data, group_labels)):
        dist_fig = ff.create_distplot(
            [data],
            [label],
            bin_size=5,
            show_hist=True,
            show_rug=False,
            colors=[pastel_palette[i % len(pastel_palette)]],
        )
        for trace in dist_fig["data"]:
            fig.add_trace(trace, row=1, col=i + 1)

    fig.update_layout(
        showlegend=True,
        xaxis_title="Monthly Revenue",
        yaxis_title="Density",
        height=400,
    )
    for i in range(len(churn_labels)):
        fig["layout"][f"xaxis{i+1}"]["title"] = "Monthly Revenue"
        fig["layout"][f"yaxis{i+1}"]["title"] = "Density"

    st.plotly_chart(fig, use_container_width=True)
