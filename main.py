import os

from src.data_preprocessing import load_and_preprocess_data
from src.rfm_analysis import create_rfm_features
from src.pca_analysis import perform_pca
from src.clustering import apply_kmeans
from src.visualization import (
    plot_elbow_method,
    plot_clusters,
    plot_customer_clusters
)

os.makedirs("outputs", exist_ok=True)

df = load_and_preprocess_data("dataset/Mall_Customers.csv")

rfm = create_rfm_features(df)

plot_elbow_method(
    rfm[["Recency", "Frequency", "Monetary"]],
    "outputs/elbow_method.png"
)

model, clusters = apply_kmeans(
    rfm[["Recency", "Frequency", "Monetary"]],
    5
)

rfm["Cluster"] = clusters

plot_customer_clusters(
    df,
    clusters,
    "outputs/customer_clusters.png"
)

pca_data = perform_pca(
    rfm[["Recency", "Frequency", "Monetary"]]
)

plot_clusters(
    pca_data,
    clusters,
    "outputs/pca_clusters.png"
)

rfm.to_csv(
    "outputs/cluster_report.csv",
    index=False
)

print("\n" + "="*60)
print("CUSTOMER SEGMENTATION REPORT")
print("="*60)

print("\nCustomer Data:")
print(rfm)

summary = rfm.groupby("Cluster").agg({
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean",
    "CustomerID": "count"
}).round(2)

summary.rename(
    columns={"CustomerID": "Total_Customers"},
    inplace=True
)

print("\n" + "="*60)
print("CLUSTER SUMMARY")
print("="*60)

print(summary)

summary.to_csv(
    "outputs/cluster_summary.csv"
)

print("\nProject Completed Successfully!")