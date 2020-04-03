class Solution:
    def maxSubArray(self, nums):
        r = 0
        f = 0
        for i in range(len(nums)):
            if r + nums[i] > 0:
                r = r + nums[i]
            else:
                r = 0
            f = max(f, r)
        if all([x < 0 for x in nums]):
            return max(nums)
        return f


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, -3, -1]))
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
