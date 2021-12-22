class Solution:
    def maximumSwap(self, num: int) -> int:
        r = num
        s = list(str(num))
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                s[i], s[j] = s[j], s[i]
                r = max(r, int(''.join(s)))
                s[i], s[j] = s[j], s[i]

        return r
    