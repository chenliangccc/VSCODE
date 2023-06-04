#
# @lc app=leetcode.cn id=1250 lang=python
#
# [1250] 检查「好数组」
#

# @lc code=start
from functools import reduce
# from math import gcd


class Solution(object):

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return reduce(self.gcd, nums) == 1


# @lc code=end
