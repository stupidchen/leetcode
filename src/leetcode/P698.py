from functools import cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        m = sum(nums)
        if m % k != 0:
            return False
        m = m // k
        if max(nums) > m:
            return False

        @cache
        def f(mask):
            if mask == 0:
                return 0
            for i in range(n):
                if mask | (1 << i) == mask:
                    new_mask = mask ^ (1 << i)
                    r = f(new_mask)
                    if r == -1:
                        continue
                    if r + nums[i] <= m:
                        return (r + nums[i]) % m
            return -1

        return f((1 << n) - 1) == 0


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets(
        [2999, 3914, 1064, 927, 64, 1130, 2048, 235, 159, 3549, 241, 987, 972, 976, 279, 1004], 4
    ))
