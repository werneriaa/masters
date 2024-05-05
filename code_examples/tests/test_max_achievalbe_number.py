import unittest
from src.max_achievable_number import max_achievable_number


class TestMaxAchievableNumber(unittest.TestCase):
    def test_positive_num_and_t(self):
        self.assertEqual(max_achievable_number(5, 3), 11)

    def test_num_zero_positive_t(self):
        self.assertEqual(max_achievable_number(0, 4), 8)

    def test_negative_num_positive_t(self):
        self.assertEqual(max_achievable_number(-5, 3), 1)

    def test_positive_num_zero_t(self):
        self.assertEqual(max_achievable_number(5, 0), 5)

    def test_large_num_and_t(self):
        self.assertEqual(max_achievable_number(1000, 500), 2000)

    def test_opposite_signs_num_and_t(self):
        self.assertEqual(max_achievable_number(-5, 10), 15)


if __name__ == "__main__":
    unittest.main()
