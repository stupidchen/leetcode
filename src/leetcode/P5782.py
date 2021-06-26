class Solution:
    def maxAlternatingSum(self, nums):
        last = [0, 0]
        current = [0, 0]
        for num in nums:
            current[0] = last[1] + num
            current[1] = last[0] - num
            last[0] = max(last[0], current[0])
            last[1] = max(last[1], current[1])
        return max(last)
