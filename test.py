from itertools import pairwise

for a, b in pairwise((10_000, 1_000, 100, 10, 1)):
    print(a, b)
