import unittest
from day4.day4 import part_1, part_2


class TestScratchcardCalculatorWithPrefix(unittest.TestCase):
    def test_multiple_matches_with_prefix(self):
        input_str = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        self.assertEqual(
            part_1(input_str),
            8,
            "Should calculate points correctly for multiple matches with card prefix",
        )

    def test_mixed_results_with_prefixes(self):
        input_str = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
        self.assertEqual(
            part_1(input_str),
            13,
            "Should calculate total points correctly for mixed results with card prefixes",
        )

    def test_original_and_copies(self):
        input_str = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
        self.assertEqual(
            part_2(input_str),
            30,
            "Should calculate the total number of scratchcards including originals and all copies won correctly",
        )


if __name__ == "__main__":
    unittest.main()
