'''
https://www.codewars.com/kata/64294e2be00c71422d1f59c2/python
You've found yourself a magic box, which seems to break the laws of physics. You notice that if you put some money in it, it seems to spit out more money than was put in. Free money right?

In time you notice the following facts:

If you start with N dollars, using the box twice yields exactly 3*N dollars
You never seem to get any fractional dollar amounts
The box consistently gives the same amount out, if the amount put in is the same
The more money you put in, the more money you get out
Note: "using the box twice" means using it once, and then using it again with all of the money the box gave you.

The four above mentioned facts can be succinctly stated as follows: f is a function mapping between non-negative integers such that f(f(n)) = 3*n and f(n+1) > f(n) for all n

Your task is to define the function f, such that it predicts the number of dollars produced by the box when n dollars are put in it.(i.e. f(n) gives how many dollars the box gives when used on n once, not twice.

A Note of tests:

Input 0 <= N < 10000000
The actual output for any given input is NOT validated directly. As long as your function satisfies the above specifications, you should pass the tests
'''
# 6kyu????????????????
import math


def f(n):
    if n == 0:
        return 0
    k = 3 ** math.floor(math.log(n, 3))
    if n < 2*k:
        return n+k
    return 3 * (n-k)


print(f(6))
