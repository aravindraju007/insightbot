import pandas as pd

def get_summary_statistics(df):
    """
    Returns basic summary statistics for numeric columns.
    """
    return df.describe()

def get_value_counts(df, columns=None):
    """
    Returns value counts for specified columns. If none specified, does all object/categorical columns.
    """
    if columns is None:
        columns = df.select_dtypes(include=["object", "category"]).columns
    return {col: df[col].value_counts() for col in columns}

def get_correlations(df, method="pearson"):
    """
    Returns a correlation matrix for numeric columns.
    """
    return df.corr(method=method)

def get_missing_data_info(df):
    """
    Returns a summary of missing values per column.
    """
    missing = df.isnull().sum()
    percent = (missing / len(df)) * 100
    return pd.DataFrame({'missing_values': missing, 'percent_missing': percent}).sort_values(by='percent_missing', ascending=False)

def get_column_types(df):
    """
    Returns a summary of column data types and unique counts.
    """
    return pd.DataFrame({
        'dtype': df.dtypes,
        'unique_values': df.nunique()
    })
