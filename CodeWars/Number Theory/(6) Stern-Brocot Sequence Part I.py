# https://www.codewars.com/kata/59986011d85bdd7fd7000621/train/python
"""
It starts with [1, 1] and adds two new terms every iteration: nextTerm which is the sum of a previous pair; and termAfterThat which is the second term of this previous pair. Here is how to find those terms:

[1, 1] + [nextTerm: 1 + 1 = 2; termAfterThat: 1] ==> [1, 1, 2, 1]
 ^  ^
Then you shift the pairs with one index in the sequence:
[1, 1, 2, 1] + [1 + 2, 2] ==> [1, 1, 2, 1, 3, 2]
"""


def stern_brocot(n):
    """
    Input:
    n - desired term generated in the Stern-Brocot Sequence

    Return:
    index of first occurence of n
    """
    if n == 1:
        return 0
    lst, i = [1, 1], 0
    while n not in lst[-2:]:
        lst.extend([sum(lst[i:i + 2]), lst[i + 1]])
        i += 1
    return len(lst) - 1 - (lst[-2] == n)
    # return len(lst) - 2
