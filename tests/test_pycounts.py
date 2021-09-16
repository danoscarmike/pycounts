from collections import Counter
from pycounts import pycounts


def test_count_words():
    """Test word counting from a file."""
    expected = Counter(
        {
            "insanity": 1,
            "is": 1,
            "doing": 1,
            "the": 1,
            "same": 1,
            "thing": 1,
            "over": 2,
            "and": 2,
            "expecting": 1,
            "different": 1,
            "results": 1,
        }
    )
    actual = pycounts.count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"