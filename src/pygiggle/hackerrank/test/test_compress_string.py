"""Tests for Compress the String challenge from HackerRank."""

import pytest

from ..compress_string import compress


@pytest.mark.parametrize("string,expected", [
    ("1222311", "(1, 1) (3, 2) (1, 3) (2, 1)"),
    ("22222222222222222222", "(20, 2)")
])
def test_compress(string: str, expected: str):
    """It should return the expected output."""
    assert compress(string) == expected
