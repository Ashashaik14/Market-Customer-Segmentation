from sklearn.cluster import KMeans


def apply_kmeans(data, n_clusters=5):

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(data)

    return model, clusters