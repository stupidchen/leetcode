from collections import defaultdict


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(lambda :0)

        for num in nums:
            d[num] += 1

        if len(d.keys()) < 3:
            return max(d.keys())
        else:
            for i in range(2):
                t = max(d.keys())
                del d[t]
            return max(d.keys())
