import unittest
from day5.day5 import (get_seeds, process_ranges, process_all_ranges,
                              map_to_value, calculate_location, find_smallest_location,
                              map_to_prev, find_seed, get_all_seed_ranges,
                              is_valid_seed, calculate_locations, get_lowest_location, Range)

class TestYourScript(unittest.TestCase):

    def test_get_seeds(self):
        self.assertEqual(get_seeds(["seeds: 79 14 55 13"]), [79, 14, 55, 13])
        self.assertEqual(get_seeds(["seeds: "]), [])

    def test_process_ranges(self):
        self.assertEqual(process_ranges("header\n10 20 5\n30 40 10"), [Range(10, 20, 5), Range(30, 40, 10)])
        self.assertEqual(process_ranges("header\n"), [])

    def test_process_all_ranges(self):
        sections = ["range1\n10 20 5", "range2\n30 40 10", "range3\n10 20 5", "range4\n10 20 5", "range5\n10 20 5", "range6\n10 20 5", "range7\n10 20 5"]
        result = process_all_ranges(sections)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], [Range(10, 20, 5)])
        self.assertEqual(result[1], [Range(30, 40, 10)])

    def test_map_to_value(self):
        self.assertEqual(map_to_value(22, Range(10, 20, 5)), 12)
        self.assertEqual(map_to_value(19, Range(10, 20, 5)), -1)

    def test_calculate_location(self):
        ranges = [[Range(10, 20, 5)]]
        self.assertEqual(calculate_location(22, ranges), 12)
        self.assertEqual(calculate_location(19, ranges), 19)

    def test_find_smallest_location(self):
        seeds = [22, 23, 24]
        ranges = [[Range(10, 20, 5)]]
        self.assertEqual(find_smallest_location(seeds, ranges), 12)

    def test_map_to_prev(self):
        self.assertEqual(map_to_prev(12, Range(10, 20, 5)), 22)
        self.assertEqual(map_to_prev(9, Range(10, 20, 5)), -1)

    def test_find_seed(self):
        ranges = [[Range(10, 20, 5)]]
        self.assertEqual(find_seed(12, ranges), 22)
        self.assertEqual(find_seed(19, ranges), 19)

    def test_get_all_seed_ranges(self):
        sections = ["seeds: 79 14 55 13"]
        self.assertEqual(list(get_all_seed_ranges(sections)), [(10, 5), (20, 10)])

    def test_is_valid_seed(self):
        seed_ranges = [(10, 5), (20, 10)]
        self.assertTrue(is_valid_seed(12, seed_ranges))
        self.assertFalse(is_valid_seed(30, seed_ranges))

    def test_calculate_locations(self):
        ranges = [[Range(10, 20, 5)]]
        sections = ["seeds: 79 14 55 13"]
        all_locations, seed_ranges = calculate_locations(ranges, sections)
        self.assertEqual(all_locations, range(1, 36))
        self.assertEqual(seed_ranges, [(10, 5), (20, 10)])

    def test_get_lowest_location(self):
        ranges = [[Range(10, 20, 5)]]
        sections = ["seeds: 10 5 20 10"]
        all_locations, seed_ranges = calculate_locations(ranges, sections)
        self.assertEqual(get_lowest_location(all_locations, seed_ranges), 1)

if __name__ == '__main__':
    unittest.main()
