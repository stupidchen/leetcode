from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        calculated_path = {}

        for num in nums:
            calculated_path[num] = 0
            t = [num]
            while nums[t[-1]] not in calculated_path:
                t.append(nums[t[-1]])
            s = calculated_path[nums[t[-1]]]
            for i in reversed(t):
                calculated_path[i] = s
                s += 1
        return max(calculated_path.values()) + 1
