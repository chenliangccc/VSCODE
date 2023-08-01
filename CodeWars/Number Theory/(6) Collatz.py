# https://www.codewars.com/kata/5286b2e162056fd0cb000c20/train/python
def collatz(n):
    if n == 1:
        return "1"
    elif n % 2 == 0:
        return str(n) + "->" + collatz(n // 2)

    else:
        return str(n) + "->" + collatz(3 * n + 1)


print(collatz(3))
