from collections import defaultdict


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        d = defaultdict(lambda: 0)
        for i in range(n):
            q = ord(t[i]) - ord(s[i])
            if q < 0:
                q += 26
            d[q] += 1

        for s in d:
            if s != 0 and d[s] > (k - s) // 26 + 1:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canConvertString(s="input", t="ouput", k=9))
    print(Solution().canConvertString(s="abc", t="bcd", k=10))
