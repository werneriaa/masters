# import unittest
# from src.is_valid_parentheses import is_valid_parentheses


# class TestIsValidString(unittest.TestCase):
#     def test_empty_string(self):
#         self.assertTrue(is_valid_parentheses(""))

#     def test_single_type_parentheses(self):
#         self.assertTrue(is_valid_parentheses("()"))

#     def test_mixed_type_parentheses(self):
#         self.assertTrue(is_valid_parentheses("()[]{}"))

#     def test_invalid_order_parentheses(self):
#         self.assertFalse(is_valid_parentheses("(]"))

#     def test_long_valid_sequence(self):
#         self.assertTrue(is_valid_parentheses("([]){()}[[{}]]"))

#     def test_long_invalid_sequence(self):
#         self.assertFalse(is_valid_parentheses("([{])"))

#     def test_unmatched_open_parentheses(self):
#         self.assertFalse(is_valid_parentheses("(((("))

#     def test_unmatched_close_parentheses(self):
#         self.assertFalse(is_valid_parentheses("))))"))

#     def test_complex_valid_sequence(self):
#         self.assertTrue(is_valid_parentheses("{[()]}[{}]"))

#     def test_complex_invalid_sequence(self):
#         self.assertFalse(is_valid_parentheses("{[(])}[{}]"))


# if __name__ == "__main__":
#     unittest.main()
