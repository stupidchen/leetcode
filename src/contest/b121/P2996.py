from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                res += nums[i]
            else:
                break
        s = set(nums)
        while res in s:
            res += 1
        return res


if __name__ == '__main__':
    r = Solution().missingInteger([4, 5, 6, 7, 8, 8, 9, 4, 3, 2, 7])
    print(r)
