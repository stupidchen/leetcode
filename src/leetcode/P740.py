from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        s = min(nums)
        e = max(nums)
        c = Counter(nums)
        f = [0] * (e + 1)
        for i in range(s, e + 1):
            f[i] = (f[i - 2] if i > 1 else 0) + c[i] * i
            f[i] = max(f[i - 1], f[i])
        return max(f)


if __name__ == '__main__':
    print(Solution().deleteAndEarn([1]))
