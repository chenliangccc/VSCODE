#
# @lc app=leetcode.cn id=858 lang=python
#
# [858] 镜面反射
#

# @lc code=start
class Solution(object):
    def _gcd_(self, a, b):
        if a < b:
            a, b = b, a
        return a if b == 0 else self._gcd_(b, a % b)

    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        """
        数论镜面反射讲解 把光线的运动拆分成水平和垂直两个方向来看，光线都在0到p之间往返运动，并且水平防线的运动速度是垂直方向的p/q倍。我们可以将光线的运动抽象成： 
        设每经过一个时间步，光线在水平方向从一侧跳动到另一侧（即移动p的距离），同时在竖直方向前进q的距离，如果到达了边界就折返。
        由于接收器的位置在水平方向的两侧，因此只有当光线经过整数个时间步后，才有可能到达某一个接收器。而由于接收器的位置也在垂直方向的两侧，因此光线经过k个时间步后，他在竖直方向移动的总距离kq必须是p的倍数，才会碰到垂直方向的两侧。
        1.需要找到最小的k使得kq是p的倍数，并且根据k的奇偶性可以得知光线到达了左侧还是右侧；
        2.根据j=k*q/p的奇偶性可以得知光线到达了上方还是下方，从而得知光线到达的接收器的编号。 
        3.设g=gcd(p,q)为p和q的最大公约数，那么s=p*q/gcd(p,g)是最小的同时整除p和q的数，即s是p和q的最小公倍数。因此k=s/q=p/gcd(p,q)
        """
        # from fractions import gcd
        # 1.求出p、q的最大公约数
        g = self._gcd_(p, q)

        # 2.p/g求出光线移动了k个q，并判断k的奇偶性，偶数在左侧，奇数在右侧
        # s = (p*q)/g；
        # k = s/q = p/g
        k = (p/g) % 2

        # 3.q/g求出
        # j = (k*q/p) = [(p*q/g)/q]*q/p = q/g
        j = (q/g) % 2

        # 4.根据k,j的奇偶性判断光线位置
        # if k and j:
        #     return 1
        # elif j:
        #     return 2
        # else:
        #     return 0
        return 1 if k and j else 2 if j else 0


p, q = 2, 1
g = Solution().mirrorReflection(p, q)
print(g)
# @lc code=end
