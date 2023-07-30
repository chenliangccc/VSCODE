# https://www.codewars.com/kata/56a628758f8d06b59800000f/train/python
'''
A number is self-descriptive when the n'th digit describes the amount n appears in the number.
E.g. 21200:
There are two 0's in the number, so the first digit is 2.
There is one 1 in the number, so the second digit is 1.
There are two 2's in the number, so the third digit is 2.
There are no 3's in the number, so the fourth digit is 0.
There are no 4's in the number, so the fifth digit is 0
Numbers can be of any length up to 9 digits and are only full integers. For a given number derive a function selfDescriptive(num) that returns; true if the number is self-descriptive or false if the number is not.
'''
from collections import Counter


def self_descriptive(num):
    s = [int(a) for a in str(num)]
    cnt = Counter(s)
    print(cnt)
    return all(cnt[i] == b for i, b in enumerate(s))

    # digits = list(str(num))
    # counts = [0] * len(digits)
    # print(counts)

    # # 统计每个数字的出现次数
    # for digit in digits:
    #     if not digit.isdigit():
    #         return False
    #     if int(digit) >= len(counts):
    #         return False
    #     counts[int(digit)] += 1

    # '''
    # # 检查每个数字的出现次数是否与数字本身等
    # for i in range(len(digits)):
    #     if counts[i] != int(digits[i]):
    #         return False
    # return True
    # '''

    # return all(counts[i] == int(digits[i]) for i in range(len(digits)))
