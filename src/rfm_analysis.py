import pandas as pd


def create_rfm_features(df):

    rfm = pd.DataFrame()

    rfm["CustomerID"] = df["CustomerID"]

    # Simulated RFM features
    rfm["Recency"] = 100 - df["Spending Score (1-100)"]
    rfm["Frequency"] = df["Age"] // 5
    rfm["Monetary"] = df["Annual Income (k$)"]

    return rfm