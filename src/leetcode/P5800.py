class Solution:
    def buildArray(self, nums):
        r = [0] * len(nums)
        for i, num in enumerate(nums):
            r[i] = nums[nums[i]]
        return r
