import unittest
from src.minimum_numbers import minimum_numbers


class TestMinimumNumbers(unittest.TestCase):
    def test_zero_num(self):
        self.assertEqual(minimum_numbers(0, 5), 0)

    def test_num_less_than_k(self):
        self.assertEqual(minimum_numbers(7, 9), -1)

    def test_num_equal_k(self):
        self.assertEqual(minimum_numbers(9, 9), 1)

    def test_possible_combination(self):
        self.assertEqual(minimum_numbers(58, 9), 2)

    def test_impossible_combination(self):
        self.assertEqual(minimum_numbers(37, 8), -1)

    def test_large_num(self):
        self.assertEqual(minimum_numbers(1000, 1), 10)

    def test_large_num_impossible_combination(self):
        self.assertEqual(minimum_numbers(1000, 3), 10)

    def test_k_equals_zero_num_not_zero(self):
        self.assertEqual(minimum_numbers(10, 0), 1)

    def test_k_equals_zero_num_zero(self):
        self.assertEqual(minimum_numbers(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
