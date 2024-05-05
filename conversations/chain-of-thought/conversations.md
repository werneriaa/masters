## Sum of Numbers With Units Digit K

**DATE**
12.3.2024

**Grade**
Medium

**Prompts**

1.  Given two integers `num` and `k`, consider a set of positive integers with the following properties:

    - The units digit of each integer is `k`.
    - The sum of the integers is `num`.

    Return *the **minimum** possible size of such a set, or* `-1` *if no such set exists.*

    Note:

    - The set can contain multiple instances of the same integer, and the sum of an empty set is considered `0`.
    - The **units digit** of a number is the rightmost digit of the number.

2.  . **Example 1:**

    **Input:** num = 58, k = 9
    **Output:** 2
    **Explanation:**
    One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
    Another valid set is [19,39].
    It can be shown that 2 is the minimum possible size of a valid set.

    **Example 2:**

    **Input:** num = 37, k = 2
    **Output:** -1
    **Explanation:** It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.

    **Example 3:**

    **Input:** num = 0, k = 7
    **Output:** 0
    **Explanation:** The sum of an empty set is considered 0.

3.  **Constraints:**

    - `0 <= num <= 3000`
    - `0 <= k <= 9`

**Answer**

1.  To clarify the requirements for generating unit tests, I'd like to ask a few questions:

    1.  Is there a specific range for the values of `num` and `k`?
    2.  Are `num` and `k` always integers, and can `num` be negative or zero?
    3.  How should the function handle edge cases, such as `k` being greater than 9 or less than 0, since the units digit can only be in the range of 0 to 9?
    4.  Could you provide a couple of example inputs and the expected outputs for this function?

    These details will help ensure that the unit tests are comprehensive and cover a variety of scenarios.

2.  Thank you for the examples. Based on the provided information, I'll structure unit tests for a function that meets the following criteria:

3.  The function takes two integer parameters, `num` and `k`.
4.  It returns the minimum possible size of a set of positive integers where each integer's units digit is `k`, and the sum of the integers is `num`.
5.  If no such set exists, the function returns -1.
6.  Special cases include:
    - `num` being zero, where the minimum set size is naturally 0 because the sum of an empty set is considered 0.
    - Situations where it is impossible to achieve the sum `num` with integers having `k` as their units digit.


    Before proceeding to generate the whole test code, are there any constraints or additional details about how `num` and `k` should be treated beyond those provided in the examples?

3.  Given the requirements and constraints, I'll generate unit tests for a function that we'll refer to as `min_set_size(num, k)`. These tests will cover a range of scenarios, including valid inputs where a set exists, cases where no such set can be formed, and edge cases as defined by the constraints.

    The function signature will be assumed as follows for the purpose of these tests:

    ```python
    def min_set_size(num: int, k: int) -> int:
        pass
    ```

    Here are the unit tests:

    ```python
    import unittest
    from placeholder import min_set_size  # Replace 'placeholder' with the actual module name

    class TestMinSetSize(unittest.TestCase):

        def test_valid_set_exists_small_set(self):
            self.assertEqual(min_set_size(58, 9), 2, "Minimum set size with num=58 and k=9 should be 2")

        def test_no_valid_set_exists(self):
            self.assertEqual(min_set_size(37, 2), -1, "It should return -1 when no valid set can be formed")

        def test_sum_zero_empty_set(self):
            self.assertEqual(min_set_size(0, 7), 0, "Minimum set size with num=0 should be 0 for any k")

        def test_valid_set_exists_larger_sum(self):
            self.assertEqual(min_set_size(3000, 1), 1, "Minimum set size with num=3000 and k=1 should be 1")

        def test_valid_set_exists_edge_k(self):
            self.assertEqual(min_set_size(90, 0), 1, "Minimum set size with num=90 and k=0 should be 1")

        def test_valid_set_exists_with_minimum_possible_numbers(self):
            self.assertEqual(min_set_size(19, 9), 1, "Minimum set size with num=19 and k=9 should be 1")

        def test_upper_bound_num(self):
            self.assertGreaterEqual(min_set_size(3000, 9), 1, "Function should handle upper boundary of num=3000 correctly")

    if __name__ == '__main__':
        unittest.main()
    ```

