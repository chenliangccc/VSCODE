# https://www.codewars.com/kata/5286b2e162056fd0cb000c20/train/python
"""
f(n)= n/2, if n is even
      3n+1, if n is odd
"""


def collatz(n):
    # 该函数接受一个正整数 n 作为输入，返回一个字符串，表示 Collatz 猜想的序列。
    # 如果 n 为 1，则返回字符串 "1"。
    if n == 1:
        return "1"
    # 如果 n 为偶数，则返回字符串 n + "->" + collatz(n // 2)。
    elif n % 2 == 0:
        return str(n) + "->" + collatz(n // 2)
    # 如果 n 为奇数，则返回字符串 n + "->" + collatz(3 * n + 1)。
    else:
        return str(n) + "->" + collatz(3 * n + 1)


print(collatz(3))
