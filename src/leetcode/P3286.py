class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        m = n
        for i in reversed(range(n)):
            if nums[i] == 0:
                for j in range(i + 1, m):
                    nums[j - 1] = nums[j]
                m -= 1
                nums[m] = 0
