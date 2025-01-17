# https://leetcode.com/problems/single-element-in-a-sorted-array

import unittest
from typing import List

# Key observation is that this algorithm will still work even if the array
# isn't fully sorted. As long as pairs are always grouped together in the array
# (for example, [10, 10, 4, 4, 7, 11, 11, 12, 12, 2, 2]), it doesn't matter what
# order they're in. Binary search worked for this problem because we knew the subarray
# with the single number is always odd-lengthed, not because the array was fully sorted
# numerically. We commonly call this an invariant, something that is always true
# (i.e. "The array containing the single element is always odd-lengthed"). Be on the lookout
# for invariants like this when solving array problems, as binary search is very flexible!


def single_non_duplicate(nums: List[int]) -> int:
    n = len(nums)

    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        # Ensure 'mid' is even for comparison with its pair
        if mid % 2 == 1:
            mid -= 1  # Make it even

        # Check if the pair is valid
        if nums[mid] == nums[mid + 1]:
            # If the pair is valid, move the search space to the right
            left = mid + 2
        else:
            # Otherwise, move the search to the left
            right = mid

    # The left pointer will point at the single non-duplicate element
    return nums[left]


class TestSingleNonDuplicate(unittest.TestCase):
    def test_single_element(self):
        """Test with a single-element array"""
        self.assertEqual(single_non_duplicate([1]), 1)

    def test_single_in_middle(self):
        """Test with an odd-length array, single element in the middle"""
        self.assertEqual(single_non_duplicate([1, 1, 2, 3, 3]), 2)

    def test_single_at_start(self):
        """Test with a single element at the start of the array"""
        self.assertEqual(single_non_duplicate([2, 3, 3, 4, 4]), 2)

    def test_single_at_end(self):
        """Test with a single element at the end of the array"""
        self.assertEqual(single_non_duplicate([1, 1, 2, 2, 3]), 3)

    def test_longer_array(self):
        """Test with a larger array"""
        self.assertEqual(single_non_duplicate([1, 1, 2, 2, 3, 3, 4, 5, 5]), 4)

    def test_consecutive_numbers(self):
        """Test with a numerical sequence as pairs and single"""
        self.assertEqual(single_non_duplicate([0, 0, 1, 1, 2, 3, 3]), 2)

    def test_invalid_input(self):
        """Test with input that doesn't meet constraints (all paired elements)"""
        with self.assertRaises(IndexError):
            single_non_duplicate([1, 1, 2, 2])

    def test_large_input(self):
        """Test with very large input"""
        nums = list(range(1, 20000)) * 2
        nums.append(1000000)
        nums.sort()
        self.assertEqual(single_non_duplicate(nums), 1000000)
