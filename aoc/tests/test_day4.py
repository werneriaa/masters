import unittest
from day4.day4 import transform_data, calculate_points, process_cards

class TestDayFour(unittest.TestCase):
    def test_transform_data(self):
      input_data = [
          "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
          "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
          "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
          "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
          "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
          "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
      ]

      expected_output = [
          (1, ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})),
          (2, ({13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19})),
          (3, ({1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1})),
          (4, ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83})),
          (5, ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36})),
          (6, ({31, 18, 13, 56, 72}, {74, 77, 10, 23, 35, 67, 36, 11}))
      ]

      result = transform_data(input_data)
      self.assertEqual(result, expected_output)


    def test_calculate_points(self):
      input_data = [
          (1, ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})),
          (2, ({13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19})),
          (3, ({1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1})),
          (4, ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83})),
          (5, ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36})),
          (6, ({31, 18, 13, 56, 72}, {74, 77, 10, 23, 35, 67, 36, 11}))
      ]
       
      expected_output = 13
      result = calculate_points(input_data)
      self.assertEqual(result, expected_output)


    def test_process_cards(self):
      input_data = [
          (1, ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})),
          (2, ({13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19})),
          (3, ({1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1})),
          (4, ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83})),
          (5, ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36})),
          (6, ({31, 18, 13, 56, 72}, {74, 77, 10, 23, 35, 67, 36, 11}))
      ]
       
      expected_output = 30
      result = process_cards(input_data)
      self.assertEqual(result, expected_output)
    
if __name__ == '__main__':
    unittest.main()
