"""is_leap function from HackerRank Write a Function challenge."""


def is_leap(year: int) -> bool:
    """Return true if year is a leap year."""
    leap = False

    if _is_divisible_by(year, 4):
        leap = True
        if _is_divisible_by(year, 100):
            leap = False
            if _is_divisible_by(year, 400):
                leap = True

    return leap


def _is_divisible_by(num: int, divisor: int) -> bool:
    """Return true if [num] is evenly divisible by [divisor]."""
    return num % divisor == 0
