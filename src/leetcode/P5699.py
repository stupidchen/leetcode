from functools import lru_cache
from math import inf

MOD = 10 ** 9 + 7


class Solution:
    def countRestrictedPaths(self, n: int, edges):
        el = [[] for i in range(n)]
        for edge in edges:
            x, y, w = edge
            x -= 1
            y -= 1
            el[x].append((y, w))
            el[y].append((x, w))

        q = [n - 1]
        h = 0
        d = [inf] * n
        d[n - 1] = 0
        while h < len(q):
            c = q[h]
            for edge in el[c]:
                y, w = edge
                if d[y] > d[c] + w:
                    d[y] = d[c] + w
                    q.append(y)
            h += 1

        p = [set() for i in range(n)]
        q = [n - 1]
        v = [False] * n
        v[0] = True
        h = 0
        while h < len(q):
            c = q[h]
            for edge in el[c]:
                y, w = edge
                if d[y] > d[c]:
                    p[y].add(c)
                    if not v[y]:
                        q.append(y)
                        v[y] = True
            h += 1

        @lru_cache(maxsize=None)
        def f(x):
            if x == n - 1:
                return 1
            r = 0
            for pp in p[x]:
                r = (r + f(pp)) % MOD
            return r

        return f(0)


if __name__ == '__main__':
    print(Solution().countRestrictedPaths(n=5, edges=[[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1],
                                                      [5, 4, 10]]))
