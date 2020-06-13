class Solution:
    def shuffle(self, nums, n):
        r = []
        for i in range(n):
            r.append(nums[i])
            r.append(nums[i + n])
        return r
