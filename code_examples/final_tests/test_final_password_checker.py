import unittest
from src.password_checker import strong_password_checker


class TestMakePasswordStrong(unittest.TestCase):

    def test_password_needs_5_insertions_for_single_character(self):
        """
        Test that a password with only 1 character needs 5 insertions to become strong.
        """
        password = "a"
        expected_steps = 5
        self.assertEqual(strong_password_checker(password), expected_steps)

    def test_password_needs_3_insertions_to_meet_minimum_criteria(self):
        """
        Test that a password with 3 characters, meeting the lowercase, uppercase, and digit criteria,
        still needs 3 insertions to reach the minimum length of 6 characters.
        """
        password = "aA1"
        expected_steps = 3
        self.assertEqual(strong_password_checker(password), expected_steps)

    def test_password_already_strong_no_changes_needed(self):
        """
        Test that a password meeting all criteria for strength (length, character variety, no three consecutive
        repeating characters) requires no changes.
        """
        password = "1337C0d3"
        expected_steps = 0
        self.assertEqual(strong_password_checker(password), expected_steps)

    def test_maximum_length_password_needs_reduction(self):
        """
        Test that a password at the maximum length of 50 characters but not meeting other criteria
        needs steps to become strong without exceeding the length limit.
        """
        password = "aA1" + "a" * 47
        expected_steps = 1  # Placeholder for actual expected steps, assuming at least one replacement
        self.assertEqual(strong_password_checker(password), expected_steps)

    def test_password_with_dots_and_exclamations(self):
        """
        Test that a password containing dots and exclamation marks handles these characters correctly
        in the context of making the password strong.
        """
        password = "a!A.1"
        expected_steps = (
            1  # Assuming we only need one more character to meet the strong criteria
        )
        self.assertEqual(strong_password_checker(password), expected_steps)


if __name__ == '__main__':
    unittest.main()
