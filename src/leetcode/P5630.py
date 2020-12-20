from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums):
        l = 0
        r = 0
        d = defaultdict(lambda: 0)
        s = 0
        for i, v in enumerate(nums):
            s += v
            d[v] += 1
            while d[nums[l]] > 1 or d[v] > 1:
                d[nums[l]] -= 1
                s -= nums[l]
                l += 1
            r = max(r, s)
        return r


if __name__ == '__main__':
    print(Solution().maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))
