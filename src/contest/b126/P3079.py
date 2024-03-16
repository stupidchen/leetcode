from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            sn = str(num)
            res += int(''.join(max(sn) * len(sn)))
        return res

