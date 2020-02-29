DX = [-1, 0, 1, 1, 1, 0]
DY = [1, 1, 0, -1, 0, 1]


class Solution:
    def findDiagonalOrder(self, matrix):
        r = []
        n = len(matrix)
        if n == 0:
            return r
        m = len(matrix[0])

        def valid(x, y, d):
            tx, ty = x + DX[d], y + DY[d]
            return 0 <= tx < n and 0 <= ty < m

        d = 0
        x, y = 0, 0
        while x < n and y < m:
            r.append(matrix[x][y])
            c = d
            while not valid(x, y, d):
                d = (d + 1) % 6
                if c == d:
                    return r
            x, y = x + DX[d], y + DY[d]
            while d % 3 != 0:
                d = (d + 1) % 6


# For test only
SI = (([
           [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
       ],),)
SO = ([1, 2, 4, 7, 5, 3, 6, 8, 9],)
TM = 'findDiagonalOrder'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
