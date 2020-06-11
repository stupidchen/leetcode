from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        d = defaultdict(lambda: [])
        for p in prerequisites:
            d[p[0]].append(p[1])

        f = [[False] * n for i in range(n)]

        def solve(s, c):
            if f[s][c]:
                return
            f[s][c] = True
            for i in d[c]:
                solve(s, i)

        for i in range(n):
            solve(i, i)

        r = []
        for q in queries:
            r.append(f[q[0]][q[1]])
        return r
