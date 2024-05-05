import unittest
from day1.day1 import sum_calibration_values, sum_calibration_values_part2


class TestSumCalibrationValues(unittest.TestCase):

    # TN
    def test_empty_document(self):
        """Test that an empty document returns a sum of 0."""
        self.assertEqual(sum_calibration_values([]), 0)

    # TN
    def test_single_line_document(self):
        """Test documents with a single line."""
        self.assertEqual(sum_calibration_values(["1abc2"]), 12)
        self.assertEqual(sum_calibration_values(["pqr3stu8vwx"]), 38)
        self.assertEqual(sum_calibration_values(["a1b2c3d4e5f"]), 15)
        self.assertEqual(sum_calibration_values(["treb7uchet"]), 77)

    # TN
    def test_multiple_lines_document(self):
        """Test documents with multiple lines."""
        document = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(sum_calibration_values(document), 142)

    # TN
    def test_lines_with_no_digits(self):
        """Test lines that do not contain any digits."""
        self.assertEqual(sum_calibration_values(["abcdefg", "xyz"]), 0)

    # FP
    def test_lines_with_single_digit(self):
        """Test lines with only one digit, which should be ignored."""
        self.assertEqual(sum_calibration_values(["a1bcdefg", "xy2z"]), 0)

    # TN
    def test_line_with_digits_at_ends(self):
        """Test lines where digits are at the very beginning and end."""
        self.assertEqual(sum_calibration_values(["9abcdefgh1"]), 91)

    ## PART 2 TESTS

    # TN
    def test_with_text_digits(self):
        """Test documents with spelled out digits."""
        document = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
        self.assertEqual(sum_calibration_values_part2(document), 281)

    # TN
    def test_mixed_text_and_numeric_digits(self):
        """Test lines with both spelled out and numeric digits."""
        self.assertEqual(sum_calibration_values_part2(["one2three"]), 13)
        self.assertEqual(sum_calibration_values_part2(["four5six"]), 46)
        self.assertEqual(sum_calibration_values_part2(["seven8nine"]), 79)

    # TN
    def test_spelled_out_digits_only(self):
        """Test lines with only spelled out digits."""
        self.assertEqual(sum_calibration_values_part2(["oneeight"]), 18)
        self.assertEqual(sum_calibration_values_part2(["twoseven"]), 27)
        self.assertEqual(sum_calibration_values_part2(["threefour"]), 34)

    # FP
    def test_spelled_out_single_digit(self):
        """Test lines with a single spelled out digit, which should be ignored."""
        self.assertEqual(sum_calibration_values_part2(["onetwo"]), 0)
        self.assertEqual(sum_calibration_values_part2(["three"]), 0)

    # TP
    def test_empty_and_no_digit_lines(self):
        """Test empty lines and lines with no digits."""
        document = ["", "abcdefg", "onetwo", "xyz"]
        self.assertEqual(sum_calibration_values_part2(document), 0)


if __name__ == "__main__":
    unittest.main()
