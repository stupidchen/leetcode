class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        f, g = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + (1 if S[i] == '1' else 0)
        for i in reversed(range(n)):
            g[i] = g[i + 1] + (1 if S[i] == '0' else 0)
        ret = f[0] + g[0]
        for i in range(n):
            ret = min(ret, f[i] + g[i])
            if g[i] == n - i:
                ret = min(ret, f[i + 1])
            if f[i] == i:
                ret = min(ret, g[i])
        return ret
