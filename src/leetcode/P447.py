from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points):
        n = len(points)
        sqr = lambda x: x * x
        ret = 0
        for i in range(n):
            d = defaultdict(lambda: 0)
            for j in range(n):
                if i != j:
                    d[sqr(points[i][0] - points[j][0]) + sqr(points[i][1] - points[j][1])] += 1

            for k in d:
                ret += d[k] * (d[k] - 1)

        return ret


if __name__ == '__main__':
    print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
