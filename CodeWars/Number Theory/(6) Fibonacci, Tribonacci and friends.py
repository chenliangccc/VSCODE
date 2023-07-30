# https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python
def Xbonacci(signature, n):
    # your code here
    size = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-size:]))
    return signature[:n]
