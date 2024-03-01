"""
This module contains essential functions to handle the data.
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def preprocess_and_smooth(df):
    # Convert Time to total seconds
    df['Time'] = pd.to_timedelta(df['Time']).dt.total_seconds()

    # Round Time to nearest 0.01 second for synchronization
    df['Time'] = (df['Time'] * 100).round() / 100

    # Group by Time and average the Values for smoothing
    df = df.groupby('Time', as_index=False)['Value'].mean()
    return df


def resample_timestamp(df):
    """
    Regularize the data to a uniform sampling rate of inherent frequency.
    """
    def convert_time_duration_to_seconds(time_str):
        """
        Convert a time duration string into total number of seconds as a float,
        handling various time formats.
        """
        # Check if the string represents a negative duration
        is_negative = time_str.startswith('-')
        if is_negative:
            # Remove the negative sign for parsing
            time_str = time_str[1:]

        expected_length = len("HH:MM:SS.ffffff")  # Length of the format without the trailing '0'
        time_str_adjusted = time_str[:expected_length]

        # List of formats to try
        formats = ["%H:%M:%S.%f", "%H:%M:%S", "%M:%S.%f", "%M:%S", "%S.%f", "%S"]

        # Attempt to parse the string with each format
        for fmt in formats:
            try:
                # Parse the time duration string with the current format
                parsed_time = datetime.strptime(time_str_adjusted, fmt)
                # Convert to timedelta
                delta = timedelta(hours=parsed_time.hour, minutes=parsed_time.minute,
                                  seconds=parsed_time.second, microseconds=parsed_time.microsecond)
                # Convert timedelta to total seconds as float
                total_seconds = delta.total_seconds()
                # Apply the negative sign if necessary
                if is_negative:
                    total_seconds = -total_seconds
                return total_seconds
            except ValueError:
                # If parsing fails, try the next format
                continue

        # If none of the formats work, raise an error
        raise ValueError(f"Time string '{time_str}' does not match any expected format.")

    df['Time'] = df['Time'].apply(convert_time_duration_to_seconds)

    return df


if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\nq9093\AppData\Local\Temp\CutFileParser\BobbenAccelerometerX.csv")
    ddf = resample_timestamp(df)

