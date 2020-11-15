import bisect


class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]

        s = p[n]
        r = -1
        for i in reversed(range(n + 1)):
            k = x - (s - p[i])
            if k < 0:
                break
            t = bisect.bisect_left(p, k, 0, i)
            if p[t] == k:
                v = t + n - i
                if r == -1 or v < r:
                    r = v
        return r


if __name__ == '__main__':
    print(Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5))
    print(Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))
