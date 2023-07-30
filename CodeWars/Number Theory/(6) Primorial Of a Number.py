# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/python
"""Definition (Primorial Of a Number)
Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied, only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P# and it is the product of the first n prime numbers.
Task:
Given a number N , calculate its primorial.
"""


def num_primorial(n):
    primorial, x, n = 2, 3, n-1  # 初始化 primorial 为 2，x 为 3，n 减 1
    while n:
        if all(x % d for d in range(3, int(x**.5)+1, 2)):  # 判断 x 是否为质数
            primorial *= x  # 如果是质数，则将其乘入 primorial 中
            n -= 1  # n 减 1
        x += 2  # x 加 2，因为偶数不可能是质数
    return primorial
