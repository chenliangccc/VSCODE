# (6kyu) Jungerstein's Math Training Room：How many zeros are at the end of n!! ？
# https://www.codewars.com/kata/58cbfe2516341cce1e000001
def count_zeros_n_double_fact(n):
    # 如果 n 是奇数，则 n!! 的末尾一定没有零，直接返回 0
    if n % 2 != 0:
        return 0
    k = 0
    # 计算 n!! 中因子 5 的个数
    """由于 n!! 中每隔 2 个数字相乘，因此其中因子 2 的个数一定大于等于因子 5 的个数。因此，我们只需要计算因子 5 的个数即可。另外，由于每个因子 5 都可以和一个因子 2 相乘得到一个因子 10，因此因子 5 的个数就是末尾的零的个数。 """
    while n >= 10:
        k += n // 10
        n //= 5
    # 返回 n!! 中因子 10 的个数，也就是末尾的零的个数
    return k


print(count_zeros_n_double_fact(30))
