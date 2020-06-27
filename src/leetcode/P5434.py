class Solution:
    def longestSubarray(self, nums):
        def init():
            return [[0, 0] for i in range(2)]

        n = len(nums)
        f = [init() for i in range(n + 1)]
        r = 0
        for i in range(n):
            if nums[i] == 1:
                f[i + 1][1][0] = f[i][1][0] + 1
                f[i + 1][1][1] = f[i][1][1] + 1
            else:
                f[i + 1][1][1] = f[i][1][0]
            r = max(r, max(f[i + 1][1]), max(f[i + 1][0]))

        if all(num == 1 for num in nums):
            r -= 1
        return r


if __name__ == '__main__':
    print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
