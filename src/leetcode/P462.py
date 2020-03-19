class Solution:
    def minMoves2(self, nums):
        n = len(nums)
        nums = sorted(nums)
        mid = nums[n // 2]
        return sum(abs(num - mid) for num in nums)
