from math import gcd


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return (x == y == z == 0) or (x + y >= z and z % gcd(x, y) == 0)
