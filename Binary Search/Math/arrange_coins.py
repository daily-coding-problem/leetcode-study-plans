# https://leetcode.com/problems/arranging-coins

import unittest


def arrange_coins(n: int) -> int:
    left = 0
    right = n

    while left <= right:
        k = (left + right) // 2

        current = k * (k + 1) // 2

        if current == n:
            return k

        if current < n:
            left = k + 1
        else:
            right = k - 1

    return right


class TestArrangeCoins(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(arrange_coins(0), 0)
        self.assertEqual(arrange_coins(1), 1)
        self.assertEqual(arrange_coins(2), 1)
        self.assertEqual(arrange_coins(3), 2)

    def test_medium_numbers(self):
        self.assertEqual(arrange_coins(5), 2)
        self.assertEqual(arrange_coins(8), 3)
        self.assertEqual(arrange_coins(10), 4)

    def test_large_numbers(self):
        self.assertEqual(arrange_coins(10000), 140)
        self.assertEqual(arrange_coins(500000), 999)

    def test_boundary_conditions(self):
        self.assertEqual(arrange_coins(15), 5)  # Fully filled staircase
        self.assertEqual(arrange_coins(16), 5)  # 15 + 1 extra coin
        self.assertEqual(arrange_coins(17), 5)
