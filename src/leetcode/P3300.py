class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        f = [1] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] * nums[i]

        q = [1] * (n + 1)
        for i in reversed(range(n)):
            q[i] = q[i + 1] * nums[i]

        r = []
        for i in range(n):
            r.append(f[i] * q[i + 1])
        return r


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
