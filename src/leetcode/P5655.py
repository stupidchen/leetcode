class Solution:
    def largestSubmatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        d = []
        for i in range(n):
            t = []
            for j in range(m):
                if matrix[i][j] == 1:
                    t.append(j)
            d.append(set(t))

        r = 0
        for i in range(n):
            t = d[i]
            m = n - i + 1
            for j in range(i, n):
                t = t & d[j]
                w = len(t)
                a = (j - i + 1) * w
                r = max(a, r)
                if w * m <= r:
                    break
        return r
