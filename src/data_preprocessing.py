import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)

    encoder = LabelEncoder()
    df["Gender"] = encoder.fit_transform(df["Gender"])

    return df