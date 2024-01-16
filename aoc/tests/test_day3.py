import unittest
from day3.day3 import part1, part2, read_input

class TestDayThreePartOne(unittest.TestCase):

    def test_part_one_engine(self):
        engine = read_input(3, True) 
        
        self.assertEqual(part1(engine), 4361)

class TestDayThreePartTwo(unittest.TestCase):

    def test_part_two_engine(self):
        engine = read_input(3, True) 
        
        self.assertEqual(part2(engine), 467835)


if __name__ == '__main__':
    unittest.main()
