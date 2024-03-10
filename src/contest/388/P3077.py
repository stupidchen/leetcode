import math
from typing import List


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [-math.inf] * k
        res = -math.inf
        for i in range(n):
            for j in reversed(range(1, min(k, i + 1))):
                if j & 1 == 0:
                    sign = 1
                else:
                    sign = -1
                value = sign * (k - j) * nums[i]
                f[j] = max(f[j - 1], f[j]) + value
            f[0] = max(f[0] + k * nums[i], k * nums[i])
            res = max(res, f[k - 1])
        return res


if __name__ == '__main__':
    r = Solution().maximumStrength(nums=[1, 2, 3, -1, 2], k=3)
    print(r)
