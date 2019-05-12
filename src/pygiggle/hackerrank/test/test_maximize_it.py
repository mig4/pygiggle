"""Tests for Maximize It challenge from HackerRank."""

from ..maximize_it import Data, maximize_it


DATA = Data(3, 1000, [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]])


def test_it_finds_best_values():
    """it finds best values from lists resulting in max outcome."""
    assert maximize_it(DATA) == 206
