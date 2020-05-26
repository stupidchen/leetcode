class Solution:
    def findMaxLength(self, nums):
        n = len(nums)
        f = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + (1 if nums[i] == 1 else -1)

        d = {0: -1}
        for i in range(n):
            d[f[i + 1]] = i
        r = d[0] + 1
        for i in range(n):
            r = max(d[f[i + 1]] - i, r)
        return r
