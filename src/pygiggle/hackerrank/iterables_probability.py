"""Iterables and Iterators challenge from HackerRank."""

import itertools

from typing import List, Tuple


def main():
    """CLI interface."""
    num_letters, k, letters = read_input()
    print(a_probability(num_letters, k, letters))


def read_input() -> Tuple[int, int, List[str]]:
    """Read test input from stdin."""
    num_letters = int(input())
    letters = input().split()
    k = int(input())
    return (num_letters, k, letters)


def a_probability(num_letters: int, k: int, letters: List[str]) -> float:
    """Return probability of letter "a" in k-length slices of [letters]."""
    a_indices = [i for i, s in enumerate(letters) if s == "a"]
    combinations = list(itertools.combinations(range(0, num_letters), k))
    combinations_containing_a = [
        t for t in combinations if any([i in t for i in a_indices])
    ]
    return len(combinations_containing_a) / len(combinations)


if __name__ == "__main__":
    main()
