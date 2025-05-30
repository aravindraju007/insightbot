import pandas as pd
import numpy as np

def handle_missing_values(df, strategy="drop"):
    if strategy == "drop":
        return df.dropna()
    elif strategy == "mean":
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == "median":
        return df.fillna(df.median(numeric_only=True))
    else:
        raise ValueError("Unsupported strategy. Choose from: drop, mean, median.")

def remove_duplicates(df):
    return df.drop_duplicates()

def convert_dtypes(df):
    return df.convert_dtypes()

def standardize_column_names(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df
