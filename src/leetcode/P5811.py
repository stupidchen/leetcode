MOD = 10 ** 9 + 7


class Solution:
    def colorTheGrid(self, m, n):
        c = 3 ** m

        def color(x):
            ret = [0] * m
            for i in range(m):
                ret[i] = x % 3
                x = x // 3
            return ret

        colors = []
        for i in range(c):
            cc = color(i)
            valid = True
            for j in range(m - 1):
                if cc[j] == cc[j + 1]:
                    valid = False
                    break
            if valid:
                colors.append(cc)

        t = len(colors)
        last = []
        for i in range(t):
            last_i = []
            for j in range(t):
                valid = True
                for d in range(m):
                    if colors[i][d] == colors[j][d]:
                        valid = False
                        break
                if valid:
                    last_i.append(j)
            last.append(last_i)

        f = [1] * t
        for i in range(n - 1):
            nf = [0] * t
            for j in range(t):
                for k in last[j]:
                    nf[j] = (nf[j] + f[k]) % MOD
            f = nf
        ret = 0
        for i in range(t):
            ret = (ret + f[i]) % MOD
        return ret


if __name__ == '__main__':
    print(Solution().colorTheGrid(5, 1000))
