from math import gcd


class Solution:
    def mirrorReflection(self, p, q):
        g = gcd(p, q)
        return q // g % 2 - p // g % 2 + 1
