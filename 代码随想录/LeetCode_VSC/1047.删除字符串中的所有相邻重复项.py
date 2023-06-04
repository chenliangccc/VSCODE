#
# @lc app=leetcode.cn id=1047 lang=python
#
# [1047] 删除字符串中的所有相邻重复项
#


# @lc code=start
class Solution(object):

    def removeDuplicates1(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1.栈
        res = []
        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        return "".join(res)

    def removeDuplicates(self, s):
        # 2.双指针模拟站，不可以用栈的时候备用
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一直换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]

            # 如果发现和前一个相同，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[:slow])


s = 'abbaca'
g = Solution().removeDuplicates(s)
print(g)

# @lc code=end
