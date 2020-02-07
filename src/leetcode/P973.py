class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points = sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:K]

if __name__ == '__main__':
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
