from collections import defaultdict


class Solution:
    def appealSum(self, s: str) -> int:
        r = 0
        f = defaultdict(lambda: -1)
        n = len(s)
        for i, c in enumerate(s):
            r += (i - f[c]) * (n - i)
            f[c] = i
        return r


if __name__ == '__main__':
    print(Solution().appealSum('abbca'))
