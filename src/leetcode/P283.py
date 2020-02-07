class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        t = 0
        for i in range(n):
            if nums[i] != 0:
                nums[t] = nums[i]
                t += 1
        for i in range(t, n):
            nums[i] = 0
