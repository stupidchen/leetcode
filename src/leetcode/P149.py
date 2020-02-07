# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n == 0:
            return 0
        map = {}
        for point in points:
            map[(point.x, point.y)] = map.get((point.x, point.y), 0) + 1
        p = list(map.keys())
        if len(map) == 1:
            return map[p[0]]
        ret = 0
        for i in range(len(p)):
            slopes = {}
            for j in range(i + 1, len(p)):
                dx, dy = p[j][0] - p[i][0], p[j][1] - p[i][1]
                if dx == 0:
                    slope = '$'
                else:
                    slope = dy / dx
                slopes[slope] = slopes.get(slope, 0) + map[p[j]]
            tmp = list(slopes.values())
            ret = max(ret, map[p[i]] + (0 if len(tmp) == 0 else max(tmp)))
        return ret


if __name__ == '__main__':
    data = [Point(1, 1), Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)]
    print(Solution().maxPoints(data))
