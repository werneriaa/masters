import unittest
from src.median_of_two_arrays import find_median_sorted_arrays


class TestFindMedianSortedArrays(unittest.TestCase):

    # TN
    def test_single_element_each(self):
        self.assertEqual(find_median_sorted_arrays([1], [2]), 1.5)

    # TN
    def test_single_element_one_empty(self):
        self.assertEqual(find_median_sorted_arrays([], [1]), 1.0)

    # TN
    def test_two_elements_each_even_total(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)

    # TN
    def test_two_elements_each_odd_total(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0)

    # FP
    def test_with_negative_numbers(self):
        self.assertEqual(find_median_sorted_arrays([-5, -3, -1], [0, 2, 4]), -1.0)

    # TN
    def test_large_numbers(self):
        self.assertEqual(find_median_sorted_arrays([100000], [100001]), 100000.5)

    # TN
    def test_empty_first_array(self):
        self.assertEqual(find_median_sorted_arrays([], [1, 2, 3, 4, 5]), 3.0)

    # TN
    def test_empty_second_array(self):
        self.assertEqual(find_median_sorted_arrays([1, 2, 3, 4, 5], []), 3.0)


if __name__ == '__main__':
    unittest.main()
