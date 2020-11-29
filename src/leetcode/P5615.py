import bisect
from collections import Counter


class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        m = n >> 1
        s, min_s, max_s = [], [], []
        for i in range(m):
            x, y = nums[i], nums[n - i - 1]
            s.append(x + y)
            min_s.append(min(x, y))
            max_s.append(max(x, y))

        s = Counter(s)
        min_s.sort()
        max_s.sort()
        r = n
        for t in s.keys():
            equals = s[t]
            increase = bisect.bisect_left(max_s, t - limit)
            decrease = m - bisect.bisect_left(min_s, t)
            r = min(m - equals + increase + decrease, r)

        return r


if __name__ == '__main__':
    print(Solution().minMoves(nums=[1, 2, 4, 3], limit=4))
