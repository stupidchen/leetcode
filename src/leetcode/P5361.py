from math import sqrt


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        r = radius
        sqr = lambda x: x * x
        d = lambda x1, y1, x2, y2: sqrt(sqr(x1 - x2) + sqr(y1 - y2))
        if d(x1, y1, x_center, y_center) <= r or d(x2, y2, x_center, y_center) <= r:
            return True
        if d(x1, y2, x_center, y_center) <= r or d(x2, y1, x_center, y_center) <= r:
            return True
        if d(x1, (y1 + y2) >> 1, x_center, y_center) <= r or d(x2, (y1 + y2) >> 1, x_center, y_center) <= r:
            return True
        if d((x1 + x2) >> 1, y1, x_center, y_center) <= r or d((x1 + x2) >> 1, y2, x_center, y_center) <= r:
            return True
        i = lambda x, y: x1 <= x <= x2 and y1 <= y <= y2
        if i(x_center + r, y_center) or i(x_center - r, y_center) or i(x_center, y_center + r) or i(x_center, y_center - r):
            return True
        return False


if __name__ == '__main__':
    print(Solution().checkOverlap(1206, -5597, -276, -5203, -1795, -4648, 1721))
    print(Solution().checkOverlap(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1))
    print(Solution().checkOverlap(radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3))
    print(Solution().checkOverlap(radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1))
