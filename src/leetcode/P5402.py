import heapq


class Solution:
    def longestSubarray(self, nums, limit):
        n = len(nums)
        maxh = []
        minh = []
        l = 0
        r = 0
        v = [False] * n

        def pop(h, x):
            p = False
            if len(h) != 0:
                c, i = h[0]
                if c == x:
                    heapq.heappop(h)
                    p = True
            if p:
                while len(h) > 0 and not v[h[0][1]]:
                    heapq.heappop(h)

        d = lambda: -maxh[0][0] - minh[0][0]

        for i in range(n):
            heapq.heappush(maxh, (-nums[i], i))
            heapq.heappush(minh, (nums[i], i))
            v[i] = True

            if d() <= limit:
                r = max(r, i - l + 1)
            else:
                while l <= i and d() > limit:
                    v[l] = False
                    pop(maxh, -nums[l])
                    pop(minh, nums[l])
                    l += 1
        return r


if __name__ == '__main__':
    print(Solution().longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))
    print(Solution().longestSubarray(nums=[8, 2, 4, 7], limit=4))
    print(Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=3))
    print(Solution().longestSubarray(nums=[1, 1, 1], limit=0))
