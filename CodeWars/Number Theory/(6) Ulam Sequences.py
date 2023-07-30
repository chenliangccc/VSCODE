# https://www.codewars.com/kata/5995ff073acba5fa3a00011d/train/python
"""
Example
The first 10 terms of the sequence U(u0=1, u1=2) are: 1, 2, 3, 4, 6, 8, 11, 13, 16, 18.

Let's see it in details:

The first term after the initial 1, 2 is obviously 3, because 1 + 2 = 3
The next term is 1 + 3 = 4 (we don't have to worry about 4 = 2 + 2 since it is a sum of a single term instead of distinct terms)
5 is not a member of the sequence since it is representable in two ways: 1 + 4 and 2 + 3
6 is a memeber, as 2 + 4 = 6
etc."""


from collections import defaultdict
from itertools import combinations


def ulam_sequence(u0, u1, n):
    """
    u0 = first number
    u1 = second numberr
    n = final number of elements in the sequence
    """
    seq = [u0, u1, u0 + u1]  # 初始化数列为 [u0, u1, u0+u1]

    while len(seq) < n:  # 如果数列中的元素个数小于 n，继续循环
        candidates = defaultdict(int)  # 初始化 candidates 为 defaultdict(int)

        for a, b in combinations(seq, 2):  # 遍历 seq 中任意两个元素的组合
            candidates[a + b] += 1  # 将 a+b 的出现次数加 1

        for num, pairs in sorted(candidates.items()):  # 遍历 candidates 中的每个元素
            if num > seq[-1] and pairs == 1:  # 如果 num 大于 seq 中的最后一个元素，并且 pairs 等于 1
                seq.append(num)  # 将 num 加入数列中
                break  # 跳出循环

    return seq  # 返回数列
