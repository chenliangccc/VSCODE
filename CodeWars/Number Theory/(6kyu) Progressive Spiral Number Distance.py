# https://www.codewars.com/kata/5a27e3438882f334a10000e3/train/python
"""
17 16 15 14 13    4 3 2 3 4
18 05 04 03 12    3 2 1 2 3
19 06 01 02 11 => 2 1 0 1 2
20 07 08 09 10    3 2 1 2 3
21 22 23 24 25    4 3 2 3 4
"""


from math import ceil


def distance(n):
    # your code here
    if n == 1:
        return 0
     # Identify the layer and the edge length of each side
    layer = ceil(n ** 0.5) // 2 + 1
    edge_length = (layer - 1) * 2
    # 在该layer上的位置
    position = n - (2 * (layer - 1) - 1) ** 2
    offset = abs(position % edge_length - (edge_length // 2))

    return layer - 1 + offset


print((distance(25)))
