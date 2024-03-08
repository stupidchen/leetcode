from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        i = 0
        res = 0
        for num in nums:
            i += num
            if i == 0:
                res += 1
        return res


