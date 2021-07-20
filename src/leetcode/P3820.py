from random import randint


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori = [n for n in nums]
        self.nums = [n for n in nums]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.ori

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(1, len(self.nums)):
            j = randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()