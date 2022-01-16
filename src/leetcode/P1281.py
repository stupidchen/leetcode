class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n > 0:
            d = n % 10
            s += d
            p *= d
            n //= 10
        return p - s
