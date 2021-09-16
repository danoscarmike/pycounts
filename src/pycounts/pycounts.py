from collections import Counter
from string import punctuation


def load_text(file_name):
    with open(file_name, "r") as f:
        text = f.read()
    return text


def clean_text(text):
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(file_name):
    text = load_text(file_name)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
