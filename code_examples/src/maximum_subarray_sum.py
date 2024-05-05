# https://leetcode.com/problems/maximum-good-subarray-sum/description/
# Grade: Medium
# Solution: https://leetcode.com/problems/maximum-good-subarray-sum/solutions/4671754/fully-explained-python-one-pass-o-n/

from typing import List


def maximum_subarray_sum(nums: List[int], k: int) -> int:
    ans = -float('inf')
    prefix = [0]

    # hash_map to track the indices of previous x; |num - x| == k
    hm = dict()

    for i, num in enumerate(nums):

        # update prefix
        prefix.append(prefix[-1] + num)

        # check if there are valid x's if so, update the answer | x = num [+/-] k
        if (num - k) in hm:
            ans = max(ans, prefix[i + 1] - prefix[hm[num - k] + 1] + nums[hm[num - k]])
        if (num + k) in hm:
            ans = max(ans, prefix[i + 1] - prefix[hm[num + k] + 1] + nums[hm[num + k]])

        # check if num contributes more than the previous occurence if so update the index, if not continue
        if num in hm:
            if prefix[i + 1] - prefix[hm[num] + 1] + nums[hm[num]] >= num:
                continue
        hm[num] = i

    return int(ans) if ans != -float('inf') else 0
