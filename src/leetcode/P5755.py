class Solution:
    def minPairSum(self, nums):
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        ret = nums[l] + nums[r]
        while l < r:
            ret = max(ret, nums[l] + nums[r])
            l += 1
            r -= 1
        return ret
