class Solution:
    def maxScore(self, s: str) -> int:
        def score(x, y):
            return x.count('0') + y.count('1')

        r = 0
        for i in range(len(s) - 1):
            r = max(r, score(s[:i + 1], s[i + 1:]))
        return r


if __name__ == '__main__':
    print(Solution().maxScore('00'))
