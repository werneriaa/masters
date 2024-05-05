import unittest
from src.min_cuts import min_cut


class TestMinCut(unittest.TestCase):

    def test_single_character_string(self):
        self.assertEqual(min_cut("a"), 0)

    def test_string_already_palindrome(self):
        self.assertEqual(min_cut("racecar"), 0)

    def test_string_with_all_identical_characters(self):
        self.assertEqual(min_cut("aaaa"), 0)

    def test_string_needs_multiple_cuts(self):
        # For "ababbbabbababa", the minimum cuts are 3 -> a | babbbab | b | ababa
        self.assertEqual(min_cut("ababbbabbababa"), 3)

    def test_long_string_with_complex_palindrome_structure(self):
        # Assuming a complex palindrome structure, potentially requiring deep analysis
        self.assertEqual(
            min_cut("aaabbaaccdcc"), 2
        )  # a | aaabbaaccdcc | a, for example

    def test_non_palindromic_string(self):
        # Every character has to be its own substring
        self.assertEqual(min_cut("abcde"), 4)


if __name__ == "__main__":
    unittest.main()
