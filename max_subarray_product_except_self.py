# Given an integer array nums,
# return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# 1) find prefix for all nums
# 2) find postfix for all nums
# yt: https://www.youtube.com/watch?v=bNvIQI2wAjk

def max_subarray_product_except_self(nums):
    prefix = 1
    ans = [1] * len(nums)
    for i in range(len(nums)):
        ans[i] *= prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]
    return ans


# nums = [1, 2, 3, 4]
# [2 * 3 * 4, 1 * 3 * 4, 1 * 2 * 4, 1 * 2 * 3] = [24, 12, 8, 6]
# max_subarray_product_except_self(nums)
