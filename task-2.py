data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([i for k, i in enumerate(data) if k and i > data[k - 1]])
