import math


def diff_min(x, y):
    if x > y:
        x, y = y, x
    hh_x, mm_x = x.split(':')
    hh_y, mm_y = y.split(':')
    d = (int(hh_y) - int(hh_x)) * 60 + int(mm_y) - int(mm_x)
    return min(d, 1440 - d)


class Solution:
    def findMinDifference(self, timePoints):
        r = math.inf
        timePoints = sorted(timePoints)
        n = len(timePoints)
        for i, p1 in enumerate(timePoints):
            p2 = timePoints[(i + 1) % n]
            r = min(diff_min(p1, p2), r)
        return r


if __name__ == '__main__':
    print(Solution().findMinDifference(["23:59", "00:00"]))
