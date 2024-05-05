import unittest
from day5.day5 import part_1, part_2


class TestAlmanacMappingSystem(unittest.TestCase):
    def setUp(self):
        self.input_data = (
            "seeds: 79 14 55 13\n"
            "\n"
            "seed-to-soil map:\n"
            "50 98 2\n"
            "52 50 48\n"
            "\n"
            "soil-to-fertilizer map:\n"
            "0 15 37\n"
            "37 52 2\n"
            "39 0 15\n"
            "\n"
            "fertilizer-to-water map:\n"
            "49 53 8\n"
            "0 11 42\n"
            "42 0 7\n"
            "57 7 4\n"
            "\n"
            "water-to-light map:\n"
            "88 18 7\n"
            "18 25 70\n"
            "\n"
            "light-to-temperature map:\n"
            "45 77 23\n"
            "81 45 19\n"
            "68 64 13\n"
            "\n"
            "temperature-to-humidity map:\n"
            "0 69 1\n"
            "1 0 69\n"
            "\n"
            "humidity-to-location map:\n"
            "60 56 37\n"
            "56 93 4"
        )

    def test_lowest_location_number(self):
        # Given the input data, test that the lowest location number is correctly identified
        result = part_1(self.input_data)
        self.assertEqual(result, 35, "The lowest location number should be 35")

    def test_lowest_location_number_with_ranges(self):
        # Given the input data with seed ranges, test that the lowest location number is correctly identified as 46
        result = part_2(self.input_data)
        self.assertEqual(result, 46, "The lowest location number should be 46")


if __name__ == "__main__":
    unittest.main()
