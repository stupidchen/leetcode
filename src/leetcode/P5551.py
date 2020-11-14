class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i]
            if s[i] == 'a':
                f[i + 1] += 1
        for i in reversed(range(n)):
            g[i] = g[i + 1]
            if s[i] == 'a':
                g[i] += 1
        r = n
        for i in range(n + 1):
            r = min(r, i - f[i] + g[i])
        return r


if __name__ == '__main__':
    print(Solution().minimumDeletions('bab'))
