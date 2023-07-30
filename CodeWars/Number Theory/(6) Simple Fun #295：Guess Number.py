# https://www.codewars.com/kata/591e62eef99b994288000057/train/python
from math import log
from sympy import nextprime

# 方法1


def guess_what(n):
    """
    logic:
    every number from 1 to n has a unique factorisation
    so to narrow down each number, you need to be able to deduce the prime factorisation with your guesses
    so using the primes from 1 to n you need to the power you must raise each prime to in order to get n
    for the general prime p there are int(log(n, p))+1 powers of p from 1 to n that you could choose from
    however you don't need to check the last power of p because you can use process of elimination
    so you only need to check check divisibility using int(log(n, p)) powers of p to determine which power of p was used to make the number
    """
    total, p = 0, 2
    while p <= n:
        total += int(log(n, p))
        p = int(nextprime(p))
    return total


# 方法2
def find_divs(max=10**3):
    def is_prime(n): return n == 2 or all(n % k for k in [2] + [*range(3, int(n**.5) + 1, 2)])
    marg = int(max**.5)
    res = {k for k in range(2, max + 1) if is_prime(k)}
    res = res | {d**pw for d in res if d <= marg for pw in range(2, int(log(max, d)) + 1)}
    print(res)
    return res


def guess_what_2(n):
    DIVS = find_divs()
    return sum(x <= n for x in DIVS)


print(guess_what_2(15))
