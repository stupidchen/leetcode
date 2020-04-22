from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k):
        r = 0
        s = 0
        d = defaultdict(lambda: 0)
        d[0] += 1
        for num in nums:
            s += num
            t = d[s - k]
            d[s] += 1
            r += t

        return r


if __name__ == '__main__':
    print(Solution().subarraySum(nums=[-1, -1, 1], k=-1))
