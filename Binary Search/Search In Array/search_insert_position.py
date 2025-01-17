# https://leetcode.com/problems/search-insert-position

import unittest
from typing import List


def search_left(nums: List[int], target: int) -> int:
    n = len(nums)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


class TestSearchLeft(unittest.TestCase):
    def test_target_found(self):
        self.assertEqual(search_left([1, 3, 5, 6], 5), 2)
        self.assertEqual(search_left([1, 2, 3, 4], 3), 2)

    def test_target_not_found(self):
        self.assertEqual(search_left([1, 3, 5, 6], 2), 1)
        self.assertEqual(search_left([1, 3, 5, 6], 7), 4)
        self.assertEqual(search_left([1, 3, 5, 6], 0), 0)

    def test_empty_list(self):
        self.assertEqual(search_left([], 5), 0)

    def test_large_target(self):
        self.assertEqual(search_left([1, 3, 5], 10), 3)

    def test_small_target(self):
        self.assertEqual(search_left([2, 4, 6], -2), 0)
