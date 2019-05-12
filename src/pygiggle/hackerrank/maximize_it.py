"""Maximize It challenge from HackerRank."""

import functools
import itertools

from typing import List


def main():
    """CLI interface."""
    print(maximize_it(read_input()))


# @dataclass not supported in PyPy yet :(
class Data:  # pylint: disable=R0903  # dataclass, methods don't matter
    """Data for the test.

    num_lists: int: number of lists, aka `K`
    modulus: int: modulus, aka `M`
    lists: List[List[int]]: lists to check
    """
    def __init__(
        self, num_lists: int, modulus: int, lists: List[List[int]] = None
    ):
        self.num_lists = num_lists
        self.modulus = modulus
        self.lists = lists if lists is not None else []

    def __str__(self):
        return (
            f"{self.__class__.__name__}(num_lists={self.num_lists}, "
            f"modulus={self.modulus}, lists={self.lists})"
        )


def maximize_it(data: Data) -> int:
    """Return result of []"""
    calc = functools.partial(calc_s, modulus=data.modulus)
    return max(map(calc, itertools.product(*data.lists)))


def f_sq(num: int) -> int:
    """Return [num] squared."""
    return num**2


def calc_s(nums: List[int], modulus: int) -> int:
    """Return s.

    Such that
    `s = (f(nums[0]) + f(nums[1]) + ... + f(nums[len(nums)])) % modulus`
    """
    return sum(map(f_sq, nums)) % modulus


def read_input() -> Data:
    """Read test input from stdin."""
    data = Data(*_read_line())
    for _ in range(data.num_lists):
        line = _read_line()
        assert len(line) == line[0] + 1, \
            "specified list length does not match number of elements specified"
        data.lists.append(line[1:])
    return data


def _read_line() -> List[int]:
    """Read an input line, split it and convert to ints."""
    return list(map(int, input().split()))


if __name__ == "__main__":
    main()
