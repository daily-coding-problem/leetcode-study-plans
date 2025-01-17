# https://leetcode.com/problems/kth-missing-positive-number

import unittest
from typing import List


def find_kth_positive_number(arr: List[int], k: int) -> int:
    n = len(arr)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        # The number of positive numbers which are missing before arr[mid]
        missing_positive_numbers = arr[mid] - mid - 1

        if missing_positive_numbers < k:
            left = mid + 1
        else:
            right = mid - 1

    # At the end of the loop, left = right + 1,
    # and the kth missing is in-between arr[right] and arr[left].
    # The number of numbers missing before arr[right] is:
    # arr[right] - right - 1
    # The number to return is:
    # arr[right] + k - (arr[right] - right - 1) = left + k
    return left + k


class TestFindKthPositiveNumber(unittest.TestCase):
    def test_example_case(self):
        # General example case
        arr = [2, 3, 4, 7, 11]
        k = 5
        self.assertEqual(find_kth_positive_number(arr, k), 9)

    def test_single_element_array(self):
        # When the input array has a single number
        arr = [2]
        k = 1
        self.assertEqual(find_kth_positive_number(arr, k), 1)
        k = 3
        self.assertEqual(find_kth_positive_number(arr, k), 4)

    def test_k_large(self):
        # When k is larger than the array range
        arr = [1, 3, 6]
        k = 8
        self.assertEqual(find_kth_positive_number(arr, k), 11)

    def test_consecutive_elements(self):
        # When the array has all numbers consecutively
        arr = [1, 2, 3, 4, 5]
        k = 1
        self.assertEqual(find_kth_positive_number(arr, k), 6)

    def test_missing_with_gap_at_start(self):
        # When the array starts with missing elements
        arr = [5, 6, 7, 8, 9]
        k = 3
        self.assertEqual(find_kth_positive_number(arr, k), 3)

    def test_missing_with_large_gap_inside(self):
        # When there is a large gap inside the array
        arr = [3, 8, 12]
        k = 4
        self.assertEqual(find_kth_positive_number(arr, k), 5)

    def test_empty_array(self):
        # When the array is empty
        arr = []
        k = 10
        self.assertEqual(find_kth_positive_number(arr, k), 10)

    def test_large_values(self):
        # When the array and k contain larger numbers
        arr = [100, 101, 105]
        k = 5
        self.assertEqual(find_kth_positive_number(arr, k), 5)

    def test_minimum_k(self):
        # When k is 1 and higher than the smallest missing number
        arr = [2, 4, 6]
        k = 1
        self.assertEqual(find_kth_positive_number(arr, k), 1)
