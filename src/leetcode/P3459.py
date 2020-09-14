class Solution:
    def rob(self, nums):
        n = len(nums)
        f = [0, 0]
        for i in range(n):
            t = max(f[0], f[1] + nums[i])
            f[1] = f[0]
            f[0] = t
        return max(f)
