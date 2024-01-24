import unittest
from src.max_strength import max_strength


class TestMaxStrength(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_strength([3, -1, -5, 2, 5, -9]), 1350)

    def test_example2(self):
        self.assertEqual(max_strength([-4, -5, -4]), 20)


if __name__ == '__main__':
    unittest.main()
