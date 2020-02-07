import heapq


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        t = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                heapq.heappush(t, matrix[i][j])
        ret = -1
        for i in range(k):
            ret = heapq.heappop(t)
        return ret


if __name__ == '__main__':
    print(Solution().kthSmallest([[1, 2], [1, 3]], 1))
