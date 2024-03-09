import math
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        sorted_points = list(map(lambda y: (-y[0], y[1]), sorted(map(lambda x: (-x[0], x[1]), points))))
        n = len(points)
        res = 0
        for i in range(n):
            alice_x, alice_y = sorted_points[i]
            right_bound = [math.inf]
            for j in range(i + 1, n):
                y = sorted_points[j][1]
                if sorted_points[j][0] != sorted_points[j - 1][0]:
                    right_bound.append(math.inf)
                if y >= alice_y:
                    right_bound[-1] = min(right_bound[-1], sorted_points[j][1])

            rightmost = math.inf
            for right in right_bound:
                if right < rightmost:
                    res += 1
                    rightmost = right
        return res


if __name__ == '__main__':
    # r = Solution().numberOfPairs(points=[[6, 2], [4, 4], [2, 6]])
    r = Solution().numberOfPairs(points=[[3, 3], [2, 2], [1, 1]])
    print(r)
