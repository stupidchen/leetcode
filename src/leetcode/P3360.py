from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        d = defaultdict(lambda: [])
        for flight in flights:
            x, y, z = flight
            d[x].append((y, z))

        r = [-1]
        f = [[float('inf')] * n for i in range(n)]

        def solve(c, s, p):
            if r[0] != -1 and r[0] <= p:
                return

            if s > K or f[c][s] <= p:
                return

            f[c][s] = p

            if c == dst:
                r[0] = p if r[0] == -1 or r[0] > p else r[0]
                return

            for df in d[c]:
                cn, pn = df
                if cn == dst:
                    solve(cn, s, p + pn)
                else:
                    solve(cn, s + 1, p + pn)

        solve(src, 0, 0)
        return r[0]


if __name__ == '__main__':
    print(Solution().findCheapestPrice(4,
                                       [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
                                       0,
                                       3,
                                       1))
