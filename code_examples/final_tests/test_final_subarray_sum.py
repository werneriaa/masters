import unittest
from src.maximum_subarray_sum import (
    maximum_subarray_sum,
)  # Assuming the function is named maximum_subarray_sum


class TestMaxSumOfGoodSubarray(unittest.TestCase):
    def test_increasing_sequence_small_k(self):
        self.assertEqual(maximum_subarray_sum([1, 2, 3, 4, 5, 6], 1), 11)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(maximum_subarray_sum([-1, 3, 2, 4, 5], 3), 11)

    def test_all_negative_numbers(self):
        self.assertEqual(maximum_subarray_sum([-1, -2, -3, -4], 2), -6)

    def test_minimum_array_length(self):
        self.assertEqual(maximum_subarray_sum([100, 101], 1), 201)

    def test_no_good_subarrays(self):
        self.assertEqual(maximum_subarray_sum([10, 30, 50, 70], 20), 0)

    def test_large_array_and_values(self):
        nums = [i for i in range(1, 100001)]  # Large increasing sequence
        self.assertIsInstance(
            maximum_subarray_sum(nums, 99999), int
        )  # Checking for correct type due to large sum


if __name__ == '__main__':
    unittest.main()
