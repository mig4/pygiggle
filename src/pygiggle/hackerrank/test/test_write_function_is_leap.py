"""Tests for is_leap function from HackerRank Write a Function challenge."""

import pytest

from ..write_function_is_leap import is_leap


@pytest.mark.parametrize("year,expected", [
    (1800, False),
    (1900, False),
    (1990, False),
    (2000, True),
    (2100, False),
    (2200, False),
    (2300, False),
    (2400, True),
    (2500, False),
])
def test_it_determines_leap_year_correctly(year, expected):
    """it determines the leap year correctly"""
    assert is_leap(year) is expected
