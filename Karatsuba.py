import random


def karatsuba(x, y):
    # 如果 x 或 y 是一位数，则直接返回它们的乘积
    if x < 10 or y < 10:
        return x * y
    # 计算 x 和 y 的位数赛奥
    m = max(len(str(x)), len(str(y)))

    m2 = m // 2
    # 将 x 和 y 拆分成两个 m2 位整数
    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)

    # 递归计算三个乘积
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    # 计算结果并返回
    return (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0


def test():
    a, b = random.randint(1, 100000), random.randint(1, 100000)
    print(a * b)
    print(karatsuba(a, b))


test()
