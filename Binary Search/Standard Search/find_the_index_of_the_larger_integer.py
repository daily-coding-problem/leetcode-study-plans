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
    pass


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

        :param l: Start index of the first range
        :param r: End index of the first range
        :param x: Start index of the second range
        :param y: End index of the second range
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
