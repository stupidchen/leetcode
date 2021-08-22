from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        x_set = set()
        y_set = set()
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            x_set.add(x1)
            x_set.add(x2)
            y_set.add(y1)
            y_set.add(y2)

        sorted_x = list(sorted(x_set))
        sorted_y = list(sorted(y_set))
        x_dict = {}
        for i, v in enumerate(sorted_x):
            x_dict[v] = i
        y_dict = {}
        for i, v in enumerate(sorted_y):
            y_dict[v] = i

        n = len(sorted_x)
        m = len(sorted_y)
        bitmap = [[False] * m for i in range(n)]
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            x1, y1, x2, y2 = x_dict[x1], y_dict[y1], x_dict[x2], y_dict[y2]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    bitmap[i][j] = True

        ret = 0
        for i in range(n):
            for j in range(m):
                if bitmap[i][j]:
                    w = sorted_x[i + 1] - sorted_x[i]
                    h = sorted_y[j + 1] - sorted_y[j]
                    ret = (ret + w * h) % MOD
        return ret


if __name__ == '__main__':
    print(Solution().rectangleArea([[0, 0, 100, 100]]))
