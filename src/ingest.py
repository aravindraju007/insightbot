import pandas as pd
import sqlalchemy

def load_csv(file_path):
    """
    Load data from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"[✓] Loaded CSV: {file_path} ({df.shape[0]} rows, {df.shape[1]} columns)")
        return df
    except Exception as e:
        print(f"[!] Failed to load CSV: {e}")
        return None

def load_excel(file_path, sheet_name=0):
    """
    Load data from an Excel file.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"[✓] Loaded Excel: {file_path} ({df.shape[0]} rows, {df.shape[1]} columns)")
        return df
    except Exception as e:
        print(f"[!] Failed to load Excel: {e}")
        return None

def load_sql_query(db_path, query):
    """
    Load data from a SQL database using a custom query.
    """
    try:
        engine = sqlalchemy.create_engine(f"sqlite:///{db_path}")
        df = pd.read_sql_query(query, engine)
        print(f"[✓] Executed query on {db_path} ({df.shape[0]} rows, {df.shape[1]} columns)")
        return df
    except Exception as e:
        print(f"[!] Failed to execute query: {e}")
        return None
