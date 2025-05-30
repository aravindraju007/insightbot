#!/usr/bin/env python3
"""
main.py  ▸  InsightBot MVP runner
---------------------------------
Example:
    python main.py --file data/titanic.csv --ingest csv --clean mean
"""

import argparse
import sys
from pathlib import Path

# ── Internal modules ────────────────────────────────────────────────────────────
from src.ingest    import load_csv, load_excel, load_sql_query
from src.clean     import handle_missing_values, remove_duplicates, convert_dtypes, standardize_column_names
from src.analyze   import (
    get_summary_statistics,
    get_missing_data_info,
    get_correlations,
    get_column_types,
)
from src.visualize import (
    plot_histogram,
    plot_bar,
    plot_correlation_heatmap,
)
from src.utils     import preview_dataframe, print_separator, save_dataframe


# ── CLI arguments ───────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(description="Run the InsightBot data pipeline.")
    
    # Ingestion
    p.add_argument("--file",   required=True,  help="Path to CSV / Excel file OR SQLite DB.")
    p.add_argument("--ingest", required=True,  choices=["csv", "excel", "sql"],
                   help="Ingestion mode: csv | excel | sql")
    p.add_argument("--sheet",  default=0,      help="Excel sheet index/name (for --ingest excel).")
    p.add_argument("--query",  default="SELECT * FROM data;",
                   help="SQL query to run (for --ingest sql).")
    
    # Cleaning
    p.add_argument("--clean", default="drop", choices=["drop", "mean", "median"],
                   help="Missing-value strategy.")
    
    # Output
    p.add_argument("--save_clean", metavar="OUT_CSV",
                   help="If set, save the cleaned DataFrame to this CSV path.")
    
    return p.parse_args()


# ── Ingestion helpers ───────────────────────────────────────────────────────────
def ingest_data(args):
    if args.ingest == "csv":
        return load_csv(args.file)
    if args.ingest == "excel":
        return load_excel(args.file, sheet_name=args.sheet)
    if args.ingest == "sql":
        return load_sql_query(args.file, args.query)
    raise ValueError("Unknown ingestion mode.")


# ── Pipeline ────────────────────────────────────────────────────────────────────
def run_pipeline(args):
    df = ingest_data(args)
    if df is None:
        sys.exit("[x] Ingestion failed. Exiting.")
    
    print_separator("Raw Preview")
    preview_dataframe(df)

    # Cleaning
    df = standardize_column_names(df)
    df = handle_missing_values(df, strategy=args.clean)
    df = remove_duplicates(df)
    df = convert_dtypes(df)

    print_separator("After Cleaning")
    preview_dataframe(df)

    # Optionally save the cleaned dataset
    if args.save_clean:
        save_path = Path(args.save_clean)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_dataframe(df, save_path)

    # Analysis
    print_separator("Summary Statistics")
    print(get_summary_statistics(df))

    print_separator("Missing Data")
    print(get_missing_data_info(df))

    print_separator("Column Types & Uniques")
    print(get_column_types(df))

    print_separator("Correlation Matrix")
    corr = get_correlations(df)
    print(corr)

    # Visualization
    numeric_cols = df.select_dtypes(include="number").columns
    cat_cols     = df.select_dtypes(exclude="number").columns

    if len(numeric_cols) > 0:
        plot_histogram(df, numeric_cols[0])
        plot_correlation_heatmap(df)

    if len(cat_cols) > 0:
        plot_bar(df, cat_cols[0])


# ── Entrypoint ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    args = parse_args()
    run_pipeline(args)
