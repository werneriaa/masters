import re
from collections import namedtuple
import sys
import os

def get_input_path(filename): # nocover
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, '..', 'inputs', filename)

def read_input(day, transformer=str, test=False): # nocover
    try:
        filename = f'test_day_{day}_part1.txt' if test else f'day{day}.txt'
        file = get_input_path(filename)
        print(file)
        with open(file, 'r') as input_file:
            return [transformer(line) for line in input_file]
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)



PATTERN = r'((\d+) (blue|red|green))+'

Game = namedtuple('Game', ['id', 'rounds'])
Round = namedtuple('Round', ['blue', 'red', 'green'])

def parse_game_input(line):
    game_input, rounds_input = line.split(': ')
    game_id = game_input.strip().split(' ')[1]
    rounds = [round.strip() for round in rounds_input.split(';')]
    rounds_in_game = []

    for round in rounds:
        current_round = Round(blue=0, red=0, green=0)
        for matches in re.findall(PATTERN, round):
            _, count, color = matches
            update = { color: int(count) }
            current_round = current_round._replace(**update)

            rounds_in_game.append(current_round)
    game = Game(id=int(game_id), rounds=rounds_in_game)
    return game

# games = read_input(2, parse_game_input)


def validate(games):
    MAX_RED_AMOUNT = 12
    MAX_GREEN_AMOUNT = 13
    MAX_BLUE_AMOUNT = 14
    valid_games = []
    for game in games:
        for round in game.rounds:
            if round.blue > MAX_BLUE_AMOUNT or round.red > MAX_RED_AMOUNT or round.green > MAX_GREEN_AMOUNT:
                break
        else:
            valid_games.append(game)
    return sum(game.id for game in valid_games)

# part_1 = validate(games)
# print(f'Solution: {part_1}')


def calculate_power(game):
    min_green = max(round.green for round in game.rounds)
    min_blue = max(round.blue for round in game.rounds)
    min_red = max(round.red for round in game.rounds)
    return min_green * min_blue * min_red

def calculate_total_power(games):
    return sum(calculate_power(game) for game in games)

# part_2 = calculate_total_power(games)

# print(f'Solution: {part_2}')