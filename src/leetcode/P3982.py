class Solution:
    def findMaxConsecutiveOnes(self, nums):
        t, r = 0, 0
        for num in nums:
            if num == 0:
                t = 0
            else:
                t += 1
            r = max(t, r)
        return r
