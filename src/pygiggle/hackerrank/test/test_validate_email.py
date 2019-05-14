"""Tests for Validate Email Address with a Filter challenge from HackerRank."""

import pytest

from ..validate_email import fun


@pytest.mark.parametrize("email,expected", [
    ("lara@hackerrank.com", True),
    ("brian-23@hackerrank.com", True),
    ("britts_54@hackerrank.com", True),
    ("zeb@foo.me", True),
    ("zeb@foo9.me", True),
    ("zeb@foo.bar.me", False),
    ("z:b@foo.me", False),
    ("z+b@foo.me", False),
    ("zeb@fo-o.me", False),
    ("zeb@fo=o.me", False),
    ("zeb@foo.mewb", False),
])
def test_fun(email: str, expected: bool):
    """it validates emails according to spec"""
    assert fun(email) is expected
