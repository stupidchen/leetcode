from functools import lru_cache

MAXR = 40001


@lru_cache(None)
def hash(point):
    return point[0] * MAXR + point[1]


class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        d = {}
        n = len(points)
        for i in range(n):
            points[i] = tuple(points[i])
            k = hash(points[i])
            d[k] = True
        points.sort(key=hash)
        ret = 0
        for i in range(n):
            for j in range(i, n):
                if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                    continue
                p = (points[i][0], points[j][1])
                q = (points[j][0], points[i][1])
                area = abs(points[i][1] - points[j][1]) * (points[j][0] - points[i][0])
                if ret > area or ret == 0:
                    if hash(p) in d and hash(q) in d:
                        ret = area
        return ret


if __name__ == '__main__':
    print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))