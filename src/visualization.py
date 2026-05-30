import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plot_elbow_method(data, output_path):

    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(
            n_clusters=i,
            random_state=42,
            n_init=10
        )

        kmeans.fit(data)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), wcss, marker='o')
    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.savefig(output_path)
    plt.close()


def plot_customer_clusters(df, clusters, output_path):

    plt.figure(figsize=(8, 6))

    scatter = plt.scatter(
        df["Annual Income (k$)"],
        df["Spending Score (1-100)"],
        c=clusters
    )

    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.title("Customer Segmentation")

    plt.colorbar(scatter)

    plt.savefig(output_path)
    plt.close()


def plot_clusters(data, clusters, output_path):

    plt.figure(figsize=(8, 6))

    scatter = plt.scatter(
        data[:, 0],
        data[:, 1],
        c=clusters
    )

    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.title("PCA Customer Segmentation")

    plt.colorbar(scatter)

    plt.savefig(output_path)
    plt.close()