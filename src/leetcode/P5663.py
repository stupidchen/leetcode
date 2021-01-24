from heapq import heappush, heappop


class Solution:
    def kthLargestValue(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])
        h = []
        s = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                s[i + 1][j + 1] = s[i + 1][j] ^ s[i][j + 1] ^ s[i][j] ^ matrix[i][j]
        for i in range(n):
            for j in range(m):
                t = s[i + 1][j + 1]
                heappush(h, t)
                if len(h) > k:
                    heappop(h)
        return h[0]


if __name__ == '__main__':
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 1))
