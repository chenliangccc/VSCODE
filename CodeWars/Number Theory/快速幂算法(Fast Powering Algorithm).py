# 快速幂算法
def power(base, exponent, modulus):
    # base：底数，exponent：指数，modulus：模数
    result = 1
    base %= modulus
    '''
    举例 218(10) = 11011010(2)
    3^218 =3^2 · 3^2^3 · 3^2^4 · 3^2^6 · 3^2^7 
        ≡ 9 · 561 · 721 · 281 · 961 (mod 1000) 
        ≡ 489 (mod 1000).
    '''
    while exponent > 0:
        # 如果指数的当前位为1
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # 将底数乘方，并对模数取模
        base = (base * base) % modulus

        # 将指数右移一位（相当于除以2）
        exponent //= 2

    return result

print(power(3,218,1000))
