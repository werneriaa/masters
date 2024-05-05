import unittest
from day3.day3 import part1, part2


class TestCalculatePartNumbersSum(unittest.TestCase):

    def test_general_case_with_mixed_symbols(self):
        schematic = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        self.assertEqual(part1(schematic), 4361)

    def test_empty_schematic(self):
        schematic = []
        self.assertEqual(part1(schematic), 0)

    def test_schematic_with_no_symbols(self):
        schematic = [
            "467..114..",
            "..35..633.",
            "..592.....",
            "......755.",
            ".664.598..",
        ]
        self.assertEqual(part1(schematic), 0)

    def test_schematic_with_symbols_but_no_adjacent_numbers(self):
        schematic = ["...*......", "......#...", ".....+....", "...$.*...."]
        self.assertEqual(part1(schematic), 0)

    def test_numbers_at_edge_adjacent_to_symbol(self):
        schematic = ["*67......", "...#..5..", ".+......."]
        self.assertEqual(part1(schematic), 72)

    def test_single_number_surrounded_by_different_symbols(self):
        schematic = ["*.$", ".5+", ".*."]
        self.assertEqual(part1(schematic), 5)

    # PART 2

    def test_general_case_with_valid_gears(self):
        schematic = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        self.assertEqual(part2(schematic), 467835)

    def test_no_gears_in_schematic(self):
        schematic = [
            "467..114..",
            "..35..633.",
            "..592.....",
            "......755.",
            ".664.598..",
        ]
        self.assertEqual(part2(schematic), 0)

    def test_gears_with_more_than_two_adjacent_numbers(self):
        schematic = ["467*114..", "...*......", "..35*633.", "......#..."]
        self.assertEqual(part2(schematic), 0)

    def test_gears_with_less_than_two_adjacent_numbers(self):
        schematic = ["...*......", "617*......", "...$.*...."]
        self.assertEqual(part2(schematic), 0)

    def test_multiple_gears_with_same_ratio(self):
        schematic = ["4*7", "1*3", "...", "2*6"]
        # Two gears with ratios 4*7=28 and 1*3=3, 2*6=12. Sum = 28 + 3 + 12 = 43
        self.assertEqual(part2(schematic), 43)


if __name__ == '__main__':
    unittest.main()
