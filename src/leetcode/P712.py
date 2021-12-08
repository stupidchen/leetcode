from collections import defaultdict


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        f = defaultdict(lambda: 0)
        for i in range(n):
            f[(i + 1, 0)] = f[(i, 0)] + ord(s1[i])

        for j in range(m):
            f[(0, j + 1)] = f[(0, j)] + ord(s2[j])

        for i in range(n):
            for j in range(m):
                f[(i + 1, j + 1)] = min(f[(i, j + 1)] + ord(s1[i]), f[(i + 1, j)] + ord(s2[j]))
                if s1[i] == s2[j]:
                    f[(i + 1, j + 1)] = min(f[(i, j)], f[(i + 1, j + 1)])
        return f[n, m]


if __name__ == '__main__':
    print(Solution().minimumDeleteSum('sea', 'eat'))
