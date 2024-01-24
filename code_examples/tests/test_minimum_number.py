import unittest
from src.minimum_numbers import minimum_numbers


class TestTwoSumIndices(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(minimum_numbers(58, 9), 2)

    def test_example2(self):
        self.assertEqual(minimum_numbers(37, 2), -1)

    def test_example3(self):
        self.assertEqual(minimum_numbers(0, 7), 0)


if __name__ == '__main__':
    unittest.main()
