class Solution:
    def maxNonOverlapping(self, nums, target):
        n = len(nums)
        f = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + nums[i]

        r = 0
        d = {0}
        for i in range(n):
            if f[i + 1] - target in d:
                r += 1
                d.clear()
            d.add(f[i + 1])

        return r


if __name__ == '__main__':
    print(Solution().maxNonOverlapping(nums=[-1, 3, 5, 1, 4, 2, -9], target=6))
    print(Solution().maxNonOverlapping(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10))
