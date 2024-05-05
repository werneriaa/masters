import unittest
from src.minimum_numbers import minimum_numbers


class TestMinSetSize(unittest.TestCase):

    def test_valid_set_exists_small_set(self):
        self.assertEqual(
            minimum_numbers(58, 9),
            2,
            "Minimum set size with num=58 and k=9 should be 2",
        )

    def test_no_valid_set_exists(self):
        self.assertEqual(
            minimum_numbers(37, 2),
            -1,
            "It should return -1 when no valid set can be formed",
        )

    def test_sum_zero_empty_set(self):
        self.assertEqual(
            minimum_numbers(0, 7),
            0,
            "Minimum set size with num=0 should be 0 for any k",
        )

    def test_valid_set_exists_larger_sum(self):
        self.assertEqual(
            minimum_numbers(3000, 1),
            1,
            "Minimum set size with num=3000 and k=1 should be 1",
        )

    def test_valid_set_exists_edge_k(self):
        self.assertEqual(
            minimum_numbers(90, 0),
            1,
            "Minimum set size with num=90 and k=0 should be 1",
        )

    def test_valid_set_exists_with_minimum_possible_numbers(self):
        self.assertEqual(
            minimum_numbers(19, 9),
            1,
            "Minimum set size with num=19 and k=9 should be 1",
        )

    def test_upper_bound_num(self):
        self.assertGreaterEqual(
            minimum_numbers(3000, 9),
            1,
            "Function should handle upper boundary of num=3000 correctly",
        )


if __name__ == '__main__':
    unittest.main()
