class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        ret = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    ret += 1
        for i in range(n):
            ret += max(grid[i]) << 1
            t = 0
            for j in range(n):
                t = max(grid[j][i], t)
            ret += t << 1
        return ret


if __name__ == '__main__':
    print(Solution().projectionArea([[1,2],[3,4]]))
