from functools import lru_cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        m, n = n, m
        t = 3 ** m

        def init():
            r = []
            for i in range(introvertsCount + 1):
                r.append([[-1] * t for j in range(extrovertsCount + 1)])
            return r

        @lru_cache(maxsize=None)
        def c32i(x):
            r = [0] * m
            i = m - 1
            while x != 0:
                r[i] = x % 3
                i -= 1
                x = x // 3
            return r


        @lru_cache(maxsize=None)
        def get_h(x, y):
            kx = c32i(x)
            ky = c32i(y)
            r = 0
            for i in range(m):
                if kx[i] == 1 and ky[i] != 0:
                    r -= 30

                if kx[i] == 2 and ky[i] != 0:
                    r += 20

                if ky[i] == 1:
                    r += 120
                    if i > 0 and ky[i - 1] != 0:
                        r -= 30
                    if i < m - 1 and ky[i + 1] != 0:
                        r -= 30
                    if kx[i] != 0:
                        r -= 30

                if ky[i] == 2:
                    r += 40
                    if i > 0 and ky[i - 1] != 0:
                        r += 20
                    if i < m - 1 and ky[i + 1] != 0:
                        r += 20
                    if kx[i] != 0:
                        r += 20

            return r

        @lru_cache(maxsize=None)
        def get_n(x):
            k = c32i(x)
            ri, re = 0, 0
            for i in range(m):
                if k[i] == 1:
                    ri += 1
                elif k[i] == 2:
                    re += 1
            return ri, re

        f = [init() for i in range(n + 1)]
        f[0][introvertsCount][extrovertsCount][0] = 0
        r = 0
        for i in range(n):
            for ii in range(introvertsCount + 1):
                for ie in range(extrovertsCount + 1):
                    for j in range(t):
                        p = f[i][ii][ie][j]
                        if p != -1:
                            for nj in range(t):
                                ni, ne = get_n(nj)
                                if ii - ni >= 0 and ie - ne >= 0:
                                    h = get_h(j, nj)
                                    c = f[i + 1][ii - ni][ie - ne][nj]
                                    nh = p + h
                                    if c == -1 or c < nh:
                                        r = max(r, nh)
                                        f[i + 1][ii - ni][ie - ne][nj] = nh
        return r


if __name__ == '__main__':
    f = {}
    for i in range(1, 6):
        for j in range(1, 6):
            t = i * j
            for ii in range(min(i * j, 6) + 1):
                for jj in range(min(i * j, 6) + 1):
                    print('Cal {}, {}, {}, {}'.format(i, j, ii, jj))
                    f[(i, j, ii, jj)] = Solution().getMaxGridHappiness(i, j, ii, jj)
    print(f)
