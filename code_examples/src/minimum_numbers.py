# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
# Grade: Medium
def minimum_numbers(num: int, k: int) -> int:
    if num == 0:
        return 0
    unit = num % 10
    for i in range(1, 11):
        if (i * k) % 10 == unit:
            if i * k <= num:
                return i
            else:
                break
    return -1
