def count_odd_numbers(a, b):
    # 将区间左端点和右端点转换为奇数
    if a % 2 == 0:
        a += 1
    if b % 2 == 0:
        b -= 1
    # 计算区间内的奇数个数
    return (b - a) // 2 + 1


def primes(n):  # 返回一个长度为n的素数列表
    # 埃拉托色尼筛法(Sieve of Eratosthenes)
    '''
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = True
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]
'''
    # 优化版，使用了位运算来优化代码，使用位运算来标记和查询，避免使用除法和模运算，并且值枚举了奇数，将时间复杂度降低了一半
    # 创建一个长度为n//2的布尔型列表sieve，表示从3开始所有的奇数是否为素数
    # 从3开始，依次枚举每个奇数i，如果sieve[i//2]=True，则将i的倍数标记为非素数
    # 最后，函数将2添加到素数列表中，并将所有sieve中为True的元素对应的奇数加1后添加到素数列表中
    sieve = n // 2 * [True]
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            # 计算在[i*i,n]区间里有多少个奇数是i的倍数
            # (b-a)//2*i + 1
            count = (count_odd_numbers(i*i, n)-1)//i + 1
            sieve[i*i//2::i] = [False] * count
            num = [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]
