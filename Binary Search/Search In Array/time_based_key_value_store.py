# https://leetcode.com/problems/time-based-key-value-store

import unittest
from bisect import insort
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Using 'insort' because:
        # 1. It is designed specifically for sorted lists.
        # 2. It inserts the new value directly at the correct position in the list using binary search.
        # 3. It has a time complexity of O(n) because the insertion point is determined
        # in logarithmic time (via binary search), and the insertion operation itself is
        # O(n) to shift elements if necessary.
        # docs: https://docs.python.org/3/library/bisect.html#bisect.insort

        # Relating it back to TimeMap:
        # 1. It guarantees the list in 'self.store[key]' remains sorted after each set operation.
        # 2. Due to the sorted order, the binary search in 'get' behaves correctly.

        # When not to use 'insort'?
        # When dealing with very large lists, where frequent insertions wil result in an O(n)
        # operation each time.
        # Alternative data structures like balanced binary search trees (e.g., AVL trees, Red-Black trees)
        # or ordered dictionaries can be used to maintain sorting with better complexity for both insertion
        # and search operations.

        insort(self.store[key], [timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        data = self.store.get(key, [])
        result = ""

        # Binary search for the right timestamp
        left = 0
        right = len(data) - 1

        while left <= right:
            mid = (left + right) // 2
            current_timestamp, value = data[mid]

            if current_timestamp <= timestamp:
                result = value
                left = mid + 1
            else:
                right = mid - 1

        return result


class TestTimeMap(unittest.TestCase):
    def setUp(self):
        self.time_map = TimeMap()

    def test_single_key(self):
        """Test with a single key-value pair."""
        self.time_map.set("foo", "bar", 1)
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("foo", 2), "bar")  # closest before or at 2
        self.assertEqual(self.time_map.get("foo", 0), "")  # no valid timestamp exists

    def test_multiple_timestamps(self):
        """Test with multiple values for the same key."""
        self.time_map.set("foo", "bar", 1)
        self.time_map.set("foo", "bar2", 2)
        self.time_map.set("foo", "bar3", 5)

        self.assertEqual(self.time_map.get("foo", 1), "bar")  # exact match at 1
        self.assertEqual(self.time_map.get("foo", 3), "bar2")  # closest value at 3
        self.assertEqual(self.time_map.get("foo", 5), "bar3")  # exact match at 5
        self.assertEqual(self.time_map.get("foo", 6), "bar3")  # closest value at 6
        self.assertEqual(self.time_map.get("foo", 0), "")  # no value before 1

    def test_key_not_found(self):
        """Test getting a value for a non-existent key."""
        self.assertEqual(self.time_map.get("nonexistent", 1), "")

    def test_multiple_keys(self):
        """Test storing and retrieving for multiple keys."""
        self.time_map.set("foo", "bar", 1)
        self.time_map.set("baz", "qux", 2)

        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("baz", 2), "qux")
        self.assertEqual(self.time_map.get("baz", 1), "")  # baz doesn't have a value at or before 1

    def test_non_chronological_timestamps(self):
        """Test if the function works regardless of insertion order."""
        self.time_map.set("foo", "bar2", 2)
        self.time_map.set("foo", "bar1", 1)

        self.assertEqual(self.time_map.get("foo", 1), "bar1")
        self.assertEqual(self.time_map.get("foo", 2), "bar2")
        self.assertEqual(self.time_map.get("foo", 3), "bar2")  # closest valid timestamp

    def test_early_and_large_timestamps(self):
        """Test edge cases with very early and very large timestamps."""
        self.time_map.set("foo", "early", 1)
        self.time_map.set("foo", "late", 100000)

        self.assertEqual(self.time_map.get("foo", 0), "")  # no value at 0
        self.assertEqual(self.time_map.get("foo", 1), "early")  # exact match at earliest
        self.assertEqual(self.time_map.get("foo", 99999), "early")  # closest before 100000
        self.assertEqual(self.time_map.get("foo", 100000), "late")  # exact match at 100000
        self.assertEqual(self.time_map.get("foo", 100001), "late")  # closest after 100000
