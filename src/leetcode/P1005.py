from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        for i in range(min(n, k)):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            else:
                break
        if k & 1 == 1:
            if nums[i] > nums[i - 1]:
                nums[i - 1] = -nums[i - 1]
            else:
                nums[i] = -nums[i]
        return sum(nums)
