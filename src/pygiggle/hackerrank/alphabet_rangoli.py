"""Alphabet Rangoli challenge from HackerRank."""

import string


def rangoli(size: int) -> str:
    """Return an Alphabet Rangoli of specified [size]."""
    assert size <= len(string.ascii_lowercase)

    letters = string.ascii_lowercase[:size]
    mid_row = size
    num_rows = size * 2 - 1

    rangoli_lines = []

    for row in range(1, num_rows + 1):
        distance_from_mid = abs(mid_row - row)
        row_letters_right = letters[distance_from_mid:]
        # letters on the left are same as all but first on right reversed
        row_letters = (
            list(reversed(row_letters_right[1:])) + list(row_letters_right)
        )
        # pad row letters to size using `-`
        padding = ["-"] * (size - len(row_letters_right))
        if padding:
            row_letters = padding + row_letters + padding
        row_str = "-".join(row_letters)
        rangoli_lines.append(row_str)

    return "\n".join(rangoli_lines)
