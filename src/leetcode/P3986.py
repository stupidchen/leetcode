class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        for i in range(3, n + 1):
            a.append(a[-3] + a[-2] + a[-1])
        return a[n]
