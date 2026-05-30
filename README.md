# Market Customer Segmentation Using Machine Learning

## 📌 Project Overview

This project performs customer segmentation using Machine Learning techniques to identify groups of customers with similar purchasing behavior. The segmentation helps businesses design targeted marketing campaigns and improve customer engagement.

The project uses RFM (Recency, Frequency, Monetary) Analysis, K-Means Clustering, and Principal Component Analysis (PCA) to analyze customer data and generate meaningful customer segments.

---

## 🎯 Objectives

- Analyze customer behavior using RFM metrics.
- Segment customers into different groups using K-Means Clustering.
- Visualize customer segments using PCA.
- Generate cluster reports and customer insights.
- Support data-driven marketing strategies.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

## 📂 Project Structure

```text
Market_Customer_Segmentation/
│
├── dataset/
│   └── Mall_Customers.csv
│
├── outputs/
│   ├── elbow_method.png
│   ├── customer_clusters.png
│   ├── pca_clusters.png
│   ├── cluster_report.csv
│   └── cluster_summary.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── rfm_analysis.py
│   ├── pca_analysis.py
│   ├── clustering.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Features

- Data Preprocessing
- RFM Analysis
- Customer Segmentation
- K-Means Clustering
- PCA Dimensionality Reduction
- Data Visualization
- Cluster Summary Generation
- Marketing Insights

---

## 🔄 Workflow

1. Load customer dataset
2. Preprocess customer data
3. Generate RFM features
4. Apply K-Means Clustering
5. Perform PCA for visualization
6. Generate cluster reports
7. Visualize customer segments
8. Extract business insights

---

## 📈 Generated Outputs

### 1. Elbow Method
Determines the optimal number of customer clusters.

### 2. Customer Cluster Visualization
Displays customer groups based on Annual Income and Spending Score.

### 3. PCA Cluster Visualization
Shows customer segments in a reduced two-dimensional space.

### 4. Cluster Report
Contains customer-wise cluster assignments.

### 5. Cluster Summary
Provides average Recency, Frequency, Monetary values and customer counts for each cluster.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Market-Customer-Segmentation.git
```

Move into the project directory:

```bash
cd Market-Customer-Segmentation
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## 📋 Sample Output

```text
CUSTOMER SEGMENTATION REPORT

Customer Data:
CustomerID  Recency  Frequency  Monetary  Cluster

CLUSTER SUMMARY

Cluster  Avg_Recency  Avg_Frequency  Avg_Monetary  Total_Customers
0        64.25        6.50           19.00         4
1        24.57        4.29           18.29         7
...
```

---

## 💡 Business Benefits

- Customer Behavior Analysis
- Personalized Marketing Campaigns
- Customer Retention Strategies
- High-Value Customer Identification
- Improved Business Decision-Making

---

## 📚 Machine Learning Concepts Used

- Data Preprocessing
- Feature Engineering
- RFM Analysis
- K-Means Clustering
- Principal Component Analysis (PCA)
- Data Visualization

---

## 👩‍💻 Author

**Asha Shaik**

B.Tech - Computer Science & Engineering

---

## ⭐ Future Enhancements

- Interactive Dashboard using Streamlit
- Advanced Customer Analytics
- Real-Time Customer Segmentation
- Additional Clustering Algorithms
- Automated Business Recommendations
