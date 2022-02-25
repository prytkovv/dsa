
def split(values, number):
    size, extra_size = divmod(len(values), number)
    chunks = []
    for i in range(number):
        chunk = values[i * size + min(i, extra_size): (i + 1) * size + min(i + 1, extra_size)]
        chunks.append(chunk)
    return chunks


# [[0, 1], [2], [3]]
# split(list(range(4)), 3)
