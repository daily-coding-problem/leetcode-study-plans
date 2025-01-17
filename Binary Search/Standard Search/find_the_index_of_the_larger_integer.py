# https://leetcode.com/problems/find-the-index-of-the-large-integer

import unittest

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
# 	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
# 	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
# 	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
# 	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


def get_index(reader: "ArrayReader") -> int:
    # Get the length of the array from the reader
    n = reader.length()

    # Initialize the left and right pointers for binary search
    left, right = 0, n - 1

    # Perform binary search to find the index
    while left < right:
        # Calculate the middle index
        mid = (left + right) // 2

        # Determine if the current subarray has an even number of elements
        if (right - left + 1) % 2 == 0:
            # Compare the two halves of the subarray
            compare = reader.compareSub(left, mid, mid + 1, right)
        else:
            # Compare the two halves including the middle element in both halves
            compare = reader.compareSub(left, mid, mid, right)

        # If the left half is smaller, the element is in the right half
        if compare < 0:
            left = mid + 1
            continue

        # If the left half is larger or equal, the element is in the left half
        right = mid

    # Return the index of the element
    return left


class ArrayReader:
    def __init__(self, arr):
        """
        Initialize the mock class with an array.

        :param arr: The array to be used for mocking the behavior of ArrayReader.
        """
        self.array = arr

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        """
        Compares the sum of arr[l..r] with the sum of arr[x..y].

        :param l: The start index of the first range
        :param r: The end index of the first range
        :param x: The start index of the second range
        :param y: The end index of the second range
        :return:
            - 1 if sum(arr[l..r]) > sum(arr[x..y])
            - 0 if sum(arr[l..r]) == sum(arr[x..y])
            - -1 if sum(arr[l..r]) < sum(arr[x..y])
        """
        sum1 = sum(self.array[l : r + 1])  # Sum from index l to r
        sum2 = sum(self.array[x : y + 1])  # Sum from index x to y

        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        else:
            return 0

    def length(self) -> int:
        """
        Returns the length of the array.

        :return: Length of the array
        """
        return len(self.array)


class TestGetIndex(unittest.TestCase):
    def test_single_element(self):
        array = [10]
        reader = ArrayReader(array)
        self.assertEqual(get_index(reader), 0)

    def test_two_elements_first_large(self):
        array = [20, 10]
        reader = ArrayReader(array)
        self.assertEqual(get_index(reader), 0)

    def test_two_elements_second_large(self):
        array = [10, 20]
        reader = ArrayReader(array)
        self.assertEqual(get_index(reader), 1)

    def test_large_array_uniform_with_one_large(self):
        array = [
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            46,
            57,
            46,
            46,
            46,
            46,
        ]
        reader = ArrayReader(array)
        self.assertEqual(get_index(reader), 20)

    def test_large_array_middle_large(self):
        array = [1, 1, 50, 1, 1]
        reader = ArrayReader(array)
        self.assertEqual(get_index(reader), 2)

    def test_large_array_end_large(self):
        array = [1, 1, 1, 1, 50]
        reader = ArrayReader(array)
        self.assertEqual(get_index(reader), 4)

    def test_large_array_start_large(self):
        array = [50, 1, 1, 1, 1]
        reader = ArrayReader(array)
        self.assertEqual(get_index(reader), 0)
