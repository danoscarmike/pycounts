from collections import Counter

from matplotlib.container import BarContainer

from pycounts.plotting import plot_words


def test_plot_words():
    counts = Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                      'the': 1, 'same': 1, 'thing': 1, 
                      'over': 2, 'and': 2, 'expecting': 1,
                      'different': 1, 'results': 1})
    fig = plot_words(counts)
    assert isinstance(fig, BarContainer)
    assert len(fig.datavalues) == 10
