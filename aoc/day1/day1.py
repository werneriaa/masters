import re
import os


def convert_to_int(val):
    str_to_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    try:
        return int(val)
    except ValueError:
        return str_to_num[val]


def part1(file: str) -> int:
    with open(file, 'r') as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            nums = re.findall(r'(\d)', line)
            res = int(f"{(nums[0])}{(nums[-1])}")
            result += res

        return result


def part2(file: str) -> int:
    with open(file, 'r') as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            nums = re.findall(
                r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line
            )
            res = int(f"{convert_to_int(nums[0])}{convert_to_int(nums[-1])}")
            result += res

        return result


def get_input_path(filename):  # nocover
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, '..', 'inputs', filename)


# print(part1(get_input_path("day1.txt")))
# print(part2(get_input_path("day1.txt")))
