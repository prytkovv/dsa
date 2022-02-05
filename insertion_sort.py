def insertion_sort(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key


# import random
# values = [random.randint(1, 100) for _ in range(10)]
# insertion_sort(values)
