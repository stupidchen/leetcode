class Solution:
    def findCenter(self, edges):
        n = len(edges) + 1
        d = [0] * n
        for edge in edges:
            x, y = edge
            x -= 1
            y -= 1
            d[x] += 1
            d[y] += 1

        for i in range(n):
            if d[i] == n - 1:
                return i + 1
