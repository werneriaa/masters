import unittest
from src.password_checker import strong_password_checker


class TestStrongPasswordChecker(unittest.TestCase):
    def test_short_password(self):
        self.assertEqual(strong_password_checker("aA1"), 3)

    def test_perfect_password(self):
        self.assertEqual(strong_password_checker("aA1!aA1!"), 0)

    def test_long_password(self):
        self.assertEqual(strong_password_checker("a" * 50), 36)

    def test_missing_types(self):
        self.assertEqual(strong_password_checker("aaaaaa"), 2)

    def test_no_changes_needed(self):
        self.assertEqual(strong_password_checker("123Ab!"), 0)

    def test_one_type_missing_long(self):
        self.assertEqual(strong_password_checker("AAAABBBBCCCCDDDD1234"), 4)

    def test_repetitive_characters(self):
        self.assertEqual(strong_password_checker("aaaaaAAAAA11111"), 3)

    def test_complex_case(self):
        self.assertEqual(strong_password_checker("abAB12"), 0)

    def test_only_digits_long(self):
        self.assertEqual(strong_password_checker("12345678901234567890"), 2)


if __name__ == '__main__':
    unittest.main()
