MOD = 10 ** 9 + 7


class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        fl = [0] * (n + 1)
        fr = [0] * (n + 1)
        for l, r in requests:
            fr[r + 1] += 1
            fl[l] += 1

        for i in reversed(range(n)):
            fr[i] += fr[i + 1]
            fl[i] += fl[i + 1]

        c = [0] * n
        for i in range(1, n + 1):
            c[i - 1] = max(fr[i] - fl[i], 0)
        nums = sorted(nums)
        c = sorted(c)
        r = 0
        for i in range(n):
            r = (r + nums[i] * c[i]) % MOD
        return r


if __name__ == '__main__':
    print(Solution().maxSumRangeQuery(nums=[1, 8, 5, 5, 2], requests=[[4,4],[3,4],[4,4],[2,4],[0,0]]))
