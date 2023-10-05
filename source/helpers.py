from typing import Iterable
import numpy as np
import pandas as pd


def compute_elapsed_seconds(epochs:pd.Series) -> pd.Series:
    return (epochs - epochs.iloc[0]).dt.total_seconds()

def compute_rms(values:Iterable) -> float:
    return np.sqrt(np.mean(np.square(values)))
