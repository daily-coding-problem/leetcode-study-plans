# https://leetcode.com/problems/peak-index-in-a-mountain-array

import unittest
from typing import List


def peak_index_in_mountain_array(mountain: List[int]) -> int:
    n = len(mountain)

    left = 0
    right = n - 1

    # Binary Search to find the peak
    # Invariant: The peak is always within the range [left, right]
    # - If mountain[mid] < mountain[mid + 1], the peak must be to the right of mid
    #   (because we're still in the increasing slope).
    # - If mountain[mid] >= mountain[mid + 1], the peak is either at mid or to the left of mid
    #   (because we've started descending, so the peak can't be further right).
    # This ensures that the peak index is narrowed down until `left == right`.

    while left < right:
        mid = (left + right) // 2

        if mountain[mid] < mountain[mid + 1]:  # Moving up the slope
            left = mid + 1
        else:  # Moving down the slope, or current is the peak
            right = mid

    # At the end of the loop, left == right and it points to the peak index.
    return left


class TestPeakIndexInMountainArray(unittest.TestCase):
    def test_peak_at_start(self):
        """Test case where the peak is at the start of a small mountain."""
        self.assertEqual(peak_index_in_mountain_array([2, 1, 0]), 0)

    def test_peak_at_middle(self):
        """Test case with a peak element in the middle."""
        self.assertEqual(peak_index_in_mountain_array([0, 2, 1, 0]), 1)

    def test_peak_at_end(self):
        """Test case where the peak is at the end."""
        self.assertEqual(peak_index_in_mountain_array([0, 1, 2]), 2)

    def test_peak_in_large_middle(self):
        """Peak is in the middle of a larger mountain."""
        self.assertEqual(peak_index_in_mountain_array([1, 3, 5, 7, 8, 9, 6, 4, 2]), 5)

    def test_minimum_array_size(self):
        """Minimum size mountain array."""
        self.assertEqual(peak_index_in_mountain_array([0, 1, 0]), 1)

    def test_large_mountain_array(self):
        """Mountain with large number of elements."""
        large_mountain = list(range(1, 50001)) + list(range(50000, 0, -1))
        self.assertEqual(peak_index_in_mountain_array(large_mountain), 49999)

    def test_large_numbers(self):
        """Mountain array with maximum possible values."""
        mountain = [10**6 - 1, 10**6, 10**6 - 2]
        self.assertEqual(peak_index_in_mountain_array(mountain), 1)

    def test_multiple_shapes(self):
        """Various mountain shapes."""
        self.assertEqual(peak_index_in_mountain_array([0, 5, 2, 1, 0]), 1)
        self.assertEqual(peak_index_in_mountain_array([10, 20, 30, 25, 20]), 2)
        self.assertEqual(peak_index_in_mountain_array([0, 10, 11, 10, 0]), 2)
        self.assertEqual(peak_index_in_mountain_array([1, 3, 5, 7, 5, 3, 1]), 3)
