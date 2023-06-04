from math import gcd


class DiophantineEquation:

    def extended_euclidean(self, a, b):
        # 欧几里得算法的扩展，求解 ax + by = gcd(a, b) 的一组整数解 (x, y) 以及 gcd(a, b) 的值。
        if a == 0:
            return (b, 0, 1)  # base case
        else:
            gcd, x, y = self.extended_euclidean(b % a, a)  # recursive case
            return (gcd, y - (b // a) * x, x)

    def diophantine_positive(self, a, b, c):
        d = gcd(a, b)
        # 判断是否有解：最大公因数必须整除c才有解
        if c % d != 0:
            raise ValueError("不存在整数解!")
        else:
            a1 = a // d
            b1 = b // d
            c1 = c // d
            # 求a1*x+b1*y=1的整数解
            _, x0, y0 = self.extended_euclidean(a1, b1)
            # 计算获得该方程的一个特解
            x0 *= c1
            y0 *= c1
            print("a1:", a1, "b1:", b1, "x0:", x0, "y0:", y0)

            results = []
            # 通过特解和最大公因数d，求出所有整数解
            for i in range(-abs(c1), abs(c1) + 1):
                x = x0 - i * b1
                y = y0 + i * a1
                if x > 0 and y > 0:
                    results.append((x, y))
            return results

    def solve(self):
        print("请输入二元一次不定方程中a,b,c的值：")
        a, b, c = int(input()), int(input()), int(input())
        results = self.diophantine_positive(a, b, c)
        if len(results) == 0:
            print("无解")
        else:
            print("所有正整数解为：")
            for x, y in results:
                print(f"x={x},y={y}")


# 执行
DiophantineEquation().solve()