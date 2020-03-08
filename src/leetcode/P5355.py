from collections import defaultdict


class Solution:
    def frogPosition(self, n, edges, t, target):
        f = [-1] * (n + 1)
        q = [-1] * (n + 1)
        l = [False] * (n + 1)
        d = defaultdict(lambda: [])
        for edge in edges:
            x, y = edge
            d[x].append(y)
            d[y].append(x)

        v = [False] * (n + 1)
        f[1] = 1
        q[1] = 0

        def solve(c, p):
            f[c] = p
            m = 0
            for i in d[c]:
                if not v[i]:
                    m += 1
            if m == 0:
                l[c] = True

            if c == target or f[target] != -1:
                return

            v[c] = True
            for i in d[c]:
                if not v[i]:
                    q[i] = q[c] + 1
                    solve(i, p * 1 / m)
            v[c] = False

        solve(1, 1)
        if q[target] > t or q[target] == -1:
            return 0
        if not l[target] and q[target] < t:
            return 0
        return f[target]


if __name__ == '__main__':
    print(Solution().frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=20, target=6))
    print(Solution().frogPosition(9, [[2, 1], [3, 2], [4, 3], [5, 3], [6, 5], [7, 3], [8, 4], [9, 5]], 9, 1))
    print(Solution().frogPosition(8, [[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]], 7, 7))
    print(Solution().frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7))
    print(Solution().frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4))
