from math import sqrt


class Solution():
    # 质因数分解
    def prime_factors(self, n: int):
        factors = {}
        for i in range(2, int(sqrt(n)) + 1):
            while n % i == 0:
                if i not in factors:
                    factors[i] = 0
                factors[i] += 1
                n //= i
        if n > 1:
            factors[n] = 1
        return factors

    # 通过标准分解式(质因数分解)求最大公因数和最小公倍数
    def gcd(self, a, b):
        a_factor = self.prime_factors(a)
        b_factor = self.prime_factors(b)
        result = 1
        for factor in set(a_factor.keys()) | set(b_factor.keys()):
            result *= factor**min(a_factor.get(factor, 0),
                                  b_factor.get(factor, 0))
        return result

    def lcm(self, a, b):
        a_factors = self.prime_factors(a)
        b_factors = self.prime_factors(b)
        result = 1
        for factor in set(a_factors.keys()) | set(b_factors.keys()):
            result *= factor**max(a_factors.get(factor, 0),
                                  b_factors.get(factor, 0))
        return result


# print(Solution().gcd(45, 95))
# print(Solution().lcm(45, 95))
print(Solution().prime_factors(5))
print(Solution().prime_factors(95))
