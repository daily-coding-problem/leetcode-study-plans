# https://leetcode.com/problems/valid-perfect-square

import unittest


def is_perfect_square(num: int) -> bool:
    left = 0
    right = num

    while left <= right:
        mid = (left + right) // 2

        squared = mid * mid

        if squared == num:
            return True

        if squared < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


class TestIsPerfectSquare(unittest.TestCase):
    def test_perfect_squares(self):
        # Testing basic perfect squares
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertTrue(is_perfect_square(25))
        self.assertTrue(is_perfect_square(36))
        self.assertTrue(is_perfect_square(49))
        self.assertTrue(is_perfect_square(64))
        self.assertTrue(is_perfect_square(81))
        self.assertTrue(is_perfect_square(100))

    def test_non_perfect_squares(self):
        # Testing numbers that are not perfect squares
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(6))
        self.assertFalse(is_perfect_square(7))
        self.assertFalse(is_perfect_square(8))
        self.assertFalse(is_perfect_square(10))
        self.assertFalse(is_perfect_square(11))

    def test_edge_cases(self):
        # Test edge cases like 0, 1 and a very large number
        self.assertTrue(is_perfect_square(0))  # 0 is a perfect square
        self.assertTrue(is_perfect_square(1))  # Edge case where the number itself is 1
        self.assertFalse(
            is_perfect_square(2147483647)
        )  # Large number that's not a perfect square

    def test_numbers_around_perfect_squares(self):
        # Testing numbers that are close to perfect squares
        self.assertFalse(is_perfect_square(15))  # Close to 16
        self.assertFalse(is_perfect_square(17))  # Close to 16
        self.assertFalse(is_perfect_square(24))  # Close to 25
        self.assertFalse(is_perfect_square(26))  # Close to 25
