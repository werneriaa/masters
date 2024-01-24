import os
import sys
import re


def get_input_path(filename):  # nocover
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, '..', 'inputs', filename)


def read_input(day, test=False):  # nocover
    try:
        filename = f'test_day_{day}_part1.txt' if test else f'day{day}.txt'
        file = get_input_path(filename)
        print(file)
        with open(file, 'r') as input_file:
            puzzle = input_file.read()
            return puzzle.split('\n')
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)


puzzle = read_input(4, True)  # nocover


def transform_data(puzzle):
    parsed_data = []
    for line in puzzle:
        card_info, numbers = line.split(': ')
        my_nums, right_nums = numbers.split(' | ')
        my_nums_list = my_nums.split()
        my_nums_parsed = set([int(num) for num in my_nums_list])
        right_nums_list = right_nums.split()
        right_nums_parsed = set([int(num) for num in right_nums_list])
        card_number = int(re.findall('(\d+)', card_info)[0])
        parsed_data.append((card_number, (my_nums_parsed, right_nums_parsed)))
    return parsed_data


# parsed_data = transform_data(puzzle)


def calculate_points(parsed_data):
    total_points = 0
    for line in parsed_data:
        intersection = line[1][0] & line[1][1]
        if len(intersection) > 0:
            points = 2 ** (len(intersection) - 1)
            total_points += points
    return total_points


def process_cards(parsed_data):
    counts = {card_id: 1 for card_id, _ in parsed_data}
    for card_id, (winning, our) in parsed_data:
        numbers_that_won = winning & our
        winning_count = len(numbers_that_won)

        for _ in range(counts[card_id]):
            for i in range(card_id + 1, card_id + winning_count + 1):
                counts[i] += 1
    total = sum(c for c in counts.values())
    return total


# part_2 = process_cards(parsed_data) #nocover
# print(f'Solution: {part_2}') #nocover
