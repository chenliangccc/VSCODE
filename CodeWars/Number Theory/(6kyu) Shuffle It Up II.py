# https://www.codewars.com/kata/5bbecf840441ca6d6a000126

"""
 Python 的 functools.lru_cache 装饰器，用于缓存函数的结果，以提高函数的效率。这个装饰器可以将函数的结果缓存到内存中，避免重复计算。在这个函数中，我们使用了 lru_cache 装饰器来缓存 f 函数的结果，以提高计算效率。"""
from functools import lru_cache


# 数学参考：
# joplin://x-callback-url/openNote?id=b713ddc34d6a4a0fa737e1764da73a2c
@lru_cache(maxsize=None)
def f(n):
    return n-1 if n <= 2 else (n-1) * (f(n-1)+f(n-2))


def fixed_points_perms(n, k):
    # your code here
    if k == n:
        return 1
    elif k >= n-1:
        return 0
    elif k == 0:
        # def f(n): return 1 if n == 0 else n * f(n - 1) + (-1)**n
        return f(n)
    return n * fixed_points_perms(n-1, k-1) // k
