from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)

        n = len(nums)
        for i in range(1 << n):
            s = ['0'] * n
            for j in range(n):
                if (1 << j) | i == i:
                    s[j] = '1'
            t = ''.join(s)
            if t not in nums_set:
                return t