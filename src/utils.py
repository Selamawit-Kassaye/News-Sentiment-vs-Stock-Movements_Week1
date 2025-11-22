import re

def clean_text(text: str) -> str:
    """
    Basic text cleaning: lowercase, remove punctuation/numbers.
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.strip()
