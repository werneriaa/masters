import unittest
from src.minimum_numbers import minimum_numbers


class TestMinSetSize(unittest.TestCase):
    # TN
    def test_example1(self):
        self.assertEqual(minimum_numbers(58, 9), 2, "Example 1 failed")

    # TN
    def test_example2(self):
        self.assertEqual(minimum_numbers(37, 2), -1, "Example 2 failed")

    # TN
    def test_example3(self):
        self.assertEqual(minimum_numbers(0, 7), 0, "Example 3 failed")

    # TN
    def test_sum_zero_with_non_zero_k(self):
        self.assertEqual(minimum_numbers(0, 5), 0, "Sum zero with non-zero k failed")

    # TN
    def test_k_zero_with_non_zero_num(self):
        self.assertEqual(minimum_numbers(10, 0), 1, "k zero with non-zero num failed")

    # FP
    def test_max_constraints(self):
        self.assertEqual(minimum_numbers(3000, 9), 334, "Max constraints failed")


if __name__ == "__main__":
    unittest.main()
