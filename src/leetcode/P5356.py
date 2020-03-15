class Solution:
    def luckyNumbers(self, matrix):
        r = []
        for row in matrix:
            m = min(row)
            for i in range(len(row)):
                if row[i] == m:
                    t = 0
                    for j in range(len(matrix)):
                        t = max(matrix[j][i], t)
                    if t == row[i]:
                        r.append(t)
        return r


if __name__ == '__main__':
    print(Solution().luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
