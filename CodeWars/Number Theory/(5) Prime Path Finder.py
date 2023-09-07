from collections import defaultdict
from functools import reduce
from itertools import pairwise
from operator import or_

from gmpy2 import is_prime, next_prime
from sympy import isprime


def get_neighbours():
    primes = {p for p in range(1000, 9999) if isprime(p)}
    table = defaultdict(list)
    for n in primes:
        for a, b in pairwise((10_000, 1_000, 100, 10, 1)):
            # pairwise('ABCDEFG') --> AB BC CD DE EF FG
            stop = n + a - n % a
            for m in range(n + b, stop, b):
                if m in primes:
                    table[n].append(m)
                    table[m].append(n)
    return table


neighbours = get_neighbours()

# print(neighbours)


def find_shortest_path(start, end):
    paths = {start: [start]}
    seen = {start}
    while end not in paths:
        seen.update(paths)
        paths = reduce(
            or_,
            (
                {q: path + [q] for q in neighbours[p] if q not in seen}
                for p, path in paths.items()
            ),
        )
    return paths[end]


# print(find_shortest_path(3797, 5813))
