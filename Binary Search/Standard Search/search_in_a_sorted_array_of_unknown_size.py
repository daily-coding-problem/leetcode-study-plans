# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size

import unittest

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#     def get(self, index: int) -> int:
#         pass

def search(reader: 'ArrayReader', target: int) -> int:
    # Step 1: Initialize search range.
    low, high = 0, 1

    # Step 2: Expand the range until the target is within bounds or out-of-bounds value is found.
    while reader.get(high) < target:
        low = high
        high *= 2

        # If out-of-bounds value occurs, break.
        if reader.get(high) == 2 ** 31 - 1:
            break

    # Step 3: Perform binary search within the determined range.
    while low <= high:
        mid = (low + high) // 2
        value = reader.get(mid)

        # If mid is out of bounds, treat it as infinity
        if value == 2 ** 31 - 1:
            high = mid - 1  # Adjust high since out-of-bounds
            continue

        if value == target:
            return mid

        if value < target:
            low = mid + 1
        else:
            high = mid - 1

    # Target not found
    return -1

# Mock implementation of ArrayReader for testing purposes
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.arr):
            return 2**31 - 1  # Return out-of-bounds value
        return self.arr[index]

class TestSearchFunction(unittest.TestCase):
    def test_example1(self):
        reader = ArrayReader([-1, 0, 3, 5, 9, 12])
        self.assertEqual(search(reader, 9), 4)

    def test_example2(self):
        reader = ArrayReader([-1, 0, 3, 5, 9, 12])
        self.assertEqual(search(reader, 2), -1)

    def test_single_element_found(self):
        reader = ArrayReader([3])
        self.assertEqual(search(reader, 3), 0)

    def test_single_element_not_found(self):
        reader = ArrayReader([3])
        self.assertEqual(search(reader, 5), -1)

    def test_out_of_bounds(self):
        reader = ArrayReader([-10, -5, 0, 5, 10, 20])
        self.assertEqual(search(reader, 50), -1)

    def test_large_target_not_present(self):
        reader = ArrayReader([2, 4, 6, 8, 10, 12])
        self.assertEqual(search(reader, 15), -1)

    def test_negative_target_found(self):
        reader = ArrayReader([-20, -10, -5, -2, 0, 5])
        self.assertEqual(search(reader, -5), 2)

    def test_negative_target_not_found(self):
        reader = ArrayReader([-20, -10, -5, -2, 0, 5])
        self.assertEqual(search(reader, -15), -1)

    def test_empty_array(self):
        reader = ArrayReader([])
        self.assertEqual(search(reader, 10), -1)

    def test_target_is_out_of_bounds(self):
        reader = ArrayReader([-1, 0, 3, 5, 9, 12])
        self.assertEqual(search(reader, 100), -1)

    def test_large_array(self):
        # Simulate a large array of sorted unique elements
        reader = ArrayReader(list(range(1, 10001)))  # Array from 1 to 10,000
        self.assertEqual(search(reader, 5000), 4999)
        self.assertEqual(search(reader, 10000), 9999)
        self.assertEqual(search(reader, 10001), -1)
