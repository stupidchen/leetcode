class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()

        def f(x):
            r = 0
            while x > 0:
                t = x % 10
                r += t * t
                x //= 10
            return r

        while n not in d:
            d.add(n)
            n = f(n)
        return n == 1
