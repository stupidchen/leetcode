class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while True:
                t = nums[i] - 1
                if 0 <= t < n and t != i and nums[i] != nums[t]:
                    nums[i], nums[t] = nums[t], nums[i]
                else:
                    break
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([2, 2, 2, 2]))
