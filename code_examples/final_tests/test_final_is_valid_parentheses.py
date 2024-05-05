import unittest
from src.is_valid_parentheses import is_valid_parentheses


class TestBracketSequence(unittest.TestCase):

    def test_single_pair_of_parentheses(self):
        self.assertTrue(is_valid_parentheses("()"))

    def test_multiple_types_of_matched_brackets(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_matched_but_incorrectly_ordered_brackets(self):
        self.assertFalse(is_valid_parentheses("(]"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parentheses(""))

    def test_nested_valid_parentheses_of_different_types(self):
        self.assertTrue(is_valid_parentheses("({[]})"))

    def test_string_starts_with_closing_parenthesis(self):
        self.assertFalse(is_valid_parentheses("]())"))

    def test_all_opening_no_closing_parentheses(self):
        self.assertFalse(is_valid_parentheses("(((("))

    def test_very_long_valid_string(self):
        self.assertTrue(
            is_valid_parentheses("()" * 5200)
        )  # Generates a string with 10400 characters

    def test_very_long_invalid_string(self):
        self.assertFalse(
            is_valid_parentheses("((((" * 2600)
        )  # Generates a string with 10400 characters


if __name__ == "__main__":
    unittest.main()
