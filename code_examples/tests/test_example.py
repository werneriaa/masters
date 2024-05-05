import unittest
from src.example_1 import add, subtract, multiply, divide


class TestCalculus(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(5, 6), 30)

    def test_add(self):
        self.assertEqual(add(25, 31), 56)

    def test_subtract(self):
        self.assertEqual(subtract(128, 64), 64)

    def test_divide(self):
        self.assertEqual(divide(36, 6), 6)


if __name__ == '__main__':
    unittest.main()
