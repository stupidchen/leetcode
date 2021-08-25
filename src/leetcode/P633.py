from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c)) + 1
        for i in range(n):
            q = c - i * i
            if int(sqrt(q)) ** 2 == q:
                return True
        return False
