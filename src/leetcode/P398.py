import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.a = nums
        self.n = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ret = -1
        m = 0
        for i in range(self.n):
            if self.a[i] == target:
                j = random.randint(0, m)
                if j == 0:
                    ret = i
                m += 1
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)