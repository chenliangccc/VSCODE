# https://www.codewars.com/kata/632abe6080604200319b7818/train/python
'''We need a code that receives the following 3 integers as inputs:
k, ordinal number of the corresponding prime in a sorted increasing sequence of primes

n, number of consecutive primes that form the product of powers

base, the base of the numeriacal system that may have values multiple of 4 and below or equal 52.
'''

import string
from itertools import count, islice
from math import prod


def is_prime(n):
    # 试除法思想:从2-N**0.5之间枚举所有可能的因子,判断是否存在因子可以整除
    # 首先判断是否小于等于 3，如果是，则只有当 $n$ 等于 2 或 3 时，它才是素数，否则不是素数
    if n <= 3:
        return n >= 2
    if not n % 2 or not n % 3:
        return False
    # 步长为 6 是因为除了 2 和 3 以外的素数都可以表示为 6k+-1 的形式
    for i in range(5, int(n ** 0.5 + 1), 6):
        # 由于5=6*1-1，所以分别对i和i+2取余
        if not n % i or not n % (i + 2):
            return False
    return True


# P:前1000个素数
# 1.用 count 函数生成一个无限的整数序列，从 3 开始，步长为 2
# 2.然后，我们使用 filter 函数和 is_prime 函数来筛选出这个序列中的素数。其中，is_prime 函数用于判断一个整数是否为素数
# 3.用islice和list函数取前1000个素数
P = [None, 2] + [*islice(filter(is_prime, count(3, 2)), 999)]

# 转换成b进制表示的字符串
C = string.ascii_uppercase + string.ascii_lowercase
def to_base(n, b): return to_base(n//b, b).lstrip("0") + C[n % b] if n else "0"


def solver(k, n, b):
    seq = P[k:k+n]
    # prod：计算输入的 iterable 中所有元素的积。 积的默认 start 值为 1
    def f(lst): return prod(p**i for i, p in enumerate(lst, 1))
    x, y = [*map(f, (seq, seq[::-1]))]
    return to_base(x, b), to_base(y, b)
