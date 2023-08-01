# https://www.codewars.com/kata/537ba77315ddd92659000fec
def check_goldbach(number):
    if number < 4 or number % 2:
        return []
    for i in range(2, number // 2 + 1):
        if isPrime(i) and isPrime(number - i):
            return [i, number - i]
    return []


def isPrime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


number = 100
result = check_goldbach(number)
print(f"The two prime numbers that add up to {number} are {result[0]} and {result[1]}")
