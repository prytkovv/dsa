def binary_search(values, item_to_be_found):
    lower_bound = 0
    higher_bound = len(values) - 1
    while lower_bound <= higher_bound:
        mid = (lower_bound + higher_bound) // 2
        item = values[mid]
        if item == item_to_be_found:
            return mid
        elif item > item_to_be_found:
            higher_bound = mid - 1
        else:
            lower_bound = mid + 1
    return None


# import random
# values = sorted([random.randint(1, 100) for _ in range(20)])
# item = random.choice(values)
# binary_search(values, item)
