import unittest
from src.max_achievable_number import max_achievable_number


class TestMaxAchievableNumber(unittest.TestCase):

    def test_max_achievable_with_small_gap(self):
        self.assertEqual(
            max_achievable_number(4, 1), 6, "Should return 6 for num=4, t=1"
        )

    def test_max_achievable_with_larger_gap(self):
        self.assertEqual(
            max_achievable_number(3, 2), 7, "Should return 7 for num=3, t=2"
        )

    def test_max_achievable_with_min_values(self):
        self.assertEqual(
            max_achievable_number(1, 1), 3, "Should return 3 for num=1, t=1"
        )

    def test_max_achievable_with_max_values(self):
        self.assertEqual(
            max_achievable_number(50, 50), 150, "Should return 150 for num=50, t=50"
        )

    def test_max_achievable_with_no_change(self):
        self.assertEqual(
            max_achievable_number(10, 0), 10, "Should return 10 for num=10, t=0"
        )


if __name__ == '__main__':
    unittest.main()
