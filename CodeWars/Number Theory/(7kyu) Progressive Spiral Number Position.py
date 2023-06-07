# https://www.codewars.com/kata/5a254114e1ce0ecf6a000168/train/python
from math import ceil, sqrt


def layers(n):
    return ceil(sqrt(n)) // 2 + 1
