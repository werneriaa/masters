import unittest
from src.median_of_two_arrays import find_median_sorted_arrays


class TestRomanToInt(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0000)

    def test_example2(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5000)


if __name__ == '__main__':
    unittest.main()
