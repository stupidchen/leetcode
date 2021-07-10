from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        ret = 0
        for i in range(n):
            for j in range(n):
                t = (i + 1) ** 2 + (j + 1) ** 2
                k = sqrt(t)
                if int(k) == k and 1 <= k <= n:
                    ret += 1
        return ret
