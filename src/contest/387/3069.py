from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1 = [nums[0]]
        a2 = [nums[1]]
        for num in nums[2:]:
            if a1[-1] > a2[-1]:
                a1.append(num)
            else:
                a2.append(num)
        return a1 + a2
