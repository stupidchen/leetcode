class Solution:
    def countNegatives(self, grid):
        r = 0
        for row in grid:
            for num in row:
                if num < 0:
                    r += 1
        return r
