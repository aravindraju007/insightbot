import pandas as pd
import os

def preview_dataframe(df, rows=5):
    """
    Prints the head and tail of a DataFrame with shape info.
    """
    if not isinstance(df, pd.DataFrame):
        print("[!] Provided object is not a DataFrame.")
        return

    print(f"[i] DataFrame shape: {df.shape}")
    print(f"\n[i] First {rows} rows:")
    print(df.head(rows))
    print(f"\n[i] Last {rows} rows:")
    print(df.tail(rows))

def save_dataframe(df, file_path):
    """
    Save DataFrame to a CSV file.
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"[✓] DataFrame saved to {file_path}")
    except Exception as e:
        print(f"[!] Failed to save DataFrame: {e}")

def check_file_exists(path):
    """
    Check if a file exists at the given path.
    """
    exists = os.path.exists(path)
    print(f"[✓] File exists: {path}" if exists else f"[!] File not found: {path}")
    return exists

def print_separator(label=None):
    """
    Print a formatted separator for console output.
    """
    print("\n" + "=" * 60)
    if label:
        print(f"[ {label.upper()} ]")
        print("-" * 60)

def list_columns(df):
    """
    List column names and data types.
    """
    print_separator("DataFrame Columns")
    print(df.dtypes)

