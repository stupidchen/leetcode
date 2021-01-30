class Solution:
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        r = 0
        for i in range(len(nums) >> 1):
            r += nums[i << 1]
        return r
