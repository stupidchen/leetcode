class Solution:
    def diagonalSort(self, mat):
        n = len(mat)
        m = len(mat[0])
        for i in range(-m + 1, n):
            a = []
            for j in range(n):
                c = j - i
                if 0 <= c < m:
                    a.append(mat[j][c])
            a = sorted(a, reverse=True)
            for j in range(n):
                c = j - i
                if 0 <= c < m:
                    mat[j][c] = a.pop()
        return mat


if __name__ == '__main__':
    print(Solution().diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
