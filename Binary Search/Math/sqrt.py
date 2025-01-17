# https://leetcode.com/problems/sqrtx

import unittest


def sqrt(x: int) -> int:
    if x < 2:
        return x

    left = 2
    right = x // 2

    while left <= right:
        mid = (left + right) // 2

        num = mid * mid

        if num == x:
            return mid

        if num < x:
            left = mid + 1
        else:
            right = mid - 1

    return right


class TestSqrtFunction(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(sqrt(0), 0)  # Square root of 0 is 0
        self.assertEqual(sqrt(1), 1)  # Square root of 1 is 1
        self.assertEqual(sqrt(2), 1)  # Closest integer square root of 2 is 1

    def test_perfect_squares(self):
        self.assertEqual(sqrt(4), 2)  # 2^2 = 4
        self.assertEqual(sqrt(9), 3)  # 3^2 = 9
        self.assertEqual(sqrt(16), 4)  # 4^2 = 16
        self.assertEqual(sqrt(25), 5)  # 5^2 = 25

    def test_non_perfect_squares(self):
        self.assertEqual(sqrt(8), 2)  # Closest integer square root of 8 is 2
        self.assertEqual(sqrt(10), 3)  # Closest integer square root of 10 is 3
        self.assertEqual(sqrt(27), 5)  # Closest integer square root of 27 is 5

    def test_large_numbers(self):
        self.assertEqual(sqrt(1000000), 1000)  # Perfect square
        self.assertEqual(sqrt(1234567), 1111)  # Closest integer square root of 1234567

    def test_edge_cases(self):
        self.assertEqual(
            sqrt(2147395599), 46339
        )  # Largest x for which x^2 still fits in an int (32-bit)
        self.assertEqual(
            sqrt(2147483647), 46340
        )  # Input is the max 32-bit integer, square root approximates
