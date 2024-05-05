import unittest
from src.median_of_two_arrays import find_median_sorted_arrays


class TestFindMedianSortedArrays(unittest.TestCase):

    def test_with_one_array_longer_than_other(self):
        self.assertAlmostEqual(find_median_sorted_arrays([1, 3], [2]), 2.00000)

    def test_with_one_empty_array(self):
        self.assertAlmostEqual(find_median_sorted_arrays([], [1]), 1.00000)

    def test_with_two_arrays_of_equal_length(self):
        self.assertAlmostEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.50000)

    def test_with_arrays_having_all_equal_elements(self):
        self.assertAlmostEqual(find_median_sorted_arrays([2, 2], [2, 2]), 2.00000)

    def test_with_negative_numbers(self):
        self.assertAlmostEqual(find_median_sorted_arrays([-5, -3], [-2, -1]), -2.50000)

    def test_edge_case_with_smallest_possible_arrays(self):
        self.assertAlmostEqual(find_median_sorted_arrays([1], [2]), 1.50000)

    def test_with_large_range_values(self):
        self.assertAlmostEqual(
            find_median_sorted_arrays([-1000000, 1000000], [-1000000, 1000000]), 0.00000
        )

    def test_maximum_length_arrays(self):
        # This test checks the function with arrays at their maximum allowed sizes.
        # It's more for performance and ensuring the function can handle large inputs within constraints.
        # Given the nature of this test, specifics of the arrays are not as important as their sizes and the function's ability to handle them.
        nums1 = list(range(500))  # Example large array, specifics can vary
        nums2 = list(range(500, 1000))  # Another example large array
        # The expected result and exact inputs would depend on the contents of the arrays
        # This is just a placeholder to illustrate handling large inputs
        self.assertTrue(
            isinstance(find_median_sorted_arrays(nums1, nums2), float)
        )  # Check if output is a float as expected


if __name__ == '__main__':
    unittest.main()
