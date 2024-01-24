import unittest
from day6.day6 import (
    get_int_times_and_distances,
    calculate_wins,
    get_full_times_and_distances,
    calculate_wins_part2,
)


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.times_raw = "Time: 7 15 30"
        self.distances_raw = "Distance: 9 40 200"

    def test_get_int_times_and_distances(self):
        expected = [(7, 9), (15, 40), (30, 200)]
        result = list(get_int_times_and_distances(self.times_raw, self.distances_raw))
        self.assertEqual(result, expected)

    def test_calculate_wins(self):
        times_and_distances = [(7, 9), (15, 40), (30, 200)]
        expected_total = 288
        result = calculate_wins(times_and_distances)
        self.assertEqual(result, expected_total)

    def test_get_full_times_and_distances(self):
        expected_time, expected_distance = 71530, 940200
        result_time, result_distance = get_full_times_and_distances(
            self.times_raw, self.distances_raw
        )
        self.assertEqual(result_time, expected_time)
        self.assertEqual(result_distance, expected_distance)

    def test_calculate_wins_part2(self):
        time, distance = 71530, 940200
        expected_wins = 71503
        result = calculate_wins_part2(time, distance)
        self.assertEqual(result, expected_wins)


if __name__ == '__main__':
    unittest.main()
