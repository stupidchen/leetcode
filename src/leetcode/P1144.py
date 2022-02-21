from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        r1 = 0
        for i in range(n):
            if i & 1 == 1:
                t = 0
                if i + 1 < n:
                    t = max(nums[i] - nums[i + 1] + 1, t)
                t = max(nums[i] - nums[i - 1] + 1, t)
                r1 = t + r1

        r2 = 0
        for i in range(n):
            if i & 1 == 0:
                t = 0
                if i - 1 > 0:
                    t = max(nums[i] - nums[i - 1] + 1, t)
                if i + 1 < n:
                    t = max(nums[i] - nums[i + 1] + 1, t)
                r2 = t + r2
        return min(r1, r2)


if __name__ == '__main__':
    print(Solution().movesToMakeZigzag([9, 6, 1, 6, 2]))
