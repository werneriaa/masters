import unittest
from src.password_checker import strong_password_checker


class TestStrongPasswordChecker(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(strong_password_checker("a"), 5)

    def test_example2(self):
        self.assertEqual(strong_password_checker("aA1"), 3)

    def test_example3(self):
        self.assertEqual(strong_password_checker("1337C0d3"), 0)


if __name__ == '__main__':
    unittest.main()
