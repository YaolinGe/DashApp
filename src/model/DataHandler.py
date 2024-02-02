"""
This module contains essential functions to handle the data.
"""
import pandas as pd


def preprocess_and_smooth(df):
    # Convert Time to total seconds
    df['Time'] = pd.to_timedelta(df['Time']).dt.total_seconds()

    # Round Time to nearest 0.01 second for synchronization
    df['Time'] = (df['Time'] * 100).round() / 100

    # Group by Time and average the Values for smoothing
    df = df.groupby('Time', as_index=False)['Value'].mean()
    return df
