class Solution:
    def waysToMakeFair(self, nums):
        n = len(nums)
        so = [0] * (n + 1)
        se = [0] * (n + 1)
        for i in range(n):
            so[i + 1] = so[i]
            se[i + 1] = se[i]
            if i & 1 == 1:
                so[i + 1] += nums[i]
            else:
                se[i + 1] += nums[i]

        r = 0
        for i in range(n):
            to = se[n] - se[i + 1] + so[i]
            te = so[n] - so[i + 1] + se[i]
            if to == te:
                r += 1
        return r


if __name__ == '__main__':
    print(Solution().waysToMakeFair(nums=[2, 1, 6, 4]))
