import unittest
from day1.day1 import convert_to_int, part1, part2


class TestConvertToInt(unittest.TestCase):
    def test_convert_to_int(self):
        self.assertEqual(convert_to_int('one'), '1')
        self.assertEqual(convert_to_int('two'), '2')


class TestPart1(unittest.TestCase):
    def test_part1(self):
        # Test part1 with a test file
        result = part1('./inputs/test_part1.txt')
        self.assertEqual(result, 142)  # Replace expected_value


class TestPart2(unittest.TestCase):
    def test_part2(self):
        # Test part2 with a test file
        result = part2('./inputs/test_part2.txt')
        self.assertEqual(result, 281)  # Replace expected_value


if __name__ == '__main__':
    unittest.main()
