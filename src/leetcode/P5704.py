class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        p = sorted([(v, i) for i, v in enumerate(nums)])
        l = 0
        r = n - 1
        ret = 0
        for pp in p:
            v, i = pp
            if l <= i <= r:
                t = (r - l + 1) * v
                ret = max(ret, t)
                if i >= k:
                    r = i - 1
                else:
                    l = i + 1
            if not (l <= k <= r):
                break
        return ret
