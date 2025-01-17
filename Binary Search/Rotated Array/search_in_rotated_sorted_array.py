# https://leetcode.com/problems/search-in-rotated-sorted-array

import unittest
from typing import List

def search(nums: List[int], target: int) -> int:
    n = len(nums)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

class TestSearchRotatedSortedArray(unittest.TestCase):
    def test_target_in_rotated_array(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(search(nums, target), 4)

    def test_target_not_in_rotated_array(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(search(nums, target), -1)

    def test_target_in_non_rotated_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        target = 4
        self.assertEqual(search(nums, target), 3)

    def test_target_not_in_non_rotated_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        target = 8
        self.assertEqual(search(nums, target), -1)

    def test_single_element_present(self):
        nums = [1]
        target = 1
        self.assertEqual(search(nums, target), 0)

    def test_single_element_absent(self):
        nums = [1]
        target = 0
        self.assertEqual(search(nums, target), -1)

    def test_empty_array(self):
        nums = []
        target = 1
        self.assertEqual(search(nums, target), -1)

    def test_duplicate_elements(self):
        # While the problem states duplicates are not considered,
        # we can create a test for robustness
        nums = [2, 2, 2, 3, 4, 2]
        target = 3
        self.assertEqual(search(nums, target), 3)
