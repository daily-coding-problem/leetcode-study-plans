# https://leetcode.com/problems/snapshot-array

import unittest
from collections import defaultdict


class SnapshotArray:
    def __init__(self, _: int):
        self.snap_id = 0
        self.history = defaultdict(
            lambda: [(0, 0)]
        )  # Default history with initial (snap_id, value)

    def set(self, index: int, value: int) -> None:
        # Fetch the last recorded snap_id for the given index
        last_snap_id, _ = self.history[index][-1]

        # If the last recorded snap_id matches the current snap_id, update the value
        if last_snap_id == self.snap_id:
            self.history[index][-1] = (self.snap_id, value)
            return

        # Otherwise, append a new entry with the current snap_id and the value
        self.history[index].append((self.snap_id, value))

    def snap(self) -> int:
        # Increment snap_id and return the previous snap_id
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Binary search for the largest snap_id <= the requested snap_id

        snaps = self.history[index]
        left, right = 0, len(snaps) - 1

        while left <= right:
            mid = (left + right) // 2

            if snaps[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return snaps[right][
            1
        ]  # The value corresponding to the largest snap_id ≤ the requested snap_id


class TestSnapshotArray(unittest.TestCase):
    def test_initialization(self):
        # Test that the SnapshotArray initializes without errors and the default history is correct.
        obj = SnapshotArray(5)
        for i in range(
            5
        ):  # Check that every index initializes with a default value of 0
            self.assertEqual(obj.get(i, 0), 0)

    def test_set_and_get_before_snap(self):
        # Test setting and getting values before taking a snapshot
        obj = SnapshotArray(5)
        obj.set(2, 15)
        obj.set(2, 30)

        # Get the value before taking any snapshot
        self.assertEqual(obj.get(2, 0), 30)
        self.assertEqual(obj.get(0, 0), 0)  # Default value at unmodified index

    def test_snap_and_get(self):
        # Tests snap functionality and retrieving correct values
        obj = SnapshotArray(5)

        obj.set(1, 5)
        snap_0 = obj.snap()
        self.assertEqual(snap_0, 0)  # First snapshot ID should be 0

        obj.set(1, 10)
        snap_1 = obj.snap()
        self.assertEqual(snap_1, 1)  # Second snapshot ID should be 1

        self.assertEqual(obj.get(1, 0), 5)  # Value at index 1 in snapshot 0
        self.assertEqual(obj.get(1, 1), 10)  # Value at index 1 in snapshot 1
        self.assertEqual(obj.get(1, 2), 10)  # Value at index 1 in most recent snapshot

    def test_overwrite_before_snap(self):
        # Test overwriting a value before taking a snapshot
        obj = SnapshotArray(5)
        obj.set(3, 7)
        obj.set(3, 2)  # Overwrite the value before taking a snapshot

        snap_0 = obj.snap()
        self.assertEqual(snap_0, 0)
        self.assertEqual(obj.get(3, 0), 2)

    def test_multiple_snaps(self):
        # Test with multiple snapshot operations
        obj = SnapshotArray(5)
        obj.set(0, 1)
        obj.snap()  # snap_id = 0

        obj.set(0, 2)
        obj.snap()  # snap_id = 1

        obj.set(0, 3)
        obj.snap()  # snap_id = 2

        self.assertEqual(obj.get(0, 0), 1)  # Value at snap_id 0
        self.assertEqual(obj.get(0, 1), 2)  # Value at snap_id 1
        self.assertEqual(obj.get(0, 2), 3)  # Value at snap_id 2

    def test_edge_case_no_sets(self):
        # Test edge case where no `set` operations are performed before a snapshot
        obj = SnapshotArray(3)
        snap_0 = obj.snap()
        self.assertEqual(snap_0, 0)
        self.assertEqual(obj.get(2, 0), 0)  # Default value

    def test_out_of_order_snaps(self):
        # Test case where snapshots are queried out of order
        obj = SnapshotArray(2)
        obj.set(1, 100)
        _ = obj.snap()  # snap_id = 0
        obj.set(1, 200)
        _ = obj.snap()  # snap_id = 1
        obj.set(1, 300)
        _ = obj.snap()  # snap_id = 2

        self.assertEqual(obj.get(1, 2), 300)
        self.assertEqual(obj.get(1, 1), 200)
        self.assertEqual(obj.get(1, 0), 100)

    def test_large_snapshots(self):
        # Test for a larger number of snapshots
        obj = SnapshotArray(1)
        for i in range(1000):
            obj.set(0, i)
            snap_id = obj.snap()
            self.assertEqual(
                obj.get(0, snap_id), i
            )  # Value should match at each snapshot
