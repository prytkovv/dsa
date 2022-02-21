# wiki: https://en.wikipedia.org/wiki/Maximum_subarray_problem
# yt: https://www.youtube.com/watch?v=5WZl3MMT0Eg

def max_subarray(values):
    max_sum = values[0]
    temp_sum = 0
    for v in values:
        if temp_sum < 0:
            temp_sum = 0
        temp_sum += v
        max_sum = max(max_sum, temp_sum)
    return max_sum


# max_subarray = [-4, -1, 2, 1]
# max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
