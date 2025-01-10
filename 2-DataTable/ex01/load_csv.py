import pandas as pd


def load(path: str):
    """
    Loads a dataset from a CSV file and prints its dimensions.
    """
    if path is None:
        return None
    df = pd.read_csv(path, index_col=0)
    print("Loading dataset of dimensions ", df.shape)
    return df
