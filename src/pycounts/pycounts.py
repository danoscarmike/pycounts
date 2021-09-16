from collections import Counter
from string import punctuation


def load_text(file_name):
    """Reads text from file.

    Args:
        file_name (`str`): Path to file containing the subject text.

    Returns:
        `str`: Text as a string.
    """
    with open(file_name, "r") as f:
        text = f.read()
    return text


def clean_text(text):
    """Converts text to lower case and removes common
       punctuation marks.

    Args:
        text (`str`): Text string to clean.

    Returns:
        `str`: Cleaned text.
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(file_name):
    """Counts occurances of words in a given text file.

    Text is converted to lower case, and common punctuation
    is removed before counting.

    Args:
        file_name (`str`): Path to file containing the subject text.

    Returns:
        `collections.Counter`: Counter of words in text file.

    Example:
        ```python
        import matplotlib.pyplot as plt

        from pycounts.pycounts import count_words
        from pycounts.plotting import plot_words

        file_path = "path to your text file"
        word_counts = count_words(file_path)
        fig = plot_words(word_counts)
        plt.show()
        ```
    """
    text = load_text(file_name)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
