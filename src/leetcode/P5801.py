class Solution:
    def eliminateMaximum(self, dist, speed):
        n = len(dist)
        rt = []
        for i in range(n):
            rt.append((dist[i] - 1) // speed[i] + 1)
        rt = sorted(rt)
        for i in range(n):
            if rt[i] <= i:
                return i
        return n
