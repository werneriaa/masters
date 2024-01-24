import re
import sys
import os

def get_input_path(filename): # nocover
  current_dir = os.path.dirname(__file__)
  return os.path.join(current_dir, '..', 'inputs', filename)

def read_input(day, test=False): # nocover
  try:
    filename = f'test_day_{day}_part1.txt' if test else f'day{day}.txt'
    file = get_input_path(filename)
    print(file)
    with open(file, 'r') as input_file:
      input_raw = input_file.read()
      return input_raw.split('\n')
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)


# times_raw, distances_raw = read_input(6, False)

def get_int_times_and_distances(times_raw, distances_raw):
  times = map(int, re.findall('\d+', times_raw))
  distances = map(int, re.findall('\d+', distances_raw))
  return zip(times, distances)

# times_and_distances = get_int_times_and_distances(times_raw, distances_raw)

def calculate_wins(times_and_distances):
  total = 1
  for time, distance in times_and_distances:
    wins = 0
    for speed in range(1, time):
      travelled_distance = (time - speed) * speed
      if travelled_distance > distance:
        wins += 1
      elif wins:
        break
    total *= wins
  return total
    

# total = calculate_wins(times_and_distances)

def get_full_times_and_distances(times_raw, distances_raw):
  time = int(''.join(re.findall('\d+', times_raw)))
  distance = int(''.join(re.findall('\d+', distances_raw)))
  return time, distance

# time, distance = get_full_times_and_distances(times_raw, distances_raw)


def calculate_wins_part2(time, distance):
  wins = 0
  for speed in range(1, distance):
    final_distance = (time - speed) * speed
    if (final_distance > distance):
      wins += 1
    elif wins:
      break
  return wins

# total_part2 = calculate_wins_part2(time, distance)
# print(total_part2)