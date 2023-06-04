# 计算最大公因数
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# 计算最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


# 欧几里得算法的扩展，求解 ax + by = gcd(a, b) 的一组整数解 (x, y) 以及 gcd(a, b) 的值。
# 这个算法使用递归实现。当a等于0时，返回(b, 0, 1)作为基本情况。否则，递归调用extended_euclidean(b % a, a)来计算gcd、x和y。然后返回(gcd, y - (b // a) * x, x)。
# 这个算法的正确性基于贝祖等式（Bézout’s identity）：对于任意整数a和b，它们的最大公约数gcd(a, b)可以表示为ax + by的形式，其中x和y是整数。扩展欧几里得算法利用了这一性质来求解x和y。
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)  # base case
    else:
        gcd, x, y = extended_gcd(b % a, a)  # recursive case
        return (gcd, y - (b // a) * x, x)


"""这个式子是通过数学推导得出的。扩展欧几里得算法的目标是求解方程ax + by = gcd(a, b)的一组整数解x和y。我们可以将这个方程转化为另一个形式，以便递归求解。

首先，我们可以将b除以a，得到商q和余数r，即b = qa + r。将这个等式代入原方程，得到a(x) + (qa + r)(y) = gcd(a, b)。展开后得到ax + qay + ry = gcd(a, b)，即ax + qay = gcd(a, b) - ry。

由于gcd(a, b) = gcd(b % a, a)，所以我们可以将原方程转化为求解方程(b % a)(x’) + a(y’) = gcd(b % a, a)的一组整数解x’和y’。然后我们可以递归调用扩展欧几里得算法来求解x’和y’。

现在我们需要从x’和y’推导出原方程的解x和y。注意到b % a = b - qa = r，所以ry = gcd(a, b) - ax - qay，即y = (gcd(a, b) - ax) / (r + qa)。由于r + qa = b，所以y = (gcd(a, b) - ax) / b。

因此，我们可以通过递归调用扩展欧几里得算法来求解x’和y’，然后根据上面的推导计算出原方程的解x和y。具体来说，x = y’，y = x’ - (b // a) * y’。"""

print(extended_gcd(111, -321))
