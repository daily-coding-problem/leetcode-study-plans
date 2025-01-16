# https://leetcode.com/problems/first-bad-version

import unittest


# The is_bad_version API is already defined for you.
# def is_bad_version(version: int) -> bool:

# Mock is_bad_version API for testing purposes
def is_bad_version(version: int) -> bool:
    # This function needs to mimic an external API behavior.
    # Adjust the 'first_bad' variable to simulate different scenarios.
    return version >= first_bad


def first_bad_version(n: int) -> int:
    left = 1
    right = n

    earliest_bad_version = float('inf')

    while left <= right:
        mid = (left + right) // 2

        # Convert 'is_bad_version' to camelCase when importing back into LeetCode
        if is_bad_version(mid):
            earliest_bad_version = min(earliest_bad_version, mid)
            right = mid - 1
        else:
            left = mid + 1

    if earliest_bad_version == float('inf'):
        return -1

    return earliest_bad_version


class TestFirstBadVersion(unittest.TestCase):
    def test_first_bad_version(self):
        global first_bad  # Use a global variable to set the first bad version dynamically

        n = 10  # Total versions

        # Test case 1: The first bad version is 4
        first_bad = 4
        self.assertEqual(first_bad_version(n), 4)

        # Test case 2: Only one version, and it's bad
        first_bad = 1
        self.assertEqual(first_bad_version(1), 1)

        # Test case 3: The first bad version is the last one
        first_bad = 10
        self.assertEqual(first_bad_version(n), 10)

        # Test case 4: No bad version (all versions are good)
        first_bad = float('inf')  # Simulate no bad version
        self.assertEqual(first_bad_version(n), -1)

        # Test case 5: Testing with larger input size
        n = 1_000_000
        first_bad = 567_890
        self.assertEqual(first_bad_version(n), 567_890)

    def test_edge_cases(self):
        global first_bad  # Use to control the mock

        # Test case 6: Minimum input size (n = 1)
        first_bad = 1
        self.assertEqual(first_bad_version(1), 1)

        # Test case 7: Input with no bad versions in extreme edge case
        n = 2
        first_bad = float('inf')
        self.assertEqual(first_bad_version(n), -1)
