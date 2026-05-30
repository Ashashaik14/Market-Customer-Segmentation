from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def perform_pca(data):

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    pca = PCA(n_components=2)

    pca_result = pca.fit_transform(scaled_data)

    return pca_result   