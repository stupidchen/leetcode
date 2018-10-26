class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num in d:
                return num
            else:
                d[num] = True
