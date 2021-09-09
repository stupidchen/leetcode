from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = set([tuple(mine) for mine in mines])
        left = [[0] * n for i in range(n)]
        right = [[0] * n for i in range(n)]
        up = [[0] * n for i in range(n)]
        down = [[0] * n for i in range(n)]
        for i in range(n):
            s = t = 0
            for j in range(n):
                left[i][j] = t
                if (i, j) not in mines_set:
                    t += 1
                else:
                    t = 0
                up[j][i] = s
                if (j, i) not in mines_set:
                    s += 1
                else:
                    s = 0
            s = t = 0
            for j in reversed(range(n)):
                right[i][j] = t
                if (i, j) not in mines_set:
                    t += 1
                else:
                    t = 0
                down[j][i] = s
                if (j, i) not in mines_set:
                    s += 1
                else:
                    s = 0
        ret = 0
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    ret = max(ret, min(up[i][j], down[i][j], left[i][j], right[i][j]) + 1)
        return ret


if __name__ == '__main__':
    print(Solution().orderOfLargestPlusSign(1, [[0, 0]]))
