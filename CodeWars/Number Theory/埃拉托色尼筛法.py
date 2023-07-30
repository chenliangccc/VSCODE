def primes(n):
    # 如果 n 小于 2，则返回空列表
    if n < 2:
        return []
    # 创建一个长度为 n//2 的布尔型列表 sieve，表示从 3 开始所有的奇数是否为素数
    sieve = [True] * ((n // 2) + 1)
    # 将 2 添加到素数列表中
    primes = [2]
    # 从 3 开始，依次枚举每个奇数 i，如果 sieve[i//2]=True，则将 i 的倍数标记为非素数
    for i in range(3, n + 1, 2):
        if sieve[i // 2]:
            primes.append(i)
            # 将 i 的倍数标记为非素数
            for j in range(i * i, n + 1, 2 * i):
                sieve[j // 2] = False
    # 返回素数列表
    return primes


print(primes(22))
