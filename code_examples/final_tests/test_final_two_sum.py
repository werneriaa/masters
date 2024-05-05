import unittest
from src.two_sum import two_sum


class TestFindTwoSum(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(
            sorted(two_sum([2, 7, 11, 15], 9)),
            [0, 1],
            "Should return indices [0, 1] for target 9",
        )

    def test_non_adjacent_elements(self):
        self.assertEqual(
            sorted(two_sum([3, 2, 4], 6)),
            [1, 2],
            "Should return indices [1, 2] for target 6",
        )

    def test_duplicate_elements(self):
        self.assertEqual(
            sorted(two_sum([3, 3], 6)),
            [0, 1],
            "Should return indices [0, 1] for duplicate elements adding to target 6",
        )

    def test_large_range_of_numbers(self):
        nums = list(range(-5000, 5000))
        target = nums[4999] + nums[4998]
        self.assertEqual(
            sorted(two_sum(nums, target)),
            [4998, 4999],
            "Should handle a large range of numbers efficiently",
        )

    def test_with_negative_numbers(self):
        self.assertEqual(
            sorted(two_sum([-1, -2, -3, -4, -5], -8)),
            [2, 4],
            "Should correctly find indices when array contains negative numbers",
        )


if __name__ == '__main__':
    unittest.main()
