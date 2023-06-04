# https://www.codewars.com/kata/5bbecf840441ca6d6a000126

"""
 Python 的 functools.lru_cache 装饰器，用于缓存函数的结果，以提高函数的效率。这个装饰器可以将函数的结果缓存到内存中，避免重复计算。在这个函数中，我们使用了 lru_cache 装饰器来缓存 f 函数的结果，以提高计算效率。"""


import math


def fixed_points_perms(n, k):
    # your code here
    if k == n:
        return 1
    elif k >= n-1:
        return 0
    elif k == 0:
        # def f(n): return 1 if n == 0 else n * f(n - 1) + (-1)**n
        # 关于f(n)函数的说明：https://github.com/chenliangccc/Picture/blob/main/v2-d9fb230bc4d184092ee8fc4b9b0e36f4_r.png
        def f(n):
            result = 0
            for k in range(2, n+1):
                result += (-1)**k / math.factorial(k)
            return math.factorial(k) * result
        print(f(3))
        return f(n)
    return n * fixed_points_perms(n-1, k-1) // k


print(fixed_points_perms(4, 1))
