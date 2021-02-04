from collections import Counter


class Solution:
    def findLHS(self, nums):
        c = Counter(nums)
        r = 0
        for k, v in c.items():
            r = max(r, v + c[k + 1] if k + 1 in c else 0)
            r = max(r, v + c[k - 1] if k - 1 in c else 0)
        return r
