**DATE**: 24.03.2024

## Prompts

1.  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
2.  Example 1: Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. Example 2: Input: nums = [3,2,4], target = 6 Output: [1,2] Example 3: Input: nums = [3,3], target = 6 Output: [0,1]

3.  Constraints: 2 <= nums.length <= 104 -109 <= nums[i] <= 109 -109 <= target <= 109 Only one valid answer exists.

## Answers

1.  For creating unit tests for this function, which I'll refer to as `find_two_sum`, it would be helpful to understand a bit more about the expected behavior in certain edge cases. However, based on your initial description, the primary focus is on verifying that the function correctly identifies the indices of two numbers that add up to a specified target.

    Let's start by identifying some test scenarios:

    1.  A straightforward case where the solution is obvious.
    2.  A case where the two numbers that sum to the target are not adjacent.
    3.  A case involving negative numbers in the array.
    4.  A case where the array contains zero, which is part of the solution.
    5.  A case where the same number could be used twice, but the requirement specifies not to.

    Could you provide specific example cases and constraints, such as the size of the input array or the range of numbers it might contain?

2.  Great, these examples help clarify how the function should work in different scenarios. Based on these, we can design specific tests that cover a range of situations, including the presence of negative numbers, handling duplicates, and ensuring the function does not reuse elements.

    Before we proceed to writing the tests, do you have any specific constraints or limitations regarding the input array's size, the range of integer values, or performance considerations? For instance, should the function still perform efficiently with very large arrays?

3.  Given the provided examples and constraints, I'll create a series of unit tests for the `find_two_sum` function. These tests will check for correctness in various scenarios, ensuring the function behaves as expected under different conditions, including handling large arrays and working with a wide range of integer values.

    Here's the test code that covers the scenarios we've discussed:

    ```python
    import unittest
    from solution import find_two_sum

    class TestFindTwoSum(unittest.TestCase):

        def test_simple_case(self):
            self.assertEqual(sorted(find_two_sum([2, 7, 11, 15], 9)), [0, 1], "Should return indices [0, 1] for target 9")

        def test_non_adjacent_elements(self):
            self.assertEqual(sorted(find_two_sum([3, 2, 4], 6)), [1, 2], "Should return indices [1, 2] for target 6")

        def test_duplicate_elements(self):
            self.assertEqual(sorted(find_two_sum([3, 3], 6)), [0, 1], "Should return indices [0, 1] for duplicate elements adding to target 6")

        def test_large_range_of_numbers(self):
            nums = list(range(-5000, 5000))
            target = nums[4999] + nums[4998]
            self.assertEqual(sorted(find_two_sum(nums, target)), [4998, 4999], "Should handle a large range of numbers efficiently")

        def test_with_negative_numbers(self):
            self.assertEqual(sorted(find_two_sum([-1, -2, -3, -4, -5], -8)), [2, 4], "Should correctly find indices when array contains negative numbers")

    if __name__ == '__main__':
        unittest.main()
    ```

    This suite covers the basic functionality, handling of negative numbers, non-adjacent solution elements, duplicate numbers leading to a valid solution, and a stress test with a large array to ensure performance isn't severely impacted.

    Note: The test case `test_large_range_of_numbers` assumes an implementation capable of handling the entire specified range of inputs efficiently, which should align with the constraint of the array length up to 10^4.

    Please, make sure the `find_two_sum` function is implemented in a `solution.py` file for this test suite to work. If you need any adjustments or additional tests, feel free to let me know!
