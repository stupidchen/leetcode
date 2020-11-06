import math


class Solution:
    def smallestDivisor(self, nums, threshold):
        n = len(nums)

        def calculate(x):
            t = 0
            for num in nums:
                t += math.ceil(num / x)
            return t

        l, r = 1, max(nums)
        ret = -1
        while l <= r:
            mid = (l + r) >> 1
            if calculate(mid) <= threshold:
                r = mid - 1
                ret = mid
            else:
                l = mid + 1
        return ret

