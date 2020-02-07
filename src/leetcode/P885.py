DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        x = r0
        y = c0
        d = 0
        ret = []
        v = 0
        n = R * C
        visit = {}
        first = True
        while v < n:
            if 0 <= x < R and 0 <= y < C:
                v += 1
                ret.append([x, y])
            visit[(x, y)] = True
            td = (d + 1) % 4
            if not first and (x + DX[td], y + DY[td]) not in visit:
                d = td
                x = DX[td] + x
                y = DY[td] + y
            else:
                x = DX[d] + x
                y = DY[d] + y
                first = False
        return ret

if __name__ == '__main__':
    print(Solution().spiralMatrixIII(1, 4, 0, 0))
