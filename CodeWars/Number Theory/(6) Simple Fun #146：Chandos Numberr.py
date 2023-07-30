# https://www.codewars.com/kata/58aa8368ae929ea2e00000d9/train/python
"""The sequence of Chando is an infinite sequence of all Chando's numbers in ascending order.
A number is called Chando's if it is an integer that can be represented as a sum of different positive integer powers of 5.

The first Chando's numbers is 5 (5^1). And the following nth Chando's numbers are:
25  (5^2)
30  (5^1 + 5^2)
125 (5^3)
130 (5^1 + 5^3)
150 (5^2 + 5^3)
...
"""


def nth_chandos_number(n):
    # 将 n 转换为二进制，并在末尾添加一个 0
    binary = f"{bin(n)}0"
    # 将二进制字符串转换为五进制，并返回结果作为整数
    return int(binary[2:], 5)


"""首先将 n 转换为二进制，并在末尾添加一个 0，得到一个二进制字符串。然后，我们将这个二进制字符串转换为五进制，并返回结果作为整数。需要注意的是，我们在转换为五进制之前，将二进制字符串的前两个字符（即 0b）去掉了。"""

print(nth_chandos_number(3))
