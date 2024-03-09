import math
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pf = defaultdict(lambda: math.inf)
        pf[nums[0]] = 0
        n = len(nums)
        count = nums[0]
        res = -math.inf
        for i in range(1, n):
            res = max(res, count + nums[i] - pf[nums[i] + k])
            res = max(res, count + nums[i] - pf[nums[i] - k])
            pf[nums[i]] = min(pf[nums[i]], count)
            count += nums[i]
        if math.isinf(res):
            res = 0
        return res


if __name__ == '__main__':
    r = Solution().maximumSubarraySum(nums=[1, 2, 3, 4, 5, 6], k=1)
    r = Solution().maximumSubarraySum(nums=[1, 2], k=2)
    print(r)
