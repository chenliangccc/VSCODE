#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=21913
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        b = len(haystack)
        a = len(needle)
        if a == 0:
            return 0
        next = self.get_next(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p + 1] != haystack[j]:
                p = next[p]
            if needle[p + 1] == haystack[j]:
                p += 1
            if p == a - 1:
                return j - a + 1
        return -1

    def get_next(self, a, needle):
        next = ["" for i in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            while k > -1 and needle[k + 1] != needle[i]:
                k = next[k]
            if needle[k + 1] == needle[i]:
                k += 1
            next[i] = k
        return next


# @lc code=end


#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#
