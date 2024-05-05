import unittest
from src.zigzac_conversion import (
    convert,
)  # Assuming the function is defined in a file named placeholder.py


class TestZigzagConversion(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(
            convert("PAYPALISHIRING", 3),
            "PAHNAPLSIIGYIR",
            "Should convert string to zigzag pattern and read it line by line for numRows=3",
        )

    def test_example_2(self):
        self.assertEqual(
            convert("PAYPALISHIRING", 4),
            "PINALSIGYAHRPI",
            "Should convert string to zigzag pattern and read it line by line for numRows=4",
        )

    def test_example_3(self):
        self.assertEqual(convert("A", 1), "A", "Should handle single character string")

    def test_all_uppercase_string(self):
        self.assertEqual(
            convert("ABCDEFG", 2),
            "ACEGBDF",
            "Should correctly handle all uppercase string",
        )

    def test_string_with_comma_and_period(self):
        self.assertEqual(
            convert("A,B.C", 2),
            "A.CB,",
            "Should correctly handle string with commas and periods",
        )

    def test_large_num_rows(self):
        self.assertEqual(
            convert("PAYPALISHIRING", 1000),
            "PAYPALISHIRING",
            "Should return the original string if numRows is greater than the string length",
        )

    def test_single_row(self):
        self.assertEqual(
            convert("PAYPALISHIRING", 1),
            "PAYPALISHIRING",
            "Should return the original string if numRows is 1",
        )


if __name__ == "__main__":
    unittest.main()