````
	These tests cover:
	- Valid sets with the minimum and larger sums.
	- Cases where no valid set can be formed.
	- The special case of `num` being zero.
	- Edge cases based on the constraints provided.

	Make sure to replace `'placeholder'` with the actual module name where the `min_set_size` function is defined. This setup assumes a simple test environment using Python's built-in `unittest` framework.

**Result**

TP = 0
FP = 1
TN = 6
FN = 0


## Find max achievable number

**DATE**
12.3.2024

**Grade**
Easy

**Prompt**
1.
	   You are given two integers, `num` and `t`.

	An integer `x` is called **achievable** if it can become equal to `num` after applying the following operation no more than `t` times:

	- Increase or decrease `x` by `1`, and simultaneously increase or decrease `num` by `1`.

	Return _the maximum possible achievable number_. It can be proven that there exists at least one achievable number.


2.
	**Example 1:**

	**Input:** num = 4, t = 1
	**Output:** 6
	**Explanation:** The maximum achievable number is x = 6; it can become equal to num after performing this operation:
	1- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5.
	It can be proven that there is no achievable number larger than 6.

	**Example 2:**

	**Input:** num = 3, t = 2
	**Output:** 7
	**Explanation:** The maximum achievable number is x = 7; after performing these operations, x will equal num:
	1- Decrease x by 1, and increase num by 1. Now, x = 6 and num = 4.
	2- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5.
	It can be proven that there is no achievable number larger than 7.

3.
	   **Constraints:**

	- `1 <= num, t <= 50`
**Answer**
1.
	To create the unit tests for this requirement, I need a bit more information. Could you provide example cases, including inputs and expected outputs? This will help in creating more precise tests.
2.
	Great, thanks for the examples. Do you have any specific constraints for the inputs, such as the ranges for `num` and `t`, or any special cases I should be aware of while writing the tests?

3.

	Based on the description, examples, and constraints provided, I will create a Python test file with appropriate test cases for the function that calculates the maximum achievable number. The function seems to involve a calculation where both `num` and `t` are modified simultaneously under specific conditions, aiming to maximize a value.

	Let's assume the function we are testing is called `max_achievable_number(num, t)`.

	Here's a Python test file that includes tests for the provided examples and additional edge cases considering the constraints:

	```python
	import unittest
	from placeholder import max_achievable_number

	class TestMaxAchievableNumber(unittest.TestCase):

	    def test_max_achievable_with_small_gap(self):
	        self.assertEqual(max_achievable_number(4, 1), 6, "Should return 6 for num=4, t=1")

	    def test_max_achievable_with_larger_gap(self):
	        self.assertEqual(max_achievable_number(3, 2), 7, "Should return 7 for num=3, t=2")

	    def test_max_achievable_with_min_values(self):
	        self.assertEqual(max_achievable_number(1, 1), 3, "Should return 3 for num=1, t=1")

	    def test_max_achievable_with_max_values(self):
	        self.assertEqual(max_achievable_number(50, 50), 150, "Should return 150 for num=50, t=50")

	    def test_max_achievable_with_no_change(self):
	        self.assertEqual(max_achievable_number(10, 0), 10, "Should return 10 for num=10, t=0")

	if __name__ == '__main__':
	    unittest.main()
	```

	I've included tests for the scenarios you provided and added a few to cover the range of input values, including the minimum and maximum values based on the constraints. The assumption is that the `max_achievable_number` function will be defined in a file named `placeholder.py`, which you would replace with the actual file name containing the function implementation.

	Please let me know if there's anything else you'd like to adjust or add!

**Result**

TP = 0
FP = 0
TN = 5
FN = 0
##  Median of Two Sorted Arrays

**DATE**
13.3.2024

**Grade**
Hard

**Prompt**
1.
	   Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
2.
	   **Example 1:**
	**Input:** nums1 = [1,3], nums2 = [2]
	**Output:** 2.00000
	**Explanation:** merged array = [1,2,3] and median is 2.

	**Example 2:**

	**Input:** nums1 = [1,2], nums2 = [3,4]
	**Output:** 2.50000
	**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
