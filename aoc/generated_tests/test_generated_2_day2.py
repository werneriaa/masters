import unittest
from day1.day1 import sum_calibration_values, sum_calibration_values_part2


class TestSnowCalibration(unittest.TestCase):

    def test_basic_input(self):
        """Test function with basic input."""
        self.assertEqual(
            sum_calibration_values(
                ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
            ),
            142,
        )

    def test_single_digit_duplicated(self):
        """Test strings with a single digit, ensuring the digit is duplicated."""
        self.assertEqual(sum_calibration_values(['abc1', '2def', 'g3']), 11 + 22 + 33)

    def test_with_special_characters(self):
        """Test strings containing special characters alongside digits."""
        self.assertEqual(sum_calibration_values(['!1@#2$', '%3^&*4(']), 12 + 34)

    def test_empty_string(self):
        """Test handling of an empty string within the list."""
        self.assertEqual(sum_calibration_values(['', '1a2', 'b3c4']), 12 + 34)

    def test_large_input_set(self):
        """Test function with a large input set to evaluate performance."""
        large_input = ['1a2'] * 1000  # Repeat '1a2' 1000 times
        self.assertEqual(sum_calibration_values(large_input), 12 * 1000)

    def test_all_strings_have_at_least_one_digit(self):
        """Test that all strings have at least one digit, handling edge cases accordingly."""
        self.assertEqual(
            sum_calibration_values(['x5x', 'y']), 55
        )  # Assuming 'y' somehow got through with a digit

    ## PART 2-----

    def test_with_spelled_out_numbers(self):
        """Test function with numbers spelled out in words."""
        self.assertEqual(
            sum_calibration_values_part2(
                [
                    'two1nine',
                    'eightwothree',
                    'abcone2threexyz',
                    'xtwone3four',
                    '4nineeightseven2',
                    'zoneight234',
                    '7pqrstsixteen',
                ]
            ),
            281,
        )

    def test_mixed_numerals_and_words(self):
        """Test strings containing both numerals and spelled-out numbers."""
        self.assertEqual(sum_calibration_values_part2(['1one1', 'tw2two']), 11 + 22)

    def test_spelled_out_numbers_at_start_and_end(self):
        """Ensure correct processing with spelled-out numbers at start and end of strings."""
        self.assertEqual(
            sum_calibration_values_part2(['onetwo3fourfive', 'six7eight']), 15 + 68
        )

    def test_handling_uppercase_and_mixed_case_words(self):
        """Test handling of uppercase and mixed-case spelled-out numbers."""
        self.assertEqual(
            sum_calibration_values_part2(['THREE3seven', 'fOuR4six']), 37 + 46
        )

    def test_large_input_with_spelled_out_numbers(self):
        """Test function performance with a large input set including spelled-out numbers."""
        large_input = ['one2three'] * 1000  # Repeat 'one2three' 1000 times
        self.assertEqual(sum_calibration_values_part2(large_input), 13 * 1000)

    def test_with_special_characters_and_spelled_out_numbers(self):
        """Test strings with special characters and spelled-out numbers."""
        self.assertEqual(
            sum_calibration_values_part2(['!one@#2$', '%three^&*four(']), 12 + 34
        )


if __name__ == '__main__':
    unittest.main()
