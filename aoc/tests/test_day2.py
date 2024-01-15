import unittest
from collections import namedtuple
from day2.day2 import parse_game_input, validate, calculate_total_power, calculate_power, Game, Round

class TestTransformer(unittest.TestCase):

    def test_parse_game_input(self):
        expected_output = Game(id=1, rounds=[Round(blue=3, red=0, green=0), Round(blue=3, red=4, green=0), Round(blue=0, red=1, green=0), Round(blue=0, red=1, green=2), Round(blue=6, red=1, green=2), Round(blue=0, red=0, green=2)])
        self.assertEqual(parse_game_input('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), expected_output)


    # Define your test case
class TestValidateFunction(unittest.TestCase):

    def test_valid_games(self):
        games = [
            Game(id=1, rounds=[Round(blue=5, red=5, green=5)]),
            Game(id=2, rounds=[Round(blue=14, red=12, green=13)]),
            Game(id=3, rounds=[Round(blue=0, red=0, green=0)])
        ]
        self.assertEqual(validate(games), 6)  # Expected sum of IDs 1 and 2

    def test_invalid_games(self):
        games = [
            Game(id=4, rounds=[Round(blue=15, red=5, green=5)]),
            Game(id=5, rounds=[Round(blue=14, red=13, green=13)]),
            Game(id=6, rounds=[Round(blue=0, red=0, green=14)])
        ]
        self.assertEqual(validate(games), 0)  # No valid games

    def test_mixed_valid_and_invalid_games(self):
        games = [
            Game(id=7, rounds=[Round(blue=5, red=5, green=5)]),
            Game(id=8, rounds=[Round(blue=15, red=15, green=15)]),
            Game(id=9, rounds=[Round(blue=14, red=12, green=13)])
        ]
        self.assertEqual(validate(games), 16)  # Expected sum of IDs 7


class TestGameCalculations(unittest.TestCase):

    def test_calculate_power(self):
        game = Game(id=1, rounds=[Round(blue=2, red=3, green=4), Round(blue=5, red=6, green=7)])
        self.assertEqual(calculate_power(game), 7*5*6)  # max of each color

    def test_calculate_total_power_single_game(self):
        games = [Game(id=1, rounds=[Round(blue=2, red=3, green=4), Round(blue=5, red=6, green=7)])]
        self.assertEqual(calculate_total_power(games), 7*5*6)  # total power of one game

    def test_calculate_total_power_multiple_games(self):
        games = [
            Game(id=1, rounds=[Round(blue=2, red=3, green=4), Round(blue=5, red=6, green=7)]),
            Game(id=2, rounds=[Round(blue=1, red=2, green=3), Round(blue=4, red=5, green=6)])
        ]
        self.assertEqual(calculate_total_power(games), (7*5*6) + (6*4*5))  # total power of two games

if __name__ == '__main__':
    unittest.main()
