def gcd(a, b):
    return gcd(b, a % b) if b else a


def extend_gcd(a, b):
    """扩展欧几里得算法"""
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extend_gcd(b, a % b)
        return (g, y, x - a // b * y)


def multiplicative_inverse(a, n):
    """
    计算乘法逆元

    参数:
    a -- 需要计算逆元的数
    n -- 模数

    返回:
    a 在 mod n 下的乘法逆元

    注意:
    这个函数使用了欧几里得算法，时间复杂度为 O(log n)。
    """
    g, x, y = extend_gcd(a, n)
    if g != 1:
        return "无逆元"
    else:
        return (x + n) % n


a = 6
n = 23
print("乘法逆元:", multiplicative_inverse(a, n))
