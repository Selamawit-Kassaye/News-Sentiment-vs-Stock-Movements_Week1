import pandas as pd


def compute_publication_frequency(df: pd.DataFrame):
    return df.groupby(df["published_at"].dt.date).size()


def analyze_publish_time_of_day(df: pd.DataFrame):
    return df.groupby(df["published_at"].dt.hour).size()


def detect_spikes(df: pd.DataFrame, multiplier=2.0):
    freq = compute_publication_frequency(df)
    mean_val = freq.mean()
    std_val = freq.std()

    threshold = mean_val + multiplier * std_val
    spikes = freq[freq > threshold]
    return spikes
