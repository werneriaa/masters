import unittest
from src.zigzac_conversion import convert


class TestConvertFunction(unittest.TestCase):

    def test_single_row(self):
        self.assertEqual(convert("hello", 1), "hello")

    def test_rows_equal_to_string_length(self):
        self.assertEqual(convert("hello", 5), "hello")

    def test_typical_string_and_row_number(self):
        self.assertEqual(convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_numRows_greater_than_string_length(self):
        self.assertEqual(convert("short", 10), "short")

    def test_empty_string(self):
        self.assertEqual(convert("", 3), "")

    def test_special_characters_and_spaces(self):
        self.assertEqual(convert("h e l!lo", 3), "hl  !oel")

    def test_very_long_string(self):
        long_string = "a" * 1000  # 1000 characters long
        self.assertEqual(
            convert(long_string, 2), long_string
        )  # As it will just zigzag between two rows


if __name__ == "__main__":
    unittest.main()
