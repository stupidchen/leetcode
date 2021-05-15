class Solution:
    def rotateTheBox(self, box):
        n = len(box)
        m = len(box[0])
        r = [['.'] * n for i in range(m)]
        for i in range(n):
            for j in range(m):
                if box[i][j] == '*':
                    r[j][n - i - 1] = '*'
        for j in reversed(range(m)):
            for i in range(n):
                if box[i][j] == '#':
                    x = j
                    k = n - i - 1
                    while x < m and r[x][k] == '.':
                        x += 1
                    r[x - 1][k] = '#'
        return r


if __name__ == '__main__':
    print(Solution().rotateTheBox([['#'] * 500] + [['.'] * 500 for i in range(499)]))
