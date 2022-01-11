from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        r = 0
        for num in nums:
            if len(str(num)) & 1 == 0:
                r += 1
        return r
