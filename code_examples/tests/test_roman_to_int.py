import unittest
from src.roman_to_int import roman_to_int


class TestRomanToInt(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(roman_to_int("III"), 3)

    def test_example2(self):
        self.assertEqual(roman_to_int("LVIII"), 58)

    def test_example3(self):
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
