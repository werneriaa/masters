import unittest
from src.max_strength import max_strength


class TestMaxStrength(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(max_strength([3, -1, -5, 2, 5, -9]), 1350)

    def test_basic_two(self):
        self.assertEqual(max_strength([-4, -5, -4]), 20)

    def test_lenght_one(self):
        self.assertEqual(max_strength([5]), 5)

    def test_lenght_two_negative(self):
        self.assertEqual(max_strength([5, -1, -3]), 15)

    def test_one_in_test(self):
        self.assertEqual(max_strength([5, -1, -1]), 5)


if __name__ == '__main__':
    unittest.main()
