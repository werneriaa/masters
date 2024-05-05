# import unittest
# from src.roman_to_int import roman_to_int


# class TestRomanToInt(unittest.TestCase):
#     def test_single_symbol(self):
#         self.assertEqual(roman_to_int("I"), 1, "Should be 1")
#         self.assertEqual(roman_to_int("V"), 5, "Should be 5")
#         self.assertEqual(roman_to_int("X"), 10, "Should be 10")
#         self.assertEqual(roman_to_int("L"), 50, "Should be 50")
#         self.assertEqual(roman_to_int("C"), 100, "Should be 100")
#         self.assertEqual(roman_to_int("D"), 500, "Should be 500")
#         self.assertEqual(roman_to_int("M"), 1000, "Should be 1000")

#     def test_combined_symbols(self):
#         self.assertEqual(roman_to_int("III"), 3, "III should be 3")
#         self.assertEqual(roman_to_int("LVIII"), 58, "LVIII should be 58")
#         self.assertEqual(roman_to_int("MCMXCIV"), 1994, "MCMXCIV should be 1994")

#     def test_subtractive_notation(self):
#         self.assertEqual(roman_to_int("IV"), 4, "IV should be 4")
#         self.assertEqual(roman_to_int("IX"), 9, "IX should be 9")
#         self.assertEqual(roman_to_int("XL"), 40, "XL should be 40")
#         self.assertEqual(roman_to_int("XC"), 90, "XC should be 90")
#         self.assertEqual(roman_to_int("CD"), 400, "CD should be 400")
#         self.assertEqual(roman_to_int("CM"), 900, "CM should be 900")


# if __name__ == "__main__":
#     unittest.main()
