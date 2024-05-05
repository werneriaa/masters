## Find max achievable number

**DATE**
27.2.2024

**Grade**
Easy

**Prompt**
You are given two integers, num and t.

An integer x is called achievable if it can become equal to num after applying the following operation no more than t times:

Increase or decrease x by 1, and simultaneously increase or decrease num by 1.

Return the maximum possible achievable number. It can be proven that there exists at least one achievable number.

Example 1:

Input: num = 4, t = 1

Output: 6

Explanation: The maximum achievable number is x = 6; it can become equal to num after performing this operation:

1- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5.

It can be proven that there is no achievable number larger than 6.

Example 2:

Input: num = 3, t = 2

Output: 7

Explanation: The maximum achievable number is x = 7; after performing these operations, x will equal num:

1- Decrease x by 1, and increase num by 1. Now, x = 6 and num = 4.

2- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5.

It can be proven that there is no achievable number larger than 7.

Constraints:

1 <= num, t <= 50

**Answer**

```
import unittest

from placeholder import max_achievable_number



class TestMaxAchievableNumber(unittest.TestCase):



def test_example_1(self):

self.assertEqual(max_achievable_number(4, 1), 6, "The maximum achievable number with num=4 and t=1 should be 6.")



def test_example_2(self):

self.assertEqual(max_achievable_number(3, 2), 7, "The maximum achievable number with num=3 and t=2 should be 7.")



def test_num_equals_t(self):

self.assertEqual(max_achievable_number(5, 5), 10, "The maximum achievable number with num=5 and t=5 should be 10.")



def test_num_greater_than_t(self):

self.assertEqual(max_achievable_number(10, 2), 12, "The maximum achievable number with num=10 and t=2 should be 12.")



def test_t_greater_than_num(self):

self.assertEqual(max_achievable_number(2, 10), 12, "The maximum achievable number with num=2 and t=10 should be 12.")



def test_min_constraints(self):

self.assertEqual(max_achievable_number(1, 1), 2, "The maximum achievable number with the minimum constraints (num=1, t=1) should be 2.")



def test_max_constraints(self):

self.assertEqual(max_achievable_number(50, 50), 100, "The maximum achievable number with the maximum constraints (num=50, t=50) should be 100.")



if **name** == "**main**":

unittest.main()
```

**Result**

TP = 0
FP = 5
TN = 2
FN = 0

COVERAGE 100%

The AI didnt understand correctly how the function should work. It generated two test cases correctly based on the example provided in the description.

However the base setup was correctly done, only thing i had to change was the import. Also the test code worked.

## Sum of Numbers With Units Digit K

**DATE**
27.2.2024

**Grade**
Medium

**Prompt**
Given two integers `num` and `k`, consider a set of positive integers with the following properties:

- The units digit of each integer is `k`.
- The sum of the integers is `num`.

Return *the **minimum** possible size of such a set, or* `-1` *if no such set exists.*

Note:

- The set can contain multiple instances of the same integer, and the sum of an empty set is considered `0`.
- The **units digit** of a number is the rightmost digit of the number.

**Example 1:**

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

**Constraints:**

- `0 <= num <= 3000`
- `0 <= k <= 9`

**Answer**

```
import unittest

from solution import min_set_size



class TestMinSetSize(unittest.TestCase):

def test_example1(self):

self.assertEqual(min_set_size(58, 9), 2, "Example 1 failed")



def test_example2(self):

self.assertEqual(min_set_size(37, 2), -1, "Example 2 failed")



def test_example3(self):

self.assertEqual(min_set_size(0, 7), 0, "Example 3 failed")



def test_sum_zero_with_non_zero_k(self):

self.assertEqual(min_set_size(0, 5), 0, "Sum zero with non-zero k failed")



def test_k_zero_with_non_zero_num(self):

self.assertEqual(min_set_size(10, 0), 1, "k zero with non-zero num failed")



def test_max_constraints(self):

self.assertEqual(min_set_size(3000, 9), 334, "Max constraints failed")



if __name__ == "__main__":

unittest.main()
```

**Result**

TP = 0
FP = 1
TN = 5
FN = 0

COVERAGE 90%

It was able understand the task quite well, how ever the line coverage was 90% with this function, which means some of the edge cases were not covered

##  Median of Two Sorted Arrays

**DATE**
27.2.2024

**Grade**
Hard

**Prompt**
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1:**

**Input:** nums1 = [1,3], nums2 = [2]
**Output:** 2.00000
**Explanation:** merged array = [1,2,3] and median is 2.

**Example 2:**

**Input:** nums1 = [1,2], nums2 = [3,4]
**Output:** 2.50000
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`

**Answer**

```
import unittest
from placeholder import find_median_sorted_arrays

