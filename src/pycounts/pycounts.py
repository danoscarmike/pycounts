from collections import Counter
from string import punctuation


def load_text(file_name):
    """Reads text from file.

    Parameters
    ----------
    file_name : string 
        Path to file containing the subject text.

    Returns
    -------
    string
        File text as a string.
    
    Examples
    --------
    >>> load_text("text.txt")
    """
    with open(file_name, "r") as f:
        text = f.read()
    return text


def clean_text(text):
    '''Converts text to lower case and removes common punctuation marks.

    Parameters
    ----------
    text : string
        Text string to clean.

    Returns
    -------
    string
        Cleaned text.

    Examples
    --------
    >>> clean_text("Howdy, partner!")
    'howdy partner'
    '''
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(file_name):
    """Counts occurances of words in a given text file.

    Text is converted to lower case, and common punctuation
    is removed before counting.

    Parameters
    ----------
    file_name : string
        Path to file containing the subject text.

    Returns
    -------
    `collections.Counter`
        Counter of words in text file.

    Examples
    --------
    >>> count_words("text.txt")
    """
    text = load_text(file_name)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
