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


def sum_calibration_values(lines):
    result = 0
    for line in lines:
        nums = re.findall(r'(\d)', line)
        if len(nums) > 0:
            res = int(f"{(nums[0])}{(nums[-1])}")
            result += res

    return result


# def part1(file: str) -> int:  # nocover
#     with open(file, 'r') as file:
#         lines = file.readlines()
#         result = sum_calibration_values(lines)
#         return result


def sum_calibration_values_part2(lines):
    result = 0
    for line in lines:
        nums = re.findall(
            r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line
        )
        res = int(f"{convert_to_int(nums[0])}{convert_to_int(nums[-1])}")
        result += res

    return result


# def sum_calibration_values_part2_broken(lines):  # nocover
#     result = 0
#     for line in lines:
#         try:
#             nums = re.findall(r'(?=(\d|one|two|three|four|six|seven|eight|nine))', line)
#             if len(nums) < 0:
#                 continue
#             res = int(f"{convert_to_int(nums[0])}{convert_to_int(nums[-1])}")
#             result += res
#         except IndexError:
#             continue

#     return result


# def part2(file: str) -> int:  # nocover
#     with open(file, 'r') as file:
#         lines = file.readlines()
#         result = sum_calibration_values_part2(lines)
#         return result


def get_input_path(filename):  # nocover
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, '..', 'inputs', filename)


# print(part1(get_input_path("test_part1_2.txt")))
# print(part2(get_input_path("day1.txt")))
