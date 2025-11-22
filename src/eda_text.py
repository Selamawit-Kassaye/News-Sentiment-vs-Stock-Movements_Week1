import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from collections import Counter
from utils import clean_text


def compute_headline_lengths(df: pd.DataFrame) -> pd.DataFrame:
    df["char_len"] = df["headline"].astype(str).apply(len)
    df["word_len"] = df["headline"].astype(str).apply(lambda x: len(x.split()))
    return df


def get_common_keywords(df: pd.DataFrame, top_n=20):
    all_words = []
    for text in df["headline"]:
        words = clean_text(str(text)).split()
        all_words.extend(words)

    counter = Counter(all_words)
    return counter.most_common(top_n)


def perform_topic_modeling(df: pd.DataFrame, n_topics=5, max_features=5000):
    cleaned = df["headline"].astype(str).apply(clean_text)

    vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
    X = vectorizer.fit_transform(cleaned)

    nmf = NMF(n_components=n_topics, random_state=42)
    W = nmf.fit_transform(X)
    H = nmf.components_

    vocab = vectorizer.get_feature_names_out()
    topics = []

    for i, topic_weights in enumerate(H):
        top_words_idx = topic_weights.argsort()[-10:][::-1]
        topics.append({
            "topic": i,
            "keywords": [vocab[j] for j in top_words_idx]
        })

    return topics
