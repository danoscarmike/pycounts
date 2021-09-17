import matplotlib.pyplot as plt


def plot_words(word_counts, n=10):
    """Creates a bar chart of the top `n` most common words in `word_counts`.

    Parameters
    ----------
    word_counts : `collections.Counter`
        Counter object of words. Typically output by the `pycounts.pycounts.count_words` method.
    n : int, optional
        Number of top words to include, by default 10.

    Returns
    -------
    `matplotlib.container.BarContainer`
        A bar chart rendered by `matplotlib.pyplot.bar`.
    
    Examples
    --------
    >>> from pycounts.pycounts import count_words
    >>> from pycounts.plotting import plot_words
    >>> word_counts = count_words("text.txt")
    >>> plot_words(word_counts)
    """
    word, count = zip(*word_counts.most_common(n))
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Count")
    return fig
