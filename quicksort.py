def quicksort(values, lo, hi):
    if lo < hi:
        p = partition(values, lo, hi)
        quicksort(values, lo, p)
        quicksort(values, p + 1, hi)


def partition(values, lo, hi):
    pivot = values[(lo + hi) // 2]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while values[i] < pivot:
            i += 1
        j -= 1
        while values[j] > pivot:
            j -= 1
        if i >= j:
            return j
        values[i], values[j] = values[j], values[i]


# import random
# values = [random.randint(1, 100) for _ in range(20)]
# quicksort(values, 0, len(values) - 1)
