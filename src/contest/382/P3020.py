from collections import Counter
from math import sqrt
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        f = {1: (counter[1] + 1) >> 1}
        for num in sorted(counter.keys()):
            if num != 1:
                f[num] = 1
                root = int(sqrt(num))
                if root * root == num and counter[root] >= 2:
                    f[num] = f[root] + 1
        res = max(f.values()) * 2 - 1
        return res


if __name__ == '__main__':
    r = Solution().maximumLength([1, 1])
    print(r)
