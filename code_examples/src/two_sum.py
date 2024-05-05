from typing import List

# https://leetcode.com/problems/two-sum/description/
# Grade: Easy
# Solution: https://leetcode.com/problems/two-sum/solutions/4856661/video-visualization-using-a-hash-map/


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
