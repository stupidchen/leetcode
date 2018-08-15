class Solution:
    def solve(self, nums):
        n = len(nums)
        f = [0] * n
        l = 0
        ret = 0
        for i in range(n - 1):
            if i <= 1:
                f[i] = nums[i]
            else:
                f[i] = max(l + nums[i], f[i - 1])
            ret = max(ret, f[i])
            if i >= 1:
                l = max(l, f[i - 1])
        return ret

    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        t1 = self.solve(nums)
        nums.reverse()
        t2 = self.solve(nums)
        return max(t1, t2)


if __name__ == '__main__':
    print(Solution().rob([4, 1, 2]))
