import pandas as pd
from roktools.gnss.types import ConstellationId, TrackingChannel

def compute_geometry_free(data: pd.DataFrame, constellation: ConstellationId, channel_a: TrackingChannel, channel_b: TrackingChannel) -> pd.DataFrame:
    """
    Compute the geometry (ionospheric free combination)
    """

    columns = ['epoch', 'constellation', 'sat', 'channel', 'range', 'phase', 'slip']

    # Create a new dataframe
    df = data[columns].copy()

    # Create subsets of the DataFrame corresponding to the constellation and each of
    # the channels selected to build the ionospheric combination
    df_a = df[(df['constellation'] == constellation) & (df['channel'] == str(channel_a))]
    df_b = df[(df['constellation'] == constellation) & (df['channel'] == str(channel_b))]

    # Compute the wavelength of the two tracking channels
    wl_a = channel_a.get_wavelength(constellation)
    wl_b = channel_b.get_wavelength(constellation)

    # Use merge to join the two tables
    df_out = pd.merge(df_a, df_b, on=['epoch', 'sat'], how='inner', suffixes=('_a', '_b'))
    df_out['li_m'] = df_out['phase_a'] * wl_a - df_out['phase_b'] * wl_b
    df_out['pi_m'] = df_out['range_b'] - df_out['range_a']

    return df_out

def compute_code_minus_carrier(data: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the geometry (ionospheric free combination)
    """

    # Create a new dataframe
    df = data.copy()

    # Compute the wavelength
    df['wl'] = df.apply(lambda row : TrackingChannel.from_string(row['channel']).get_wavelength(row['constellation']), axis=1)

    df['cmc'] = df['range'] - df['phase'] * df['wl']

    return df
