class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for r in range(n):
                        if matrix[r][j] != 0:
                            matrix[r][j] = None
                    for c in range(m):
                        if matrix[i][c] != 0:
                            matrix[i][c] = None
        for i in range(n):
            for j in range(m):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
