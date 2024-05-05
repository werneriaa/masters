import unittest
from src.min_cuts import min_cut


class TestMinPalindromeCuts(unittest.TestCase):
    def test_single_cut_partition(self):
        self.assertEqual(min_cut("aab"), 1, "Should require 1 cut for 'aab'")

    def test_single_character_string(self):
        self.assertEqual(
            min_cut("a"), 0, "Should require 0 cuts for a single character"
        )

    def test_two_character_non_palindrome(self):
        self.assertEqual(min_cut("ab"), 1, "Should require 1 cut for 'ab'")

    def test_longer_string_various_cases(self):
        self.assertEqual(min_cut("abbac"), 1, "Should require 1 cut for 'abbac'")

    def test_maximum_length_string(self):
        # Assuming 'a'*2000 is the input string, which is already a palindrome and should require 0 cuts
        self.assertEqual(
            min_cut("a" * 2000), 0, "Should handle maximum length string with 0 cuts"
        )


if __name__ == '__main__':
    unittest.main()
