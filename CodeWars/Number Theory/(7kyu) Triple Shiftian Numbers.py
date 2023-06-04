"""
https://www.codewars.com/kata/56b7526481290c2ff1000c75/train/python
Much cooler than your run-of-the-mill Fibonacci numbers, the Triple Shiftian are so defined: T[n] = 4 * T[n-1] - 5 * T[n-2] + 3 * T[n-3].

You are asked to create a function which accept a base with the first 3 numbers and then returns the nth element.

triple_shiftian([1,1,1],25) == 1219856746
triple_shiftian([1,2,3],25) == 2052198929
triple_shiftian([6,7,2],25) == -2575238999
triple_shiftian([3,2,1],35) == 23471258855679
triple_shiftian([1,9,2],2) ==  2
Note: this is meant to be an interview quiz, so the description is scarce in detail on purpose
"""


def triple_shiftian(base, n):
    # for i in range(2, n):
    #     base.append(4*base[i] - 5*base[i-1] + 3*base[i-2])
    # return base[n]
    a, b, c = base
    for _ in range(n):
        a, b, c = b, c, 4*c-5*b+3*a
    return a


triple_shiftian([1, 1, 1], 25)
