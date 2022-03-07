# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# yt: https://www.youtube.com/watch?v=Pcd1ii9P9ZI


def remove_item(nums, val):
    counter = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[counter] = nums[i]
            counter += 1
    return counter


# nums = [3, 2, 2, 3]
# nums[: counter] = [2, 2]
# remove_item(nums, 3)
