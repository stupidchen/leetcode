import math
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        res = math.inf
        size = k - 2
        sl = SortedList(nums[1:dist+1])
        cost_mid = sum(sl.islice(0, size))

        for i in range(1, n - k + 2):
            if i + dist < n:
                sl.add(nums[i+dist])
                cost_mid += nums[i+dist]
                if sl.bisect_right(nums[i+dist]) <= size:
                    cost_mid -= sl[size]
                else:
                    cost_mid -= nums[i+dist]
            elif len(sl) <= size:
                break

            index_to_be_removed = sl.bisect_right(nums[i])
            if index_to_be_removed <= size:
                cost_mid = cost_mid - nums[i] + sl[size]
            sl.remove(nums[i])

            cost = nums[0] + nums[i] + cost_mid
            res = min(res, cost)
        return res


if __name__ == '__main__':
    r = Solution().minimumCost([20, 43, 21, 19, 3, 39, 40, 37, 32, 12], 5, 4)
    print(r)
