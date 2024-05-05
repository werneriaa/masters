import unittest
from src.median_of_two_arrays import find_median_sorted_arrays


class TestFindMedianSortedArrays(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0)

    def test_example2(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)

    def test_empty_first_array(self):
        self.assertEqual(find_median_sorted_arrays([], [1, 2, 3, 4, 5]), 3.0)

    def test_empty_second_array(self):
        self.assertEqual(find_median_sorted_arrays([1, 2, 3, 4, 5], []), 3.0)

    def test_single_element_arrays(self):
        self.assertEqual(find_median_sorted_arrays([1], [2]), 1.5)

    def test_uneven_length_arrays(self):
        self.assertEqual(find_median_sorted_arrays([1, 2, 3, 4], [5, 6, 7, 8, 9]), 5.0)


if __name__ == '__main__':
    unittest.main()
