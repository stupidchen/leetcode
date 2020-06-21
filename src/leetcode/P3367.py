class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon)
        if n == 0:
            return 0
        m = len(dungeon[0])
        for i in range((n + 1) >> 1):
            tmp = list(reversed(dungeon[i]))
            dungeon[i] = list(reversed(dungeon[n - 1 - i]))
            dungeon[n - 1 - i] = tmp
        f = []
        for i in range(n):
            f.append([0x7fffffff] * m)
        f[0][0] = max(1 - dungeon[0][0], 1)
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0] - dungeon[i][0], 1)
        for i in range(1, m):
            f[0][i] = max(f[0][i - 1] - dungeon[0][i], 1)
        for i in range(1, n):
            for j in range(1, m):
                f[i][j] = max(min(f[i - 1][j], f[i][j - 1]) - dungeon[i][j], 1)
        return f[n - 1][m - 1]


if __name__ == '__main__':
    print(Solution().calculateMinimumHP([[-2,-3],[-5,-10],[10,30]]))