class TestFindMedianSortedArrays(unittest.TestCase):

    def test_single_element_each(self):
        self.assertEqual(find_median_sorted_arrays([1], [2]), 1.5)

    def test_single_element_one_empty(self):
        self.assertEqual(find_median_sorted_arrays([], [1]), 1.0)

    def test_two_elements_each_even_total(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)

    def test_two_elements_each_odd_total(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0)

    def test_with_negative_numbers(self):
        self.assertEqual(find_median_sorted_arrays([-5, -3, -1], [0, 2, 4]), -1.0)

    def test_large_numbers(self):
        self.assertEqual(find_median_sorted_arrays([100000], [100001]), 100000.5)

    def test_empty_first_array(self):
        self.assertEqual(find_median_sorted_arrays([], [1, 2, 3, 4, 5]), 3.0)

    def test_empty_second_array(self):
        self.assertEqual(find_median_sorted_arrays([1, 2, 3, 4, 5], []), 3.0)

if __name__ == '__main__':
    unittest.main()

```

**Result**

TP = 0
FP = 1
TN = 7
FN = 0

AI understood the answer very well, but one test failed with no purpose. Some of the tests werent necessary to achieve 100% coverage, but those are labelled as TP since they tested edge cases still

## AoC Day 1

**DATE**
27.2.2024

**Grade**
Hard

**Prompt**
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all *fifty stars* by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants *one star*. Good luck!

You try to ask why they can't just use a [weather machine](https://adventofcode.com/2015/day/1) ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a [trebuchet](https://en.wikipedia.org/wiki/Trebuchet) ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been *amended* by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific *calibration value* that the Elves now need to recover. On each line, the calibration value can be found by combining the *first digit* and the *last digit* (in that order) to form a single *two-digit number*.

For example:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces `_142_`.

Consider your entire calibration document. *What is the sum of all of the calibration values?*

**Answer**

```
import unittest
from placeholder import sum_calibration_values

class TestSumCalibrationValues(unittest.TestCase):

    def test_empty_document(self):
        """Test that an empty document returns a sum of 0."""
        self.assertEqual(sum_calibration_values([]), 0)

    def test_single_line_document(self):
        """Test documents with a single line."""
        self.assertEqual(sum_calibration_values(["1abc2"]), 12)
        self.assertEqual(sum_calibration_values(["pqr3stu8vwx"]), 38)
        self.assertEqual(sum_calibration_values(["a1b2c3d4e5f"]), 15)
        self.assertEqual(sum_calibration_values(["treb7uchet"]), 77)

    def test_multiple_lines_document(self):
        """Test documents with multiple lines."""
        document = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(sum_calibration_values(document), 142)

    def test_lines_with_no_digits(self):
        """Test lines that do not contain any digits."""
        self.assertEqual(sum_calibration_values(["abcdefg", "xyz"]), 0)

    def test_lines_with_single_digit(self):
        """Test lines with only one digit, which should be ignored."""
        self.assertEqual(sum_calibration_values(["a1bcdefg", "xy2z"]), 0)

    def test_line_with_digits_at_ends(self):
        """Test lines where digits are at the very beginning and end."""
        self.assertEqual(sum_calibration_values(["9abcdefgh1"]), 91)

if __name__ == "__main__":
    unittest.main()

```

**Result**

TP = 0
FP = 0
TN = 0
FN = 0

AI understood the thing very well, only error it made was it thought "asd6asd" is 0, but based on the examples they it should 66. Coverage Still 100%

**Part2**

Continue from part 1

**Prompt**

## --- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually *spelled out with letters*: `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine` *also* count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

In this example, the calibration values are `29`, `83`, `13`, `24`, `42`, `14`, and `76`. Adding these together produces `_281_`.

_What is the sum of all of the calibration values?_

**Answer**

```
class TestSumCalibrationValuesWithTextDigits(unittest.TestCase):

    def test_with_text_digits(self):
        """Test documents with spelled out digits."""
        document = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"
        ]
        self.assertEqual(sum_calibration_values(document), 281)

    def test_mixed_text_and_numeric_digits(self):
        """Test lines with both spelled out and numeric digits."""
        self.assertEqual(sum_calibration_values(["one2three"]), 13)
        self.assertEqual(sum_calibration_values(["four5six"]), 46)
        self.assertEqual(sum_calibration_values(["seven8nine"]), 79)

    def test_spelled_out_digits_only(self):
        """Test lines with only spelled out digits."""
        self.assertEqual(sum_calibration_values(["oneeight"]), 18)
        self.assertEqual(sum_calibration_values(["twoseven"]), 27)
        self.assertEqual(sum_calibration_values(["threefour"]), 34)

    def test_spelled_out_single_digit(self):
        """Test lines with a single spelled out digit, which should be ignored."""
        self.assertEqual(sum_calibration_values(["onetwo"]), 0)
        self.assertEqual(sum_calibration_values(["three"]), 0)

    def test_empty_and_no_digit_lines(self):
        """Test empty lines and lines with no digits."""
        document = ["", "abcdefg", "onetwo", "xyz"]
        self.assertEqual(sum_calibration_values(document), 0)

if __name__ == "__main__":
    unittest.main()
```

**Result**

TP = 1
FP = 2
TN = 8
FN = 0

AI understood the thing very well, only error it made was it thought "asd6asd" is 0, but based on the examples they it should 66. Coverage Still 100%
