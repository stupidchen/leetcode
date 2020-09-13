class Solution:
    def numSpecial(self, mat):
        n = len(mat)
        m = len(mat[0])
        r = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    t = 0
                    for ti in range(n):
                        t += mat[ti][j]
                    for tj in range(m):
                        t += mat[i][tj]
                    if t == 2:
                        r += 1
        return r


if __name__ == '__main__':
    print(Solution().numSpecial([[1]]))
