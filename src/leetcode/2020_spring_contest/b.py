from collections import defaultdict


class Solution:
    def numWays(self, n, relation, k):
        d = defaultdict(lambda: [])
        for x, y in relation:
            d[x].append(y)

        q = [(0, 0)]
        f = [[0] * (k + 1) for i in range(n)]
        g = [[False] * (k + 1) for i in range(n)]
        f[0][0] = 1
        h = 0
        while h < len(q):
            cv, ct = q[h]
            g[cv][ct] = True
            if ct < k:
                for v in d[cv]:
                    f[v][ct + 1] += f[cv][ct]
                    if not g[v][ct + 1]:
                        q.append((v, ct + 1))
                        g[v][ct + 1] = True
            h += 1

        return f[n - 1][k]


if __name__ == '__main__':
    print(Solution().numWays(n = 3, relation = [[0,2],[2,1]], k = 2))
