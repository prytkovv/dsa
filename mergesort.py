def merge_sort(values):
    if len(values) > 1:
        mid = len(values) // 2
        left = values[:mid]
        right = values[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                values[k] = left[i]
                i += 1
            else:
                values[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            values[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            values[k] = right[j]
            j += 1
            k += 1


# import random
# values = [random.randint(1, 100) for _ in range(1, 20)]
# merge_sort(values)
