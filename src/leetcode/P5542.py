from collections import defaultdict

MOD = 10 ** 9 + 7


class Solution:
    def numWays(self, words, target):
        n = len(target)
        len_words = [len(word) for word in words]
        m = len(words)
        t = max(len_words)
        g = [[0] * t for i in range(n)]
        for i in range(t):
            d = defaultdict(lambda: 0)
            for j in range(m):
                if i < len_words[j]:
                    d[words[j][i]] += 1
            for k in range(n):
                g[k][i] = d[target[k]]

        f = [[0] * (t + 1) for i in range(n + 1)]
        f[0][0] = 1
        p = [1] * (t + 1)
        for i in range(1, n + 1):
            tp = [0] * (t + 1)
            for j in range(1, t + 1):
                f[i][j] = p[j - 1] * g[i - 1][j - 1] % MOD
                tp[j] = (tp[j - 1] + f[i][j]) % MOD
            p = tp

        return p[t]


if __name__ == '__main__':
    print(Solution().numWays(words=["abab", "baba", "abba", "baab"], target="abba"))
    print(Solution().numWays(words=["acca", "bbbb", "caca"], target="aba"))
