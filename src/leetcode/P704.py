from bisect import bisect


class Solution:
    def search(self, nums, target):
        i = bisect(nums, target) - 1
        if not (0 <= i < len(nums)) or nums[i] != target:
            return -1
        return i


if __name__ == '__main__':
    print(Solution().search([-1, 0, 3, 5, 9, 12], 10))
