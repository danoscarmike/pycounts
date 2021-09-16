import matplotlib.pyplot as plt


def plot_words(word_counts, n=10):
    """Creates a `matplotlib.pyplot.bar` chart of the top
       `n` most common words in `word_counts`

    Args:
        word_counts (`collections.Counter`): Counter object of words.
        Typically output by the `pycounts.pycounts.count_words` method.
        n (int, optional): Number of words to include. Defaults to 10.

    Returns:
        `matplotlib.pyplot.bar`: matplotlib figure
    """
    word, count = zip(*word_counts.most_common(n))
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Count")
    return fig
