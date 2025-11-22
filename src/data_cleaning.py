# src/data_cleaning.py

import pandas as pd


def clean_news_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the financial news dataframe.

    Steps:
    -------
    - Drop rows missing headline, publisher, or date
    - Strip whitespace
    - Normalize publisher text
    - Remove invalid dates
    - Add headline length
    - Extract publication day & hour
    - Extract publisher email domain (if present)

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe ready for EDA.
    """

    # Drop missing essential values
    df = df.dropna(subset=["headline", "publisher", "date"])

    # Clean headline & publisher strings
    df["headline"] = df["headline"].astype(str).str.strip()
    df["publisher"] = df["publisher"].astype(str).str.strip().str.lower()

    # Remove invalid date rows
    df = df[df["date"].notna()]

    # Add headline length column
    df["headline_length"] = df["headline"].str.len()

    # Extract date-only column
    df["pub_day"] = df["date"].dt.date

    # Extract publishing hour (if timestamp includes time)
    df["pub_hour"] = df["date"].dt.hour

    # Optional: Extract domain from publisher if formatted like email
    df["publisher_domain"] = df["publisher"].str.extract(r"@([\w\.-]+)")

    return df
