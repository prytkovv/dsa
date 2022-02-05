def max_heapify(values, heapsize, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heapsize and values[l] > values[i]:
        largest = l
    if r < heapsize and values[r] > values[largest]:
        largest = r
    if largest != i:
        values[i], values[largest] = values[largest], values[i]
        max_heapify(values, heapsize, largest)


def heapsort(values):
    heapsize = len(values)
    for i in range(heapsize // 2, -1, -1):
        max_heapify(values, heapsize, i)
    for i in range(heapsize - 1, 0, -1):
        values[0], values[i] = values[i], values[0]
        max_heapify(values, i, 0)


# import random
# values = [random.randint(1, 100) for _ in range(10)]
# heapsort(values)
