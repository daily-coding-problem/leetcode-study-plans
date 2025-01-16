# https://leetcode.com/problems/find-right-interval

import unittest
from typing import List, Tuple

def find_right_interval(intervals: List[List[int]]) -> List[int]:
    if not intervals:
        return []

    n = len(intervals)

    if n <= 1:
        # If there's only one interval, check if it can be its own right interval
        return [0] if intervals[0][0] == intervals[0][1] else [-1]

    def search_left(start_intervals: List[Tuple[int, int]], end: int) -> int:
        left = 0
        right = n - 1

        index = -1

        while left <= right:
            mid = (left + right) // 2

            if start_intervals[mid][0] >= end:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index

    # Create a list of tuples where each tuple is (start, index)
    start_intervals = sorted((interval[0], i) for i, interval in enumerate(intervals))

    result = [-1] * n

    for i, interval in enumerate(intervals):
        end = interval[1]

        # Find the smallest start that is >= end
        index = search_left(start_intervals, end)

        if index != -1:
            result[i] = start_intervals[index][1]

    return result

class TestFindRightInterval(unittest.TestCase):
    def test_no_intervals(self):
        self.assertEqual(find_right_interval([]), [])

    def test_single_interval_no_right(self):
        self.assertEqual(find_right_interval([[1, 2]]), [-1])

    def test_single_interval_is_its_own_right(self):
        self.assertEqual(find_right_interval([[1, 1]]), [0])

    def test_multiple_intervals_no_overlap(self):
        self.assertEqual(
            find_right_interval([[1, 2], [3, 4], [5, 6]]), [1, 2, -1]
        )

    def test_multiple_intervals_with_overlap(self):
        self.assertEqual(
            find_right_interval([[1, 4], [2, 3], [3, 4]]), [-1, 2, -1]
        )

    def test_multiple_intervals_with_same_start(self):
        self.assertEqual(
            find_right_interval([[1, 2], [1, 3], [3, 4]]), [2, 2, -1]
        )

    def test_large_intervals(self):
        self.assertEqual(
            find_right_interval([[1, 1000], [500, 1500], [1001, 2000]]),
            [2, -1, -1]
        )
