class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        d = set()
        for i in range(k):
            for j in range(n - i):
                d.add(s[j: j + i + 1])

        for i in range(1 << (k + 1) - 1):
            f = ''
            t = i
            while t > 0:
                f = chr(48 + (t & 1)) + f
                t = t >> 1

            f = '0' * (k - len(f)) + f
            if f not in d:
                return False
        return True
