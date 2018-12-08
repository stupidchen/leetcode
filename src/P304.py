class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        if n == 0:
            return
        m = len(matrix[0])

        s = [([0] * (m + 1)) for i in range(n + 1)]

        for i in range(n):
            for j in range(m):
                s[i + 1][j + 1] = (s[i + 1][j] + s[i][j + 1] - s[i][j]) + matrix[i][j]
        self.s = s

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = self.s
        return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1]


if __name__ == '__main__':
    print(NumMatrix([]))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
