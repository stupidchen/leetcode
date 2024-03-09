import math
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (-x[0], x[1]))
        n = len(points)
        res = 0
        for i in range(n):
            leftmost = math.inf
            for j in range(i + 1, n):
                if leftmost > points[j][1] >= points[i][1]:
                    res += 1
                    leftmost = points[j][1]
        return res


if __name__ == '__main__':
    r = Solution().numberOfPairs(points=[[6, 2], [4, 4], [2, 6]])
    # r = Solution().numberOfPairs(points=[[3, 3], [2, 2], [1, 1]])
    print(r)


