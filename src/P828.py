class Solution:
    def uniqueLetterString(self, S):
        s = S
        n = len(s)
        f = {}
        for i in range(n):
            c = s[i]
            if c not in f:
                f[c] = [-1, i]
            else:
                f[c].append(i)

        ans = 0
        modulo = 1000000007
        for k, v in f.items():
            v.append(n)
            for i in range(1, len(v) - 1):
                t = (v[i + 1] - v[i]) * (v[i] - v[i - 1])
                ans = (ans + t) % modulo

        return ans
