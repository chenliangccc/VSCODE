#
# @lc app=leetcode.cn id=914 lang=python
#
# [914] 卡牌分组
#

# @lc code=start


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
# collections.Counter统计字符串（数字）种类及数量，返回字典；
        from collections import Counter

# math.gcd求两个数的最大公约数，返回整数；
        from math import gcd

#! functools.reduce逐次对上次函数结果与当前序列元素应用函数:
    # ! reduce(function, sequence)
    # ! 例如 reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 计算为((((1+2)+3)+4)+5)
        from functools import reduce

        # 统计所有牌的数量
        vals = Counter(deck).values()

        return reduce(gcd, vals) >= 2


deck = [1, 2, 3, 4, 4, 3, 2, 1]
print(Solution().hasGroupsSizeX(deck))
# @lc code=end
