# src/data_loader.py

import pandas as pd


def load_news_data(filepath: str) -> pd.DataFrame:
    """
    Load the financial news dataset from CSV and standardize column names.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Raw loaded dataframe.
    """
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = [col.strip().lower() for col in df.columns]

    # Ensure expected columns exist
    expected_cols = {"headline", "url", "publisher", "date", "stock"}
    missing = expected_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df

















# import pandas as pd

# def load_news_data(path: str) -> pd.DataFrame:
#     """
#     Load financial news dataset from CSV/JSON/Parquet and preprocess.
#     """
#     if path.endswith(".csv"):
#         df = pd.read_csv(path)
#     elif path.endswith(".json"):
#         df = pd.read_json(path)
#     elif path.endswith(".parquet"):
#         df = pd.read_parquet(path)
#     else:
#         raise ValueError("Unsupported file format. Use CSV, JSON, or Parquet.")

#     # Expected columns based on YOUR dataset
#     required_cols = ["headline", "publisher", "date"]
#     missing = [c for c in required_cols if c not in df.columns]
#     if missing:
#         raise ValueError(f"Missing required columns: {missing}")

#     # Convert date to datetime
#     df["date"] = pd.to_datetime(df["date"], errors="coerce")
#     df = df.dropna(subset=["date"])

#     # Standardize column name (optional but recommended)
#     df = df.rename(columns={"date": "published_at"})

#     # Remove duplicates
#     df = df.drop_duplicates()

#     return df
