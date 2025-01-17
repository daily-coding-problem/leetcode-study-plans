# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

import unittest
from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    def find_left_index(nums: List[int], target: int) -> int:
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def find_right_index(nums: List[int], target: int) -> int:
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right

    left_index = find_left_index(nums, target)
    right_index = find_right_index(nums, target)

    # Make sure that the target is in range
    if (
        left_index <= right_index < n
        and nums[left_index] == target
        and nums[right_index] == target
    ):
        return [left_index, right_index]

    return [-1, -1]


class TestSearchRange(unittest.TestCase):
    def test_multiple_occurrences(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(search_range(nums, target), [3, 4])

    def test_single_occurrence(self):
        nums = [5, 7, 7, 8, 10]
        target = 8
        self.assertEqual(search_range(nums, target), [3, 3])

    def test_target_not_found(self):
        nums = [5, 7, 7, 8, 10]
        target = 6
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_empty_array(self):
        nums = []
        target = 1
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_all_elements_are_target(self):
        nums = [8, 8, 8, 8, 8]
        target = 8
        self.assertEqual(search_range(nums, target), [0, 4])

    def test_target_smaller_than_all(self):
        nums = [5, 7, 8, 10]
        target = 4
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_target_greater_than_all(self):
        nums = [5, 7, 8, 10]
        target = 12
        self.assertEqual(search_range(nums, target), [-1, -1])
