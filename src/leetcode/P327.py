import bisect


class Solution:
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]

        ret = 0
        t = [0]
        for i in range(1, n + 1):
            l, r = bisect.bisect_left(t,  p[i] - upper), bisect.bisect_right(t, p[i] - lower)
            ret += r - l
            bisect.insort(t, p[i])
        return ret


# For test only
SI = (([-2, 5, -1], -2, 2),)
SO = (3,)
TM = 'countRangeSum'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
