# https://leetcode.com/problems/guess-number-higher-or-lower

import unittest

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Mock guess function
def guess(num: int) -> int:
    if num > picked_number:
        return -1
    elif num < picked_number:
        return 1
    else:
        return 0

def guess_number(n: int) -> int:
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        response = guess(mid)
        is_lower = response == 1
        found_number = response == 0

        if found_number:
            return mid

        if is_lower:
            left = mid + 1
        else:
            right = mid - 1

    return n

class TestGuessNumber(unittest.TestCase):
    def test_number_found(self):
        global picked_number
        picked_number = 6  # Define the picked number
        self.assertEqual(guess_number(10), 6)  # n is 10, picked_number is 6

    def test_low_boundary(self):
        global picked_number
        picked_number = 1
        self.assertEqual(guess_number(1), 1)  # n is 1, picked_number is 1

    def test_high_boundary(self):
        global picked_number
        picked_number = 10
        self.assertEqual(guess_number(10), 10)  # n is 10, picked_number is 10

    def test_middle_search(self):
        global picked_number
        picked_number = 50
        self.assertEqual(guess_number(100), 50)  # n is 100, picked_number is 50

    def test_large_number(self):
        global picked_number
        picked_number = 999_999
        self.assertEqual(guess_number(1_000_000), 999_999)  # Large n, picked_number is 999,999

