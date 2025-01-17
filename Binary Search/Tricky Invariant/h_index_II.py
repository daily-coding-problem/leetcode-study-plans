# https://leetcode.com/problems/h-index-ii

import unittest
from typing import List


def h_index(citations: List[int]) -> int:
    n = len(citations)

    left = 0
    right = n - 1

    # We need to find the rightmost 'index' such that: (citations[index] <= n - index)
    while left <= right:
        mid = left + (right - left) // 2

        # There are (n - mid) papers with an equal or higher citation count than citations[mid]
        # If (citations[mid] == n - mid) it's the optimal result and can be returned right away
        if citations[mid] == n - mid:
            return n - mid

        # If citations[mid] are less than (n - mid), narrow down on the right half to look for a paper
        # at a future index that meets the h-index criteria. Otherwise, narrow down on the left half
        if citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid - 1

    # We didn't find an exact match, so there are exactly (n - left) papers that have citations
    # greater than or equal to citations[left], and that is our answer
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
