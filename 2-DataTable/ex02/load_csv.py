import pandas as pd


def load(path: str):
    if path is None:
        return None
    df = pd.read_csv(path, index_col=0)
    print("Loading dataset of dimensions ", df.shape)
    return df
