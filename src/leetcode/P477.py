from collections import defaultdict


def last_bit(x):
    return x ^ (x & (x - 1))


class Solution:
    def totalHammingDistance(self, nums):
        d = defaultdict(lambda: 0)
        n = len(nums)
        for num in nums:
            while num > 0:
                t = last_bit(num)
                d[t] += 1
                num -= t
        r = 0
        for v in d.values():
            r += v * (n - v)
        return r
