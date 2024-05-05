import re
import sys
import os
from operator import mul


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


# engine = read_input(3, True)


def part1(engine):
    symbol_regex = r'[^.\d]'
    symbol_adjacent = set()
    for row, line in enumerate(engine):
        for m in re.finditer(symbol_regex, line):
            col = m.start()
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    symbol_adjacent.add((r, c))

    number_regex = r'\d+'

    # Sum of numbers adjacent to symbols
    part_num_sum = 0
    for row, line in enumerate(engine):
        for num_match in re.finditer(number_regex, line):
            # Check if the number is adjacent to any symbol
            number_range = range(*num_match.span())
            is_adjacent = False
            for col in number_range:
                if (row, col) in symbol_adjacent:
                    is_adjacent = True
                    break

            if is_adjacent:
                part_num_sum += int(num_match.group())

    return part_num_sum


def part2(engine):
    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(engine):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(engine):
        for m in re.finditer(number_regex, line):
            for r in range(i - 1, i + 2):
                for c in range(m.start() - 1, m.end() + 1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)

    return gear_ratio_sum


# print('Part 1:', part1(engine))
# print('Part 2:', part2(engine))
