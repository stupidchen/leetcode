from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums):
        n = len(nums)
        d = defaultdict(lambda: 0)
        for i, v1 in enumerate(nums):
            for j in range(i + 1, n):
                v2 = nums[j]
                d[v1 * v2] += 1
        r = 0
        for k, v in d.items():
            r += v * (v - 1) // 2
        return r * 8
