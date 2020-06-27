from collections import defaultdict


def last_bit(x):
    return x & (x ^ (x - 1))


def n1(x):
    r = 0
    while x > 0:
        x -= last_bit(x)
        r += 1
    return r


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies, k: int):
        r = [float('inf')]
        g = defaultdict(lambda: [])
        for dependency in dependencies:
            x, y = dependency
            x -= 1
            y -= 1
            g[x].append(y)

        def solve(v, d, s):
            if s >= r[0]:
                return

            if all(v):
                r[0] = s
                return

            c = []
            left = 0
            for i in range(n):
                if not v[i]:
                    left += 1
                    if d[i] == 0:
                        c.append(i)

            if (left - 1) // k + s >= r[0]:
                return

            m = len(c)
            for i in range((1 << m)):
                if n1(i) == min(m, k):
                    t = []
                    for j in range(m):
                        if i | (1 << j) == i:
                            t.append(c[j])
                    for j in t:
                        for h in g[j]:
                            d[h] -= 1
                        v[j] = True
                    solve(v, d, s + 1)
                    for j in t:
                        for h in g[j]:
                            d[h] += 1
                        v[j] = False

                    if (left - 1) // k + s + 1 >= r[0]:
                        return

        d = [0] * n
        for i in range(n):
            for j in g[i]:
                d[j] += 1
        solve([False] * n, d, 0)
        return r[0]


if __name__ == '__main__':
    print(Solution().minNumberOfSemesters(n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2))
