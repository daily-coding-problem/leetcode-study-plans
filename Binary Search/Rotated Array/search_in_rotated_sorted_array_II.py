# https://leetcode.com/problems/search-in-rotated-sorted-array-ii

import unittest
from typing import List


def find_min(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If the mid-element is greater than the last element,
        # the min value must be in the right half (excluding mid).
        if nums[mid] > nums[right]:
            left = mid + 1
        # If the mid-element is less than the last element,
        # the min value is in the left half (including mid).
        elif nums[mid] < nums[right]:
            right = mid
        # If nums[mid] == nums[high], decrease `high` to skip duplicate.
        else:
            right -= 1

    return nums[left]


class TestFindMin(unittest.TestCase):
    def test_example_cases(self):
        # Example cases given in the prompt
        self.assertEqual(find_min([1, 3, 5]), 1)  # Example 1
        self.assertEqual(find_min([2, 2, 2, 0, 1]), 0)  # Example 2

    def test_sorted_no_rotation(self):
        # Fully sorted, no rotation
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)

    def test_single_element(self):
        # Single element array
        self.assertEqual(find_min([10]), 10)

    def test_all_duplicates(self):
        # Array with all duplicates
        self.assertEqual(find_min([2, 2, 2, 2]), 2)

    def test_duplicates_with_rotation(self):
        # Array with duplicates and rotation
        self.assertEqual(find_min([2, 2, 2, 3, 1, 2]), 1)
        self.assertEqual(find_min([4, 4, 4, 0, 4]), 0)

    def test_rotated_at_different_points(self):
        # Rotation at different points
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)  # Rotated in the middle
        self.assertEqual(find_min([7, 0, 1, 2, 4, 5, 6]), 0)  # Rotated almost fully
        self.assertEqual(find_min([2, 3, 4, 5, 6, 7, 0, 1]), 0)  # Rotated at the end

    def test_large_input(self):
        # Large array with rotation and duplicates
        nums = [1] * 5000 + [0] + [1] * 5000
        self.assertEqual(find_min(nums), 0)
