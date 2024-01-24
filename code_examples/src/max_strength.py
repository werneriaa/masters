from typing import List


# https://leetcode.com/problems/maximum-strength-of-a-group/description/
# Grade: Medium
def max_strength(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    nums = [num for num in nums if num != 0]

    def mul(arr):
        ans = 1
        for i in arr:
            ans *= i
        if 1 in nums or nums.count(-1) == 2:
            return ans
        else:
            return ans if ans != 1 else 0

    count_neg = 0
    max_neg = -float('inf')
    for i in nums:
        if i < 0:
            count_neg += 1
            max_neg = max(i, max_neg)
    if count_neg % 2 == 0:
        return mul(nums)
    else:
        i = nums.index(max_neg)
        nums.remove(nums[i])
        return mul(nums)
