from collections import defaultdict


class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        f = [0] * n
        m = len(edges)
        d = defaultdict(lambda: [])
        for i in range(m):
            x, y = edges[i]
            d[x].append((y, succProb[i]))
            d[y].append((x, succProb[i]))
        q = [start]
        f[start] = 1
        h = 0
        while h < len(q):
            for pair in d[q[h]]:
                v, p = pair
                if f[v] < f[q[h]] * p:
                    f[v] = f[q[h]] * p
                    q.append(v)
            h += 1
        return f[end]


if __name__ == '__main__':
    print(Solution().maxProbability(3
                                    , [[0, 1], [1, 2], [0, 2]]
                                    , [0.5, 0.5, 0.2]
                                    , 0
                                    , 2))
