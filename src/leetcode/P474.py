from collections import Counter


class Solution:
    def findMaxForm(self, strs, m, n):
        f = [[0] * (n + 1) for i in range(m + 1)]

        for s in strs:
            c = Counter(s)
            for i in reversed(range(c['0'], m + 1)):
                for j in reversed(range(c['1'], n + 1)):
                    f[i][j] = max(f[i][j], f[i - c['0']][j - c['1']] + 1)

        return max([max(f[i]) for i in range(m + 1)])


if __name__ == '__main__':
    print(Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
