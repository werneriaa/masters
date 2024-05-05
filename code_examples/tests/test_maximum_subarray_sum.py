import unittest
from src.maximum_subarray_sum import maximum_subarray_sum


class TestMaximumSubarraySum(unittest.TestCase):

    def test_normal_case_positive_numbers(self):
        self.assertEqual(maximum_subarray_sum([1, 2, 3, 4, 5], 1), 9)

    def test_array_with_negative_numbers(self):
        self.assertEqual(maximum_subarray_sum([-2, -1, -3, -4, -1], 1), -3)

    def test_array_with_positive_and_negative_numbers(self):
        self.assertEqual(maximum_subarray_sum([1, -2, 3, 10, -4, 7, 2, -5], 3), 13)

    def test_empty_array(self):
        self.assertEqual(maximum_subarray_sum([], 5), 0)

    def test_array_with_one_element(self):
        self.assertEqual(maximum_subarray_sum([10], 5), 0)

    def test_k_value_does_not_allow_valid_subarrays(self):
        self.assertEqual(maximum_subarray_sum([1, 3, 6, 10], 5), 10)

    def test_large_array_with_large_numbers(self):
        self.assertEqual(maximum_subarray_sum([100, 200, 300, 400] * 250, 50), 0)

    def test_example_one(self):
        self.assertEqual(maximum_subarray_sum([1, 2, 3, 4, 5, 6], 1), 1)

    def test_example_one(self):
        self.assertEqual(maximum_subarray_sum([3, 3, 2], 1), 8)


if __name__ == '__main__':
    unittest.main()
