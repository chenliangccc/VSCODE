# https://www.codewars.com/kata/56fcc393c5957c666900024d
from math import ceil,sqrt

def clockwise(arr):
    # 顺时针旋转矩阵函数
    # zip(*iterables, strict=False): 在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。
    # 对于每一行，将元素从每个迭代器中取出，组成一个元组，然后将元组转换为列表，并反转该列表。
    # 最终返回旋转后的矩阵。
    return [list(reversed(row)) for row in zip(*arr)]


def counterclockwise(arr):
    # 逆时针旋转矩阵函数
    # 将矩阵转置，然后将每一行反转，最终返回逆时针旋转后的矩阵。
    return [list(row) for row in reversed(list(zip(*arr)))]


def code(s):     
    """该函数将输入字符串按照顺时针方向旋转，然后按行拼接成字符串，每一行之间使用换行符分隔。

    Args:
        s (strings): 字符串

    Returns:
        string: 加密后的字符串
    """
    # math.ceil(x): 返回 x 的向上取整，即大于或等于 x 的最小的整数。
    # 确定矩阵的大小，使得矩阵的行数和列数都不小于输入字符串的长度。
    n = ceil(sqrt(len(s)))
    # str.ljust(width[, fillchar]): 返回长度为 width 的字符串，原字符串在其中靠左对齐。
    # 使用指定的 fillchar 填充空位（默认使用 ASCII 空格符）。
    # 将输入字符串填充到长度为 n*n 的倍数，并添加填充字符 chr(11)。
    s = s.ljust(n * n, chr(11))
    # 将填充后的字符串按照长度为 n 的子串划分，形成矩阵。
    square = [s[n*i:n*(i+1)] for i in range(n)]
    # 将矩阵顺时针旋转，并将结果按行拼接成字符串，每一行之间使用换行符分隔。
    return '\n'.join(''.join(row) for row in clockwise(square))


def decode(s):      # 解密函数
    # 将输入字符串按换行符分隔，并将每一行转换为列表。
    # 对列表进行逆时针旋转，然后将旋转后的矩阵按行拼接成字符串。
    # 使用 strip(chr(11)) 去除字符串末尾可能存在的填充字符 chr(11)。
    return ''.join(''.join(row) for row in counterclockwise(s.split('\n'))).strip(chr(11))

s = "I love you my baby"
print(code(s))