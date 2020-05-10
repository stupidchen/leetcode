from collections import defaultdict


class Solution:
    def findJudge(self, N, trust):
        d = defaultdict(lambda: 0)
        f = defaultdict(lambda: 0)
        for x, y in trust:
            d[y] += 1
            f[x] += 1

        r = -1
        for i in range(1, N + 1):
            if d[i] == N - 1 and f[i] == 0:
                if r == -1:
                    r = i
                else:
                    return -1
        return r
