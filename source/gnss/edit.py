import numpy as np
import pandas as pd

ARC_ID_FIELD = 'arc_id'

def compute_phase_arc_id(data: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the phase arc ID, that can be used later to perform operations
    on a per-arc basis (compute arc bias, ...)
    """

    data[ARC_ID_FIELD] = data.groupby('signal')['slip'].transform('cumsum')

    return data


def mark_time_gap(data: pd.DataFrame, threshold_s: float = 5) -> pd.DataFrame:
    """
    Mark a phase cycle slip when the time series show a time gap
    of a given threshold
    """

    # Function to mark epochs with a difference > threshold
    def mark_epochs(group):
        EPOCH_FIELD = 'epoch'
        marked = group[EPOCH_FIELD].diff() > pd.Timedelta(seconds=threshold_s)
        return marked

    # Apply the function per group using groupby
    marked_epochs = data.groupby('signal').apply(mark_epochs)

    data['slip'] = np.any([data['slip'], marked_epochs], axis=0)

    data = compute_phase_arc_id(data)

    return data

def detrend(data:pd.DataFrame, observable: str, n_samples:int) -> pd.DataFrame:
    """
    Detrend a given observable by using a rolling window of a certain number of
    samples
    """

    trend_column = f'{observable}_trend'
    detrended_column = f'{observable}_detrended'

    trend = data.groupby(['signal', ARC_ID_FIELD])[observable].transform(lambda x: x.rolling(n_samples).mean())
    data[trend_column] = trend
    data[detrended_column] = data[observable] - data[trend_column]

    return data

def remove_mean(data: pd.DataFrame, observable: str) -> pd.DataFrame:

    bias_field = f'{observable}_bias'
    aligned_field = f'{observable}_aligned'

    # For each arch id, compute the median
    data[bias_field] = data.groupby(['signal',ARC_ID_FIELD])[observable].transform('mean')

    data[aligned_field] = data[observable] - data[bias_field]

    return data
