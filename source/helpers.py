import pandas as pd


def compute_elapsed_seconds(epochs:pd.Series) -> pd.Series:

    return (epochs - epochs[0]).dt.total_seconds()
