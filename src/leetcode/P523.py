from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = (s[i] + nums[i]) % k

        d = set()
        for i in range(2, n + 1):
            d.add(s[i - 2])
            if s[i] in d:
                return True
        return False
