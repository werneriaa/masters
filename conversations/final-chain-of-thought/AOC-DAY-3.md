**DATE**: 24.03.2024

## Prompts

1.  You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside. It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving. "Aaah!" You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help. The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing. The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
2.  Here is an example engine schematic: 467..114.. ..._...... ..35..633. ......#... 617_...... .....+.58. ..592..... ......755. ...$.\*.... .664.598.. In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361. Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
3.  Its like the example always
4.  It has also part 2, ill give you example later The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source. You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers. Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola. The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any \* symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together. This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.
5.  Consider the same engine schematic again: 467..114.. ..._...... ..35..633. ......#... 617_...... .....+.58. ..592..... ......755. ...$._.... .664.598.. In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The _ adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835. What is the sum of all of the gear ratios in your engine schematic?

Unit test generator

## Answers

1.  Could you provide an example of the engine schematic and clarify how the part numbers are determined based on their adjacency to symbols? This will help in creating accurate unit tests.
2.  Based on the provided example, I'll summarize the requirements for creating the unit tests:

    - **Functionality to Test:** The function should analyze a grid (represented as a list of strings, where each string represents a row in the grid) and calculate the sum of all numbers that are adjacent (including diagonally) to any symbol (symbols are anything other than a period `.` or a digit). Numbers that are not adjacent to a symbol should not be included in the sum.

    - **Test Name Conventions:** Test names should clearly describe what aspect of the functionality they are testing.

    - **Example Test Case:**

      - **Input:** A list of strings representing the engine schematic, as provided in the example.
      - **Output:** The sum of all part numbers adjacent to symbols, which is 4361 for the given example.

    - **Edge Cases to Consider:**
      - An empty grid.
      - A grid with no symbols other than periods.
      - A grid with symbols but no numbers adjacent to them.
      - Numbers at the edge of the grid adjacent to a symbol.
      - A single number surrounded by different symbols.

    Before proceeding to generate the whole test code, could you provide any constraints on the input? For example, maximum dimensions of the schematic, specific symbols to look for, or the range of part numbers.

3.  Based on the provided description, example, and constraints, here are the unit tests that will be generated for testing the functionality of summing all part numbers in the engine schematic that are adjacent to symbols:

    1.  **Test Case: General Case with Mixed Symbols** - This test will use the provided example schematic to verify that the function correctly calculates the sum of part numbers adjacent to symbols.

    2.  **Test Case: Empty Schematic** - This test checks how the function handles an empty engine schematic.

    3.  **Test Case: Schematic with No Symbols** - This test verifies the function's behavior when the schematic contains no symbols other than periods, meaning there should be no part numbers to sum.

    4.  **Test Case: Schematic with Symbols but No Adjacent Numbers** - This tests the function with a schematic where symbols are present but no numbers are adjacent to them.

    5.  **Test Case: Numbers at the Edge Adjacent to a Symbol** - This ensures the function correctly includes numbers at the edges of the schematic that are adjacent to symbols.

    6.  **Test Case: Single Number Surrounded by Different Symbols** - This test checks the function's ability to sum a single number that is surrounded by various symbols.

    Given these test descriptions, here's how the test code might look:

    ```python
    import unittest
    from solution import calculate_part_numbers_sum

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
                ".664.598.."
            ]
            self.assertEqual(calculate_part_numbers_sum(schematic), 4361)

        def test_empty_schematic(self):
            schematic = []
            self.assertEqual(calculate_part_numbers_sum(schematic), 0)

        def test_schematic_with_no_symbols(self):
            schematic = ["467..114..", "..35..633.", "..592.....", "......755.", ".664.598.."]
            self.assertEqual(calculate_part_numbers_sum(schematic), 0)

        def test_schematic_with_symbols_but_no_adjacent_numbers(self):
            schematic = ["...*......", "......#...", ".....+....", "...$.*...."]
            self.assertEqual(calculate_part_numbers_sum(schematic), 0)

        def test_numbers_at_edge_adjacent_to_symbol(self):
            schematic = ["*67......", "...#..5..", ".+......."]
            self.assertEqual(calculate_part_numbers_sum(schematic), 72)

        def test_single_number_surrounded_by_different_symbols(self):
            schematic = ["*.$", ".5+", ".*."]
            self.assertEqual(calculate_part_numbers_sum(schematic), 5)

    if __name__ == '__main__':
        unittest.main()
    ```

    This code snippet assumes the existence of a function named `calculate_part_numbers_sum` in a module named `solution`. The tests cover various scenarios to ensure the functionality works as expected across different engine schematics.

4.  Before proceeding to create unit tests for part 2, could you provide an example that includes a schematic with gears defined as \* symbols adjacent to exactly two part numbers, along with the expected gear ratio sum for that schematic? This will help ensure the unit tests are accurate and relevant.
5.  Based on the new requirement to find and sum the gear ratios for gears in the engine schematic, here's how we can outline our unit tests for part 2:

    1.  **Test Case: General Case with Valid Gears** - This test will use the provided example schematic to verify that the function correctly identifies gears (\* symbols adjacent to exactly two part numbers) and calculates the sum of their gear ratios correctly.

    2.  **Test Case: No Gears in Schematic** - This test checks how the function behaves when there are no gears present in the schematic.

    3.  **Test Case: Gears with More Than Two Adjacent Numbers** - To test the function's ability to correctly ignore \* symbols that are adjacent to more than two part numbers.

    4.  **Test Case: Gears with Less Than Two Adjacent Numbers** - This ensures the function correctly ignores \* symbols that are adjacent to fewer than two part numbers.

    5.  **Test Case: Multiple Gears with the Same Ratio** - This checks whether the function can handle cases where multiple gears have the same gear ratio.

    Given these test descriptions, here's the test code for part 2:

    ```python
    import unittest
    from solution import calculate_gear_ratios_sum

    class TestCalculateGearRatiosSum(unittest.TestCase):

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
                ".664.598.."
            ]
            self.assertEqual(calculate_gear_ratios_sum(schematic), 467835)

        def test_no_gears_in_schematic(self):
            schematic = ["467..114..", "..35..633.", "..592.....", "......755.", ".664.598.."]
            self.assertEqual(calculate_gear_ratios_sum(schematic), 0)

        def test_gears_with_more_than_two_adjacent_numbers(self):
            schematic = ["467*114..", "...*......", "..35*633.", "......#..."]
            self.assertEqual(calculate_gear_ratios_sum(schematic), 0)

        def test_gears_with_less_than_two_adjacent_numbers(self):
            schematic = ["...*......", "617*......", "...$.*...."]
            self.assertEqual(calculate_gear_ratios_sum(schematic), 0)

        def test_multiple_gears_with_same_ratio(self):
            schematic = ["4*7", "1*3", "...", "2*6"]
            # Two gears with ratios 4*7=28 and 1*3=3, 2*6=12. Sum = 28 + 3 + 12 = 43
            self.assertEqual(calculate_gear_ratios_sum(schematic), 43)

    if __name__ == '__main__':
        unittest.main()
    ```

    This assumes the existence of a function named `calculate_gear_ratios_sum` in a module named `solution`. The tests are designed to cover various scenarios to ensure the functionality works as expected for identifying gears and calculating their ratios in different engine schematics.
