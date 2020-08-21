class Solution:
    def numIdenticalPairs(self, nums):
        n = len(nums)
        r = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    r += 1
        return r
