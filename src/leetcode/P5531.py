class Solution:
    def specialArray(self, nums):
        n = len(nums)
        for i in range(n + 1):
            t = 0
            for num in nums:
                if num >= i:
                    t += 1
            if t == i:
                return t
        return -1
