#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        # 数学：求数字根
        """
        1.num 是0，数字根就是0
        2.num 不是9的倍数，数字根就是 num 对 9 取余， 即 n mod 9
        3.num 是 9 的倍数，数字根就是 9 
        """
        # !这样写找不到9
        # return num % 9 if num else 0
        return (num - 1) % 9 + 1 if num else 0

# @lc code=end
