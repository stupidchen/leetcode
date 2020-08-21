from math import sqrt

DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


class Solution:
    def getMinDistSum(self, positions):
        n = len(positions)

        def sd(x, y):
            r = 0
            for position in positions:
                r += sqrt((position[0] - x) ** 2 + (position[1] - y) ** 2)
            return r

        x = sum([position[0] for position in positions]) / n
        y = sum([position[1] for position in positions]) / n
        d = 100
        r = sd(x, y)
        while d > 1e-6:
            zoom = True
            for i in range(4):
                tx, ty = x + DX[i] * d, y + DY[i] * d
                tr = sd(tx, ty)
                if tr < r:
                    r = tr
                    x, y = tx, ty
                    zoom = False
            if zoom:
                d /= 10
        return r


if __name__ == '__main__':
    print(Solution().getMinDistSum([[0, 1], [1, 0], [1, 2], [2, 1]]))
