# https://www.codewars.com/kata/63304cd2c68f640016b5d162/train/python
# Your goal is to write the function gcd_coeff that accepts two on-negative integers a and b and returns a tuple (x,y) of integer coefficients x and y expressing gcd(a,b) as x⋅a+y⋅b. You may assume that a≥b is always satisfied.
"""
Input:  two non-negative integers a and b, satisfying a >= b.
Output: a tuple (x, y) satisfying gcd(a, b) = x*a + y*b.
"""


def gcd_coeff(a: int, b: int) -> tuple:
    # 扩展欧几里得算法
    if b == 0:
        return (1, 0)
    else:
        x1, y1 = gcd_coeff(b, a % b)
        x = y1
        y = x1 - (a//b) * y1
        return (x, y)
