# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

import unittest
from typing import List


def count_negatives(grid: List[List[int]]) -> int:
    def count_negatives_in_row(row: List[int]) -> int:
        n = len(row)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] < 0:
                right = mid - 1
            else:
                left = mid + 1

        return len(row) - left

    result = 0

    for row in grid:
        result += count_negatives_in_row(row)

    return result


class TestCountNegatives(unittest.TestCase):
    def test_empty_grid(self):
        # Test case with an empty grid
        grid = []
        self.assertEqual(count_negatives(grid), 0)

    def test_single_row_all_positive(self):
        # Test case with a single row and no negative numbers
        grid = [[1, 2, 3, 4, 5]]
        self.assertEqual(count_negatives(grid), 0)

    def test_single_row_some_negatives(self):
        # Test case with a single row containing some negative numbers
        grid = [[1, 2, -1, -2, -3]]
        self.assertEqual(count_negatives(grid), 3)

    def test_single_row_all_negatives(self):
        # Test case with a single row of all negative numbers
        grid = [[-1, -2, -3, -4, -5]]
        self.assertEqual(count_negatives(grid), 5)

    def test_multiple_rows_no_negatives(self):
        # Test case with multiple rows with no negative numbers
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(count_negatives(grid), 0)

    def test_multiple_rows_with_negatives(self):
        # Test case with some rows containing negative numbers
        grid = [[1, -1, -2], [3, -3, -4], [-5, -6, -7]]
        self.assertEqual(count_negatives(grid), 7)

    def test_large_matrix(self):
        # Test case with a large matrix for performance validation
        grid = [
            [5, 4, 3, 2, -1],
            [4, 3, 2, -1, -2],
            [3, 2, -1, -2, -3],
            [2, -1, -2, -3, -4],
            [-1, -2, -3, -4, -5],
        ]
        self.assertEqual(count_negatives(grid), 15)

    def test_single_column(self):
        # Test case with only one column
        grid = [[4], [3], [-1], [-2]]
        self.assertEqual(count_negatives(grid), 2)

    def test_no_negatives(self):
        # Test case where there are no negative numbers at all
        grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.assertEqual(count_negatives(grid), 0)

    def test_all_negatives(self):
        # Test case where the entire grid contains only negative numbers
        grid = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(count_negatives(grid), 9)
