class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        if n == 0:
            return 0
        nums[1] = 1
        for i in range(1, n + 1):
            if 2 <= i * 2 <= n:
                nums[i * 2] = nums[i]
            if 2 <= i * 2 + 1 <= n:
                nums[i * 2 + 1] = nums[i] + nums[i + 1]
        return max(nums)


if __name__ == '__main__':
    print(Solution().getMaximumGenerated(7))
