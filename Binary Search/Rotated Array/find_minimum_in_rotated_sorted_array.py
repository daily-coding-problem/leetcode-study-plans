# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

import unittest
from typing import List


def find_min(nums: List[int]) -> int:
    n = len(nums)

    left = 0
    right = n - 1
    min_element = float("inf")

    while left < right:
        pivot = (left + right) // 2
        min_element = min(nums[pivot], min_element)

        if nums[pivot] > nums[right]:
            left = pivot + 1
        else:
            right = pivot - 1

    return min(min_element, nums[left])


class TestFindMin(unittest.TestCase):
    def test_sorted_array(self):
        # Case: Sorted array without rotation
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)

    def test_rotated_array(self):
        # Normal rotations
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min([2, 3, 4, 5, 1]), 1)

    def test_min_at_ends(self):
        # Single rotation setups where min is at the boundaries
        self.assertEqual(find_min([5, 6, 7, 8, 1, 2, 3, 4]), 1)
        self.assertEqual(find_min([9, 1, 2, 3, 4, 5, 6, 7]), 1)

    def test_single_element(self):
        # Case: Single element array
        self.assertEqual(find_min([1]), 1)

    def test_two_elements(self):
        # Case: Two-element array
        self.assertEqual(find_min([2, 1]), 1)
        self.assertEqual(find_min([1, 2]), 1)

    def test_duplicates(self):
        # Case: Duplicates (if allowed)
        self.assertEqual(find_min([2, 2, 2, 0, 1]), 0)
        self.assertEqual(find_min([1, 1, 1, 1, 1]), 1)

    def test_large_array(self):
        # Case: Large arrays
        nums = list(range(100, 1000)) + list(range(1, 100))
        self.assertEqual(find_min(nums), 1)
