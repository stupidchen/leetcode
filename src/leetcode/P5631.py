from math import inf
import heapq


class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        f = [-inf] * n
        f[0] = nums[0]
        h = [(-f[0], 0)]
        for i in range(1, n):
            if i > k:
                t = i - k
                while h and h[0][1] < t:
                    heapq.heappop(h)

            f[i] = -h[0][0] + nums[i]
            heapq.heappush(h, (-f[i], i))
        return f[n - 1]


if __name__ == '__main__':
    print(Solution().maxResult(nums=[1, -1, -2, 4, -7, 3], k=2))
