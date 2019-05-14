"""Validate Email Address with a Filter challenge from HackerRank."""

import re


EMAIL_RE = re.compile(r"[\w-]+@[a-zA-Z0-9]+\.[\w]{0,3}$")


def fun(string) -> bool:
    """return True if s is a valid email, else return False."""
    return EMAIL_RE.match(string) is not None
