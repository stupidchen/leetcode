from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(lambda: [])
        for i, num in enumerate(nums):
            d[num].append(i)
        m = max([len(v) for v in d.values()])
        r = min([idx[-1] - idx[0] + 1 for idx in filter(lambda x: len(x) == m, d.values())])
        return r


if __name__ == '__main__':
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
