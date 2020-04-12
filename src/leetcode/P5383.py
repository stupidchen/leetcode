MOD = 10 ** 9 + 7


class Solution:
    def numOfWays(self, n: int) -> int:
        def init():
            r = []
            for i in range(3):
                r.append([])
                for j in range(3):
                    r[-1].append([])
                    for k in range(3):
                        r[-1][-1].append(0)
            return r

        f = [init(), init()]
        for t in range(n):
            p = t & 1
            q = 1 - p
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if i == j or j == k:
                            f[p][i][j][k] = 0
                            continue
                        else:
                            f[p][i][j][k] = 0
                            if t == 0:
                                f[p][i][j][k] = 1
                            for qi in range(3):
                                if qi != i:
                                    for qj in range(3):
                                        if qj != j:
                                            for qk in range(3):
                                                if qk != k:
                                                    f[p][i][j][k] = (f[p][i][j][k] + f[q][qi][qj][qk]) % MOD

        r = 0
        p = 1 - (n & 1)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    r = (r + f[p][i][j][k]) % MOD
        return r


if __name__ == '__main__':
    print(Solution().numOfWays(5000))