3.
	   **Constraints:**

	- `nums1.length == m`
	- `nums2.length == n`
	- `0 <= m <= 1000`
	- `0 <= n <= 1000`
	- `1 <= m + n <= 2000`
	- `-106 <= nums1[i], nums2[i] <= 106`


**Answer**
1.
	   For creating appropriate tests for the given requirement, we'll need to design scenarios that cover various cases including edge cases. Here are some initial thoughts on tests that we could create:

	1. Test with two non-empty arrays where one array is longer than the other.
	2. Test with one non-empty array and one empty array.
	3. Test with two arrays of equal length.
	4. Test where the median is in the middle of one of the arrays.
	5. Test with arrays having all equal elements.
	6. Test with negative numbers in the arrays.
	7. Edge case with the smallest possible arrays (each containing one element).

	For each of these scenarios, could you provide example inputs and the expected output? This will help in creating accurate and comprehensive test cases.
2.
	   Given the examples, we can now outline specific test cases based on them and the initial scenarios proposed:

	1. **Test with one array longer than the other**: We can use `nums1 = [1, 3]` and `nums2 = [2]` as an example, expecting the output to be `2.00000`.
	2. **Test with one non-empty array and one empty array**: This wasn't directly provided, but we can infer an example like `nums1 = []` and `nums2 = [1]`, expecting the output to be `1.00000`.
	3. **Test with two arrays of equal length**: Using `nums1 = [1, 2]` and `nums2 = [3, 4]` as an example, expecting the output to be `2.50000`.
	4. **Test where the median is in the middle of one of the arrays**: The provided examples don't explicitly cover this scenario distinctly, but example 1 implicitly tests this.
	5. **Test with arrays having all equal elements**: An example could be `nums1 = [2, 2]` and `nums2 = [2, 2]`, expecting the output to be `2.00000`.
	6. **Test with negative numbers in the arrays**: We can create a test case like `nums1 = [-5, -3]` and `nums2 = [-2, -1]`, expecting the output to be `-2.50000`.
	7. **Edge case with the smallest possible arrays**: Using `nums1 = [1]` and `nums2 = [2]`, expecting the output to be `1.50000`.

	Before moving on to generating the whole test code, do you have any specific constraints or additional scenarios in mind that you'd like to include?

3.
	   With the constraints in mind, we can proceed to generate the whole test code for the scenarios discussed. These constraints don't introduce new test cases directly but emphasize the importance of including tests with empty arrays, tests with the arrays at their maximum lengths, and tests covering the full range of possible element values, including the extremes of `-10^6` and `10^6`. Given the structure and requirements you've provided, here's how the test code might look:

	```python
	import unittest
	from solution import findMedianSortedArrays  # Assuming the function is named findMedianSortedArrays in solution.py

	class TestFindMedianSortedArrays(unittest.TestCase):

	    def test_with_one_array_longer_than_other(self):
	        self.assertAlmostEqual(findMedianSortedArrays([1, 3], [2]), 2.00000)

	    def test_with_one_empty_array(self):
	        self.assertAlmostEqual(findMedianSortedArrays([], [1]), 1.00000)

	    def test_with_two_arrays_of_equal_length(self):
	        self.assertAlmostEqual(findMedianSortedArrays([1, 2], [3, 4]), 2.50000)

	    def test_with_arrays_having_all_equal_elements(self):
	        self.assertAlmostEqual(findMedianSortedArrays([2, 2], [2, 2]), 2.00000)

	    def test_with_negative_numbers(self):
	        self.assertAlmostEqual(findMedianSortedArrays([-5, -3], [-2, -1]), -2.50000)

	    def test_edge_case_with_smallest_possible_arrays(self):
	        self.assertAlmostEqual(findMedianSortedArrays([1], [2]), 1.50000)

	    def test_with_large_range_values(self):
	        self.assertAlmostEqual(findMedianSortedArrays([-1000000, 1000000], [-1000000, 1000000]), 0.00000)

	    def test_maximum_length_arrays(self):
	        # This test checks the function with arrays at their maximum allowed sizes.
	        # It's more for performance and ensuring the function can handle large inputs within constraints.
	        # Given the nature of this test, specifics of the arrays are not as important as their sizes and the function's ability to handle them.
	        nums1 = list(range(500))  # Example large array, specifics can vary
	        nums2 = list(range(500, 1000))  # Another example large array
	        # The expected result and exact inputs would depend on the contents of the arrays
	        # This is just a placeholder to illustrate handling large inputs
	        self.assertTrue(isinstance(findMedianSortedArrays(nums1, nums2), float))  # Check if output is a float as expected

	if __name__ == '__main__':
	    unittest.main()
	```

	This code assumes that your median-finding function is called `findMedianSortedArrays` and is located in a file named `solution.py`. The tests include checking for correct handling of various array lengths and contents, including edge cases and performance with large arrays, as outlined by the constraints and examples provided.

	If you need adjustments or have any other specific requirements for these tests, feel free to let me know!


