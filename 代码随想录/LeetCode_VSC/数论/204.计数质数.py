#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#


# @lc code=start
class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 厄拉多塞筛法：找出{0,...,n-1}内的质数
        if n < 2:
            return 0

        isPrime = [1] * n
        # 0和1不是质数，排除
        isPrime[0] = isPrime[1] = 0

        # 把不大于根号n的所有质数的倍数剔除
        ans = int(n**0.5)
        for i in range(2, ans + 1):
            if isPrime[i]:  # 是质数
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)


# @lc code=end
