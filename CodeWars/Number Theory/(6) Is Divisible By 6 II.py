# https://www.codewars.com/kata/5a1a8b7ec374cbea92000086/train/python
from itertools import product


def is_divisible_by_6(s):
    # your code here
    # if the last digit of s is odd, then the number is not divisible by 6
    if s[-1] in '13579':
        return []
    # replace '*' with '{}' and generate a list of strings
    # that contains the same number of strings '0123456789' as the number of '*' in s
    ss = s.replace('*', '{}')
    return [v for v in (ss.format(*p) for p in product(*(['0123456789']*s.count('*')))) if not int(v) % 6]


def is_divisible_by_6_readable(s):
    # 如果 s 的最后一位是奇数，则直接返回空列表
    if s[-1] in '13579':
        return []

    # 生成所有可能的数字组合
    digits = '0123456789'
    num_digits = s.count('*')
    digit_combinations = product(*([digits] * num_digits))

    # 将 s 中的星号替换为 '{}'，得到新的字符串 ss
    ss = s.replace('*', '{}')

    # 将每个数字组合插入到 ss 中，得到新的字符串，判断是否可以被 6 整除
    result = []
    for combination in digit_combinations:
        num_str = ss.format(*combination)
        if int(num_str) % 6 == 0:
            result.append(num_str)
    return result
