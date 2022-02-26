def find_max(values):
    low = 0
    high = len(values) - 1
    max_item = values[0]
    while low <= high:
        if values[low] < values[high]:
            max_item = max(max_item, values[high])
            return max_item
        mid = (low + high) // 2
        max_item = max(max_item, values[mid])
        if values[mid] > values[low]:
            low = mid + 1
        else:
            high = mid - 1
    return max_item


# values = [3, 4, 5, 1, 2]
# max => 5
# find_max(values)
