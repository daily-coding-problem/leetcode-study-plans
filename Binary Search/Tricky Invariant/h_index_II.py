# https://leetcode.com/problems/h-index-ii

import unittest
from typing import List


def h_index(citations: List[int]) -> int:
    n = len(citations)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        # If the citation at mid, equals the number of papers with citations >= citations[mid]
        if citations[mid] == n - mid:
            return citations[mid]  # Return the h-index

        # If citations at mid are less than the required h-index condition
        if citations[mid] < n - mid:
            left = mid + 1  # Shift the search to the right half
        else:
            right = mid - 1  # Shift the search to the left half

    # If no exact match is found, return the best possible h-index value
    return n - left


class TestHIndex(unittest.TestCase):
    def test_empty_list(self):
        # Empty list should return h-index of 0
        self.assertEqual(h_index([]), 0)

    def test_single_element(self):
        # Single element cases
        self.assertEqual(h_index([0]), 0)
        self.assertEqual(h_index([3]), 1)

    def test_all_zero_citations(self):
        # All papers have zero citations
        self.assertEqual(h_index([0, 0, 0, 0]), 0)

    def test_h_index_exists_in_array(self):
        # Case where h-index is present directly in the array
        self.assertEqual(h_index([0, 1, 3, 5, 6]), 3)

    def test_h_index_does_not_explicitly_exist(self):
        # Cases where the h-index value does not match any array value
        self.assertEqual(h_index([0, 1, 3, 4]), 2)
        self.assertEqual(h_index([0, 2, 3, 3, 5, 6, 7]), 3)

    def test_large_list(self):
        # Large list to test behavior on bigger inputs
        self.assertEqual(h_index([0, 1, 2, 2, 3, 3, 4, 4, 6, 8, 10]), 4)
        self.assertEqual(h_index([1, 2, 100]), 2)
