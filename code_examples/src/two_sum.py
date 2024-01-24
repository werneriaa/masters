from typing import List

# https://leetcode.com/problems/two-sum/description/
# Grade Easy

def two_sum(nums: List[int], target: int) -> List[int]:
  hash_table = {}
  for i in range(len(nums)):
    if nums[i] in hash_table:
      return [hash_table[nums[i]], i]
    else:
      hash_table[target - nums[i]] = i
