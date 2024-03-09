from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a + b > c and b + c > a and a + c > b:
            if a == b == c:
                return 'equilateral'
            elif a == b or b == c or a == c:
                return 'isosceles'
            else:
                return 'scalene'
        else:
            return 'none'
