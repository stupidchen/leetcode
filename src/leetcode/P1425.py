import heapq


class Solution:
    def constrainedSubsetSum(self, nums, k):
        h = []
        n = len(nums)
        v = [True] * n
        f = [0] * n
        for i in range(n):
            f[i] = nums[i]
            if i - k - 1 >= 0:
                v[i - k - 1] = False
                while h and not v[h[0][1]]:
                    heapq.heappop(h)
            if h:
                f[i] = max(f[i], nums[i] - h[0][0])
            heapq.heappush(h, (-f[i], i))
        return max(f)


if __name__ == '__main__':
    print(Solution().constrainedSubsetSum(nums=[-1, -2, -3], k=3))
