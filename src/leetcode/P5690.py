from math import inf

N = 2 * 10 ** 4 + 1


class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        r = inf
        for base in baseCosts:
            f = [False] * (N + 1)
            f[0] = True

            for i in reversed(range(base, N + 1)):
                t = i - base
                f[i] = f[t] or f[i]

            f[0] = False

            for topping in toppingCosts:
                for i in reversed(range(topping, N + 1)):
                    t = i - topping
                    f[i] = f[t] or f[i]

                    m = topping * 2
                    t = i - m
                    if t >= 0:
                        f[i] = f[t] or f[i]

            for i in range(N):
                if f[i] and (abs(i - target) < abs(r - target)):
                    r = i
        return r


if __name__ == '__main__':
    print(Solution().closestCost(baseCosts=[10], toppingCosts=[1], target=1))
