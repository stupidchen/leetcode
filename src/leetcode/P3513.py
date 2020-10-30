class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        f = [1] * n
        g = [1] * n
        r = [0] * (n + 1)
        l = 0
        for i in range(n):
            m = 1
            t = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if f[j] + 1 > m:
                        m = f[j] + 1
                        t = g[j]
                    elif f[j] + 1 == m:
                        t += g[j]
            f[i], g[i] = m, t
            r[f[i]] += g[i]
            l = max(l, f[i])
        return r[l]


if __name__ == '__main__':
    print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]))
