from collections import defaultdict, Counter


class Solution:
    def maxNumOfSubstrings(self, s: str):
        hi = defaultdict(lambda: -1)
        lo = defaultdict(lambda: float('inf'))
        n = len(s)
        for i in range(n):
            if i > hi[s[i]]:
                hi[s[i]] = i
            if i < lo[s[i]]:
                lo[s[i]] = i

        pd = [defaultdict(lambda: 0)] * (n + 1)
        for i in range(n):
            pd[i + 1] = pd[i].copy()
            pd[i + 1][s[i]] += 1

        def cpd(x, y):
            ret = pd[y + 1].copy()
            for kk, vv in pd[x].items():
                ret[kk] -= vv
                if ret[kk] == 0:
                    del ret[kk]
            return ret

        d = defaultdict(lambda: [])
        for k in hi:
            left, right = lo[k], hi[k]
            ch = {k}
            while True:
                t = cpd(left, right)
                cc = set(t.keys())
                if cc == ch:
                    break
                dd = cc - ch
                for c in dd:
                    left = min(left, lo[c])
                    right = max(right, hi[c])
                ch = cc
            d[right].append(left)

        f = [(0, 0)] * (n + 1)
        g = [-1] * (n + 1)
        for i in range(n):
            k, b = f[i]
            k -= 1
            for j in range(len(d[i])):
                le = d[i][j]
                if f[le][0] > k or (f[le][0] == k and f[le][1] + (i - le + 1) < b):
                    k = f[le][0]
                    g[i + 1] = j
                    b = f[le][1] + (i - le + 1)
            f[i + 1] = (k + 1, b)

        r = []
        m = n
        while m > 0:
            if g[m] != -1:
                r.append(s[d[m - 1][g[m]]: m])
                m = d[m - 1][g[m]]
            else:
                m = m - 1
        return r


if __name__ == '__main__':
    print(Solution().maxNumOfSubstrings('ababa'))
