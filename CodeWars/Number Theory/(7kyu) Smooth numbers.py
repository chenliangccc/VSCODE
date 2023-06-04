# https://www.codewars.com/kata/5b2f6ad842b27ea689000082
from math import sqrt


def is_smooth(n):
    smooth_numbers = []
    smooth_number = {
        2: "power of 2",
        3: "3-smooth",
        5: "Hamming number",
        7: "humble number"
    }
    for i in range(2, int(sqrt(n))+1):
        while n % i == 0:
            n //= i
            smooth_numbers.append(i)
    if n and n != 1:
        smooth_numbers.append(n)
    print(smooth_numbers)
    return smooth_number.get(smooth_numbers[-1], "non-smooth")


print(is_smooth(98))
