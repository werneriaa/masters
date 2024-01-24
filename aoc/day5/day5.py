import re
import sys
import os
from collections import namedtuple

Range = namedtuple('Range', ['dest_start', 'source_start', 'range'])

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
      return input_raw.split('\n\n')
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)

data_sections = read_input(5, True)
    
def get_seeds(data_sections):
  return [int(seed) for seed in re.findall(r'\d+', data_sections[0].split(': ')[1])]

def process_ranges(section):
  lines = section.split('\n')[1:]
  ranges = []
  for line in lines:
      numbers = [int(value) for value in re.findall(r'\d+', line)]
      ranges.append(Range(*numbers))
  return ranges
        
def process_all_ranges(data_sections):
  seed_to_soil = process_ranges(data_sections[1])
  soil_to_fertilizer = process_ranges(data_sections[2])
  fertilizer_to_water = process_ranges(data_sections[3])
  water_to_light = process_ranges(data_sections[4])
  light_to_temperature = process_ranges(data_sections[5])
  temperature_to_humidity = process_ranges(data_sections[6])
  humidity_to_location = process_ranges(data_sections[7])

  ranges = [
      seed_to_soil,
      soil_to_fertilizer,
      fertilizer_to_water,
      water_to_light,
      light_to_temperature,
      temperature_to_humidity,
      humidity_to_location
  ]

  return ranges


def map_to_value(source, r):
  if source >= r.source_start and source <= r.source_start + r.range:
    n = source - r.source_start
    return r.dest_start + n
  else:
    return -1

def calculate_location(seed, ranges):
  source = seed
  for _range in ranges:
    for individual_range in _range:
      potential = map_to_value(source, individual_range)
      if potential != -1:
        source = potential
        break
      else:
        continue
  return source


def find_smallest_location(seeds, ranges):
    smallest = None
    for seed in seeds:
        location = calculate_location(seed, ranges)
        if not smallest or location < smallest:
            smallest = location
    return smallest

# seeds = get_seeds(data_sections)
# ranges = process_all_ranges(data_sections)


# smallest = find_smallest_location(seeds, ranges)

# print(smallest)


def map_to_prev(dest, r):
  low = r.dest_start
  high = r.dest_start + r.range - 1
  # Any source numbers that aren't mapped
  # correspond to the same destination number.
  if dest < low or dest > high:
    return -1
  else:
    return dest - r.dest_start + r.source_start
    

def find_seed(location, ranges):
  src = location
  for _range in ranges:
    for individual_range in _range:
      potential = map_to_prev(src, individual_range)
      if potential != -1:
        src = potential
        break
  return src

def get_all_seed_ranges(data_sections):
  seed_range_input = [int(seed) for seed in re.findall(r'\d+', data_sections[0].split(': ')[1])]
  return zip(seed_range_input[::2], seed_range_input[1::2])

def is_valid_seed(seed, seed_ranges):
  for seed_range in seed_ranges:
    if seed_range[0] < seed < seed_range[0] + seed_range[1]:
      return True
  return False



def calculate_locations(ranges, data_sections):
  location_ranges = ranges[-1]
  highest_location_range = max(location_ranges, key=lambda range: range.dest_start)
  max_location = highest_location_range.dest_start + highest_location_range.range
  all_locations = range(1, max_location + 1)

  seed_ranges = list(get_all_seed_ranges(data_sections))

  return all_locations, seed_ranges

def get_lowest_location(all_locations, seed_ranges):
  print(len(all_locations))
  for location in all_locations:
    seed = find_seed(location, ranges[-1::-1])
    print(seed)
    if is_valid_seed(seed, seed_ranges):
      print(f'Found {seed=} at {location=}')
      return location
    

# all_locations, seed_ranges = calculate_locations(ranges, data_sections)

# lowest_location = get_lowest_location(all_locations, seed_ranges)

# print(lowest_location)