"""Tests for Iterables and Iterators challenge from HackerRank."""

from ..iterables_probability import a_probability


def test_a_probability():
    """it computes probability of a in slices correctly"""
    assert round(a_probability(4, 2, ["a", "a", "b", "c"]), 4) == 0.8333
