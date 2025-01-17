# https://leetcode.com/problems/find-smallest-letter-greater-than-target

import unittest
from typing import List


def next_letter_greater(letters: List[str], target: str) -> str:
    if not letters:
        raise ValueError("The input list 'letters' cannot be empty.")

    n = len(letters)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return letters[left % n]


class TestNextLetterGreater(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(next_letter_greater(["c"], "a"), "c")
        self.assertEqual(next_letter_greater(["c"], "c"), "c")

    def test_basic_cases(self):
        self.assertEqual(next_letter_greater(["c", "f", "j"], "a"), "c")
        self.assertEqual(next_letter_greater(["c", "f", "j"], "c"), "f")
        self.assertEqual(next_letter_greater(["c", "f", "j"], "d"), "f")
        self.assertEqual(next_letter_greater(["c", "f", "j"], "g"), "j")
        self.assertEqual(next_letter_greater(["c", "f", "j"], "j"), "c")

    def test_wrap_around(self):
        self.assertEqual(next_letter_greater(["c", "f", "j"], "k"), "c")

    def test_duplicates(self):
        self.assertEqual(next_letter_greater(["c", "c", "f", "f", "j", "j"], "a"), "c")
        self.assertEqual(next_letter_greater(["c", "c", "f", "f", "j", "j"], "c"), "f")
        self.assertEqual(next_letter_greater(["c", "c", "f", "f", "j", "j"], "f"), "j")
        self.assertEqual(next_letter_greater(["c", "c", "f", "f", "j", "j"], "j"), "c")

    def test_large_list(self):
        letters = ["a", "b", "c", "d", "e"]
        self.assertEqual(next_letter_greater(letters, "c"), "d")
        self.assertEqual(next_letter_greater(letters, "e"), "a")

    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            next_letter_greater([], "a")

    def test_nonexistent_target(self):
        self.assertEqual(next_letter_greater(["a", "b", "d", "e"], "c"), "d")
