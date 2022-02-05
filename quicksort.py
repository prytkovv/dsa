def quicksort(values, lo, hi):
    if lo >= hi or lo < 0:
        return
    p = partition(values, lo, hi)
    quicksort(values, lo, p)
    quicksort(values, p + 1, hi)


def partition(values, lo, hi):
    pivot = values[(lo + hi) // 2]
    i = lo - 1
    j = hi + 1
    while True:
        while True:
            i += 1
            if values[i] >= pivot:
                break
        while True:
            j -= 1
            if values[j] <= pivot:
                break
        if i >= j:
            return j
        values[i], values[j] = values[j], values[i]


# import random
# values = [random.randint(1, 100) for _ in range(10)]
# quicksort(values, 0, len(values) - 1)
