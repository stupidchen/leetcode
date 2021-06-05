import heapq

MOD = 10 ** 9 + 7


class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        t = [(efficiency[i], i) for i in range(n)]
        t = sorted(t, reverse=True)
        h = []
        s = 0
        m, r = 0, 0
        for i in range(n):
            if len(h) >= k:
                q = heapq.heappop(h)
                s -= q

            heapq.heappush(h, speed[t[i][1]])
            s += speed[t[i][1]]
            p = s * t[i][0]
            if p > m:
                m = p
                r = p % MOD
        return r
