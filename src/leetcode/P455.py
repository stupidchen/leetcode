class Solution:
    def findContentChildren(self, g, s):
        g, s = sorted(g), sorted(s)
        n, m = len(g), len(s)
        i, j = 0, 0
        r = 0
        while i < n and j < m:
            if s[j] >= g[i]:
                r += 1
                i += 1
            j += 1
        return r


if __name__ == '__main__':
    print(Solution().findContentChildren([1, 2], [1, 2, 3]))
