class Solution:
    def minDifference(self, nums) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums = sorted(nums)
        ret = nums[-1] - nums[0]
        for i in range(4):
            j = -(3 - i) - 1
            ret = min(nums[j] - nums[i], ret)
        return ret


if __name__ == '__main__':
    print(Solution().minDifference(nums=[1, 5, 0, 10, 14]))
