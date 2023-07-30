# https://www.codewars.com/kata/59974515b4c40be3cc000263
"""
For example:
A(8) = (1 + 2 + 4 + 8) / 8 = 15/8
A(25) = (1 + 5 + 25) / 25  = 31/25

Friendly Pairs are pairs of numbers (m, n), such that their abundancies are equal: A(n) = A(m).
Write a function that returns "Friendly!" if the two given numbers are a Friendly Pair. Otherwise return their respective abundacies as strings separated by a space, e.g. "1 15/8"
"""
from fractions import Fraction
from math import gcd


# Method 1:myself
def divisor(n):
    ans = [1, n]
    for i in range(2, int(n * 0.5 + 1)):
        if n % i == 0:
            ans.append(i)
    return ans


def gcd_divisor(n):
    sum_n = sum(divisor(n))
    if g := gcd(sum_n, n):
        sum_n //= g
        n //= g
    return [1] if sum_n == n else [sum_n, n]


def friendly_numbers_1(m, n):
    """
    Input
    m - first integer
    n - second integer

    Return
    'Friendly!' if they are friendly pairs
    else
    'Am An' (their abundancies as rational strings)
    """
    Am = f"{gcd_divisor(m)[0]}/{gcd_divisor(m)[1]} "  # type: ignore

    An = f"{gcd_divisor(n)[0]}/{gcd_divisor(n)[1]}"  # type: ignore
    return "Friendly!" if gcd_divisor(m)[0] == gcd_divisor(n)[0] else Am+An


# Method 2: best practices
def getDivisors(x):
    for n in range(1, int(x**.5)+1):
        if not x % n:
            yield n
            if n != x//n:
                yield x//n


def friendly_numbers_2(m, n):
    a, b = sum(getDivisors(m)), sum(getDivisors(n))
    return "Friendly!" if a/m == b/n else f"{Fraction(a, m)} {Fraction(b, n)}"


print(friendly_numbers_1(10, 11))
print(friendly_numbers_2(10, 11))
