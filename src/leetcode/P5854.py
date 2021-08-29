class Solution:
    def minimumDifference(self, nums, k):
        nums = sorted(nums)
        ret = float('inf')
        for i in range(k - 1, len(nums)):
            ret = min(ret, nums[i] - nums[i - k + 1])
        return ret
