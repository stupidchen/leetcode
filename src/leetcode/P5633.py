class Solution:
    def totalMoney(self, n: int) -> int:
        r = 0
        t = 0
        for i in range(n):
            if i % 7 == 0:
                t = i // 7 + 1
            else:
                t += 1
            r += t
        return r