**Result**

TP = 0
FP = 0
TN =8
FN = 0

## AoC Day 1

**DATE**
13.3.2024

**Grade**
Hard

**Prompt**
1.
	Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

	You've been doing this long enough to know that to restore snow operations, you need to check all _fifty stars_ by December 25th.

	Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants _one star_. Good luck!

	You try to ask why they can't just use a [weather machine](https://adventofcode.com/2015/day/1) ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a [trebuchet](https://en.wikipedia.org/wiki/Trebuchet) ("please hold still, we need to strap you in").

	As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been _amended_ by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

	The newly-improved calibration document consists of lines of text; each line originally contained a specific _calibration value_ that the Elves now need to recover. On each line, the calibration value can be found by combining the _first digit_ and the _last digit_ (in that order) to form a single _two-digit number_.

2.
	   For example: 1abc2 pqr3stu8vwx a1b2c3d4e5f treb7uchet In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.


3.
	  all the inputs are lists always, if in the string there is only one digit represented like in "treb7uchet" the result should be twice the number, so in this case "77". All of the strings has atleast one digit.


**Answer**
1.
		With the provided examples and the requirement to recognize spelled-out numbers, we'll revise the unit tests for the `extract_calibration_values` function to ensure it correctly interprets both numerical digits and numbers spelled out as words. This function now needs to parse and convert spelled-out numbers (one through nine) in addition to identifying numeric digits.

Here's how we can update and extend the unit tests to cover these new requirements:

