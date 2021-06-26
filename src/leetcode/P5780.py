class Solution:
    def canBeIncreasing(self, nums):
        n = len(nums)
        for i in range(n):
            t = nums[:i] + nums[i + 1:]
            found = True
            for j in range(1, n - 1):
                if t[j] <= t[j - 1]:
                    found = False
                    break
            if found:
                return True
        return False
