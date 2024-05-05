# import unittest
# from src.max_achievable_number import max_achievable_number


# class TestMaxAchievableNumber(unittest.TestCase):
#     # TN
#     def test_example_1(self):
#         self.assertEqual(
#             max_achievable_number(4, 1),
#             6,
#             "The maximum achievable number with num=4 and t=1 should be 6.",
#         )

#     # TN
#     def test_example_2(self):
#         self.assertEqual(
#             max_achievable_number(3, 2),
#             7,
#             "The maximum achievable number with num=3 and t=2 should be 7.",
#         )

#     # FP
#     def test_num_equals_t(self):
#         self.assertEqual(
#             max_achievable_number(5, 5),
#             10,
#             "The maximum achievable number with num=5 and t=5 should be 10.",
#         )

#     # FP
#     def test_num_greater_than_t(self):
#         self.assertEqual(
#             max_achievable_number(10, 2),
#             12,
#             "The maximum achievable number with num=10 and t=2 should be 12.",
#         )

#     # FP
#     def test_t_greater_than_num(self):
#         self.assertEqual(
#             max_achievable_number(2, 10),
#             12,
#             "The maximum achievable number with num=2 and t=10 should be 12.",
#         )

#     # FP
#     def test_min_constraints(self):
#         self.assertEqual(
#             max_achievable_number(1, 1),
#             2,
#             "The maximum achievable number with the minimum constraints (num=1, t=1) should be 2.",
#         )

#     # FP
#     def test_max_constraints(self):
#         self.assertEqual(
#             max_achievable_number(50, 50),
#             100,
#             "The maximum achievable number with the maximum constraints (num=50, t=50) should be 100.",
#         )


# if __name__ == "__main__":
#     unittest.main()
