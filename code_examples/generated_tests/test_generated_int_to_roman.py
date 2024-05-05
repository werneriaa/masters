# import unittest
# from src.int_to_roman import int_to_roman


# class TestIntToRoman(unittest.TestCase):
#     def test_single_digit(self):
#         self.assertEqual(
#             int_to_roman(3),
#             "III",
#             "Should convert single digit to Roman numeral correctly",
#         )

#     def test_double_digit(self):
#         self.assertEqual(
#             int_to_roman(58),
#             "LVIII",
#             "Should convert double digits to Roman numeral correctly",
#         )

#     def test_triple_digit(self):
#         self.assertEqual(
#             int_to_roman(294),
#             "CCXCIV",
#             "Should convert triple digits to Roman numeral correctly",
#         )

#     def test_four_digit(self):
#         self.assertEqual(
#             int_to_roman(1994),
#             "MCMXCIV",
#             "Should convert four digits to Roman numeral correctly",
#         )

#     def test_minimum_value(self):
#         self.assertEqual(
#             int_to_roman(1),
#             "I",
#             "Should convert the minimum value to Roman numeral correctly",
#         )

#     def test_maximum_value(self):
#         self.assertEqual(
#             int_to_roman(3999),
#             "MMMCMXCIX",
#             "Should convert the maximum value to Roman numeral correctly",
#         )


# if __name__ == "__main__":
#     unittest.main()
