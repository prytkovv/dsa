# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# yt: https://www.youtube.com/watch?v=KLlXCFG5TnA&t=279s


def two_sum(nums, target):
    cache = dict()
    for i, n in enumerate(nums):
        if target - n in cache:
            return i, cache.get(target - n)
        cache[n] = i


# nums = [3, 2, 4]
# 2 + 4 = 6, index_of(2) = 1, index_of(4) = 2
# two_sum(nums, 6)
