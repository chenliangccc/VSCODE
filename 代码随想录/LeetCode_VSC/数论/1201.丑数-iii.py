#
# @lc app=leetcode.cn id=1201 lang=python
#
# [1201] 丑数 III
#

# @lc code=start


class Solution(object):
    # 实现gcd
    def _gcd_(self, a, b):
        if a < b:
            a, b = b, a
        return a if b == 0 else self._gcd_(b, a % b)
    # 实现lcm

    def _lcm_(self, li):
        lcm = li[0]
        for i in li[1:]:
            lcm = lcm*i/self._gcd_(lcm, i)
        return lcm

    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        from math import lcm
        # 1.abc之间的最小公倍数
        lab, lbc, lac, labc = lcm(a, b), lcm(b, c), lcm(a, c), lcm(a, b, c)

        def countugly(x):  # 丑数数量
            # 1.计算出范围内有多少个可以被a,b,c整除的数
            # 2.减去被a,b,c里两个数同时整除的情况（如果一个数既能被a整除，又能被b整除，那么实际上该数在先前的计算中就被重复计算了一次）
            # 3.加上被a,b,c三个数字同时整除的情况
            return x//a + x//b + x//c - x//lab - x//lbc - x//lac + x//labc

        # 取二分查找的范围，按题意，a,b,c中最小的数字乘以n作为最大值必然满足条件，并和题目要求范围进行比较取较小值，以防超出题目要求上限
        # l, r = 1, min(min(a, b, c)*n, 2*pow(10, 9))

        # 优化：丑数一定是a,b,c的倍数，那么以三数的最小公倍数为间隔，每个间隔出现的丑数数量是相等的，对于每一个丑数可以缩小搜索范围
        l, r = n // countugly(labc) * labc, (n // countugly(labc)+1) * labc
        # 二分查找
        while l < r:
            m = (l+r)//2
            if countugly(m) < n:
                l = m + 1
            else:
                r = m
        return l

# @lc code=end