```python
import unittest
from your_module import extract_calibration_values  # Adjust the module name as needed

class TestExtractCalibrationValuesWithWords(unittest.TestCase):

    def test_with_spelled_out_numbers(self):
        """Test function with numbers spelled out in words."""
        self.assertEqual(extract_calibration_values(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']), 281)

    def test_mixed_numerals_and_words(self):
        """Test strings containing both numerals and spelled-out numbers."""
        self.assertEqual(extract_calibration_values(['1one1', 'tw2two']), 11 + 22)

    def test_spelled_out_numbers_at_start_and_end(self):
        """Ensure correct processing with spelled-out numbers at start and end of strings."""
        self.assertEqual(extract_calibration_values(['onetwo3fourfive', 'six7eight']), 15 + 68)

    def test_handling_uppercase_and_mixed_case_words(self):
        """Test handling of uppercase and mixed-case spelled-out numbers."""
        self.assertEqual(extract_calibration_values(['THREE3seven', 'fOuR4six']), 37 + 46)

    def test_large_input_with_spelled_out_numbers(self):
        """Test function performance with a large input set including spelled-out numbers."""
        large_input = ['one2three'] * 1000  # Repeat 'one2three' 1000 times
        self.assertEqual(extract_calibration_values(large_input), 13 * 1000)

    def test_with_special_characters_and_spelled_out_numbers(self):
        """Test strings with special characters and spelled-out numbers."""
        self.assertEqual(extract_calibration_values(['!one@#2$', '%three^&*four(']), 12 + 34)

if __name__ == '__main__':
    unittest.main()
````

These tests are designed to ensure that `extract_calibration_values` functionally meets the new requirement to recognize and process spelled-out numbers from "one" to "nine" as valid digits, in addition to handling numeric digits. It includes tests for handling mixed-case and special characters, which are critical given the updated problem statement.

Adjustments might be needed based on the exact implementation details of your function, especially concerning how it identifies and converts spelled-out numbers to their numeric equivalents. Additionally, ensure that your function is case-insensitive when interpreting spelled-out numbers to accommodate variations in input.

**Result**

TP = 0
FP = 0
TN = 6
FN = 0

**Part2**

Continue from part 1

**Prompt**

## --- Part Two ---

**Prompt**

1.  Part 2: Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits". Ill provide some examples, after this. If you want answers please ask.
2.  Equipped with this new information, you now need to find the real first and last digit on each line. For example: two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

**Answer**

1.  Given the new information that digits can also be spelled out in the strings, we'll need to update our approach for the `extract_calibration_values` function and consequently the unit tests. This function now needs to identify both numerical digits and words that represent numbers (from "one" to "nine") as valid digits. Let's plan for additional tests to account for this complexity:

    1.  **Test with spelled-out numbers**: Verify that the function correctly identifies and processes numbers spelled out in words.
    2.  **Test mixed numerals and words**: Check if the function can handle strings that contain both numeric digits and numbers spelled out in words.
    3.  **Test with spelled-out numbers at start and end**: Ensure it processes strings correctly when numbers are spelled at the beginning and the end.
    4.  **Test for handling uppercase and mixed-case words**: Since input could vary in case, verify that the function correctly identifies spelled-out numbers regardless of case.

    Could you provide the examples you mentioned? These will help to ensure the tests are accurate and cover the necessary scenarios.

2.  With the provided examples and the requirement to recognize spelled-out numbers, we'll revise the unit tests for the `extract_calibration_values` function to ensure it correctly interprets both numerical digits and numbers spelled out as words. This function now needs to parse and convert spelled-out numbers (one through nine) in addition to identifying numeric digits.

    Here's how we can update and extend the unit tests to cover these new requirements:

```python
import unittest
from your_module import extract_calibration_values  # Adjust the module name as needed

class TestExtractCalibrationValuesWithWords(unittest.TestCase):

    def test_with_spelled_out_numbers(self):
        """Test function with numbers spelled out in words."""
        self.assertEqual(extract_calibration_values(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']), 281)

    def test_mixed_numerals_and_words(self):
        """Test strings containing both numerals and spelled-out numbers."""
        self.assertEqual(extract_calibration_values(['1one1', 'tw2two']), 11 + 22)

    def test_spelled_out_numbers_at_start_and_end(self):
        """Ensure correct processing with spelled-out numbers at start and end of strings."""
        self.assertEqual(extract_calibration_values(['onetwo3fourfive', 'six7eight']), 15 + 68)

    def test_handling_uppercase_and_mixed_case_words(self):
        """Test handling of uppercase and mixed-case spelled-out numbers."""
        self.assertEqual(extract_calibration_values(['THREE3seven', 'fOuR4six']), 37 + 46)

    def test_large_input_with_spelled_out_numbers(self):
        """Test function performance with a large input set including spelled-out numbers."""
        large_input = ['one2three'] * 1000  # Repeat 'one2three' 1000 times
        self.assertEqual(extract_calibration_values(large_input), 13 * 1000)

    def test_with_special_characters_and_spelled_out_numbers(self):
        """Test strings with special characters and spelled-out numbers."""
        self.assertEqual(extract_calibration_values(['!one@#2$', '%three^&*four(']), 12 + 34)

if __name__ == '__main__':
    unittest.main()
```

These tests are designed to ensure that `extract_calibration_values` functionally meets the new requirement to recognize and process spelled-out numbers from "one" to "nine" as valid digits, in addition to handling numeric digits. It includes tests for handling mixed-case and special characters, which are critical given the updated problem statement.
Adjustments might be needed based on the exact implementation details of your function, especially concerning how it identifies and converts spelled-out numbers to their numeric equivalents. Additionally, ensure that your function is case-insensitive when interpreting spelled-out numbers to accommodate variations in input.

**Result**

TP = 0
FP = 0
TN = 6
FN = 0
