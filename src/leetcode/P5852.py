from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        n = len(mat)
        m = len(mat[0])
        f = {0}
        large = float('inf')
        for i in range(n):
            g = set()
            next_large = float('inf')
            for j in range(m):
                for k in f:
                    t = k + mat[i][j]
                    if t < target:
                        g.add(k + mat[i][j])
                    else:
                        next_large = min(next_large, t)
                next_large = min(next_large, large + mat[i][j])
            f = g
            large = next_large

        ret = large
        for i in f:
            if ret == -1 or abs(target - i) < abs(target - ret):
                ret = i
        return abs(ret - target)


if __name__ == '__main__':
    print(Solution().minimizeTheDifference(
        [[10, 3, 7, 7, 9, 6, 9, 8, 9, 5], [1, 1, 6, 8, 6, 7, 7, 9, 3, 9], [3, 4, 4, 1, 3, 6, 3, 3, 9, 9],
         [6, 9, 9, 3, 8, 7, 9, 6, 10, 6]], 5))
