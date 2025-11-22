import pandas as pd
import re


def count_articles_by_publisher(df: pd.DataFrame):
    return df["publisher"].value_counts()


def extract_publisher_domains(df: pd.DataFrame):
    def extract(email):
        match = re.search(r"@([A-Za-z0-9.-]+\.[A-Za-z]{2,})", str(email))
        return match.group(1) if match else None

    df["publisher_domain"] = df["publisher"].apply(extract)
    return df


def compare_publishers(df: pd.DataFrame):
    df["word_len"] = df["headline"].apply(lambda x: len(str(x).split()))
    return df.groupby("publisher")["word_len"].mean().sort_values(ascending=False)
