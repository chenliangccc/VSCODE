# Sum of (2^k * k^2) (for k=0 to n)
# http://lbv-pc.blogspot.com/2012/07/summation-of-polynomials.html
M = 10**9 + 7


def f(n):
    # g(x) = sum(x^k, k = 0..n)
    # Then sum(k^2 * x^2, k = 0..n) = x^2 g''(x) + x(g'(x) - 1) + x
    # g'(2) = (n - 1) * 2^n + 1
    # g''(2) = ...
    def g2(n): return (n * n * pow(2, n, M) - 3 * n *
                       pow(2, n, M) + pow(2, n + 2, M) - 4) * pow(2, M - 2, M)

    def g1(n): return pow(2, n, M) * (n - 1) + 1
    return (4 * g2(n) + 2 * (g1(n) - 1) + 2) % M
    # WolframAlpha:
    # return 2 * (pow(2, n, M) * (n * n - 2 * n + 3) - 3) % M
