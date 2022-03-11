# yt: https://www.youtube.com/watch?v=U8XENwh8Oy8


def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# search([4, 5, 6, 7, 0, 1, 2], 0)
# index_of(0) = 4
# search([4, 5, 6, 7, 0, 1, 2], 100)
# index_of(100) = -1
