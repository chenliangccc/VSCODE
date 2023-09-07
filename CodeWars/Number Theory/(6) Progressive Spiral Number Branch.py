# https://www.codewars.com/kata/5a26ca51e1ce0e987b0000ee/train/python
"""
17 16 15 14 13    1 1 1 1 0
18 05 04 03 12    2 1 1 0 0
19 06 01 02 11 => 2 2 0 0 0
20 07 08 09 10    2 2 3 3 0
21 22 23 24 25    2 3 3 3 3"""
from math import ceil, floor


def branch(n):
    if n == 1:
        return 0
    # Identify the ring and the edge length of each side
    ring = ceil(n**0.5) // 2 + 1
    edge_length = (ring - 1) * 2
    print("n:", n, "ring:", ring, "edge_length:", edge_length)

    # Find the bracketing odd square roots either side of n
    root = n**0.5
    # l 和 h 分别代表了数字 n 所处的环中最小的奇数和最大的奇数
    l = floor(root) - (floor(root) % 2 == 0)
    h = ceil(root) + (ceil(root) % 2 == 0)
    print("l:", l, "h:", h)
    if l == h:
        # n is an odd square number(the end of this ring) i.e n = (k + 1) ** 2
        l -= 2
    #! First number in ring
    base = l**2 + 1
    print("base: ", base)
    print("return: ", (n - base) // edge_length)
    return (n - base) // edge_length


n = int(input("请输入:"))
branch(n)
