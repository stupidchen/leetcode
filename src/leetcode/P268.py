class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        s = 0
        for num in nums:
            s += num
        return ((n * (n + 1)) >> 1) - s