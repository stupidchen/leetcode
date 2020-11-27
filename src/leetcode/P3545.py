class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s & 1 == 1:
            return False

        s >>= 1
        f = [False] * (s + 1)
        f[0] = True
        for num in nums:
            for i in reversed(range(num, s + 1)):
                f[i] = f[i] or f[i - num]
        return f[s]
