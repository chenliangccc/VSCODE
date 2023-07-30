"""https://www.codewars.com/kata/591392af88a4994caa0000e0/train/python
We have a set of consecutive numbers from 1 to n. We want to count all the subsets that do not contain consecutive numbers. E.g.

If our set S1 is equal to [1,2,3,4,5] The subsets that fulfill these property are:
[],[1],[2],[3],[4],[5],[1,3],[1,4],[1,5],[2,4],[2,5],[3,5],[1,3,5]

A total of 12 subsets,doesn't include the empty subset.

From the set S2 equals to[1,2,3], it is obvious that we have only 4 subsets and are:
[],[1],[2],[3],[1,3]
"""


def f(n):  # f(n) = f(n-2) + f(n-3) - 1; e.g.f(0)=1, f(1)=2
    # your magic here
    a, b = 3, 5
    for _ in range(n):  # 计算斐波那契数列
        a, b = b, a + b
        return a - 1


"""解析:
从n个元素中选择的子集可以被编码为长度为n的二进制字符串。例如，1101可以表示从{1,2,3,4}中选择元素{1,2,4}。
现在，如果你不想要"连续的元素"在你的子集中，那么在二进制表示方面对应什么呢？意思是：你的二进制数不能有任何连续的1。

那么，在没有连续1s的情况下，长度为n的二进制数有多少个呢？假设答案是buzz(n)。如果我们长度为n的二进制数以一个1开头，则下一个数字不能是1，必须是0，然后我们可以附加任何长度为n-2且没有连续1s（其中有buzz(n-2)个）的二进制数。
如果我们长度为n的二进制数以一个0开头 ，则我们可以附加任何长度为 n-1 而没有连续的元素{buzz(n-3)} 。所以基本上
kata题目得出结论：buzz(n) = buzz(n-2)+ buzz(n-3)，并且初始条件是buzz(2)=3、buzz(3)=5。
如果您曾经实现过斐波那契数列，这应该看起来很熟悉。kata题目不包括空子集作为有效的解，所以必须在最后删除一个子集以获得最终答案。"""

print(f(5))
