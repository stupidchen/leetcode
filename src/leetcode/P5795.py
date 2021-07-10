from collections import defaultdict


class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        edge_set = defaultdict(lambda: defaultdict(lambda: 0xfffffffff))
        for edge in edges:
            x, y, w = edge
            edge_set[x][y] = edge_set[y][x] = min(edge_set[x][y], w)

        f = [[-1] * (maxTime + 1) for i in range(n)]
        g = [(-1, -1)] * n

        q = [(0, 0)]
        f[0][0] = passingFees[0]
        g[0] = (0, passingFees[0])
        h = 0
        while h < len(q):
            c, t = q[h]
            for s, w in edge_set[c].items():
                if t + w <= maxTime and (f[s][t + w] == -1 or passingFees[s] + f[c][t] < f[s][t + w]):
                    f[s][t + w] = passingFees[s] + f[c][t]
                    min_time, min_fee = g[s]
                    if min_time == -1 or (min_time > t + w) or (min_fee > f[s][t + w]):
                        g[s] = (t + w, f[s][t + w])
                        q.append((s, t + w))
            h += 1

        ret = -1
        for i in f[n - 1]:
            if i != -1:
                if ret == -1 or i < ret:
                    ret = i
        return ret
