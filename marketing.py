# -*- coding: utf-8 -*-
"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("marketing_campaign(1).csv", delimiter=';', engine='python')
print(df.columns)
df = df.rename(columns={
    "NumWebVisitsMonth": "Impressions",
    "NumWebPurchases": "clicks",
    "NumStorePurchases": "Conversions",
    "Z_Revenue": "Revenue",
    "Z_CostContact": "Cost"
})

# Display first rows
print(df.head())

# Dataset information
print(df.info())
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# KPI CALCULATIONS (IMPORTANT)
# -----------------------------
df["CTR"] = (df["clicks"] / df["Impressions"]) * 100
df["Conversion_Rate"] = (df["Conversions"] / df["clicks"]) * 100
df["ROI"] = ((df["Revenue"] - df["Cost"]) / df["Cost"]) * 100

# -----------------------------
# CAMPAIGN PERFORMANCE ANALYSIS
# -----------------------------
campaign_kpis = {}
campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']

for col in campaign_cols:
    # Filter for customers who accepted the campaign
    accepted_campaign_df = df[df[col] == 1]
    if not accepted_campaign_df.empty:
        campaign_kpis[col] = {
            'Revenue': accepted_campaign_df['Revenue'].mean(),
            'ROI': accepted_campaign_df['ROI'].mean()
        }

campaign_summary = pd.DataFrame(campaign_kpis).T
print("\nCampaign Performance Summary by Accepted Campaign:")
print(campaign_summary)

# -----------------------------
# VISUALIZATION 1: Revenue by Accepted Campaign
# -----------------------------
campaign_summary["Revenue"].plot(kind="bar")
plt.title("Average Revenue by Accepted Campaign")
plt.xlabel("Campaign")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# VISUALIZATION 2: ROI by Accepted Campaign
# -----------------------------
campaign_summary["ROI"].plot(kind="bar")
plt.title("Average ROI by Accepted Campaign")
plt.xlabel("Campaign")
plt.ylabel("ROI (%)")
plt.show()

# -----------------------------
# CHANNEL PERFORMANCE ANALYSIS (Removed as 'Channel' column not available)
# -----------------------------
# VISUALIZATION 3: Conversions by Channel (Removed as 'Channel' column not available)
# -----------------------------

# -----------------------------
# VISUALIZATION 4: Cost vs Revenue
# -----------------------------
plt.scatter(df["Cost"], df["Revenue"])
plt.title("Cost vs Revenue Analysis")
plt.xlabel("Campaign Cost")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# TIME-BASED ANALYSIS (Optional but Modern)
# -----------------------------
if "Start_Date" in df.columns:
    df["Start_Date"] = pd.to_datetime(df["Start_Date"])
    monthly_revenue = df.groupby(df["Start_Date"].dt.month)["Revenue"].sum()

    monthly_revenue.plot()
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()
