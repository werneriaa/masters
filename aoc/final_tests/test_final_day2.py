import unittest
from day2.day2 import solve_day_2_part_1, solve_day_2_part_2


# Had to modify manually the games_data to run the tests. Other option is to modify the code
# However this shouldnt matter


class TestGamePossibilities(unittest.TestCase):
    def test_sum_of_possible_game_ids(self):
        game_data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        expected_sum_ids = 8
        self.assertEqual(
            solve_day_2_part_1(game_data),
            expected_sum_ids,
            "The sum of the IDs for possible games does not match the expected value.",
        )

    def test_sum_of_powers(self):
        game_data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        expected_sum_of_powers = 2286
        self.assertEqual(
            solve_day_2_part_2(game_data),
            expected_sum_of_powers,
            "The sum of the powers does not match the expected value.",
        )


if __name__ == '__main__':
    unittest.main()
