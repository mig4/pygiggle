"""Compress the String challenge from HackerRank."""

import itertools


def main():
    """CLI interface."""
    string = input()
    print(compress(string))


def compress(string: str) -> str:
    """Return string represented as tuples of characters and their count."""
    return " ".join([
        "({})".format(", ".join((str(len(list(grp))), char)))
        for char, grp in itertools.groupby(string, lambda c: c)
    ])


if __name__ == "__main__":
    main()
