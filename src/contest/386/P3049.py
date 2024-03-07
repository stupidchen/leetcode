import heapq
from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        m = len(changeIndices)
        n = len(nums)
        s = sum(nums)

        for i in range(m):
            changeIndices[i] -= 1

        v = {}
        for i, ci in enumerate(changeIndices):
            if ci not in v and nums[ci] != 0:
                v[ci] = i
        first_appear = dict({value: key for key, value in v.items()})

        def possible(bound):
            h = []
            time_available = 0
            for i in reversed(range(bound)):
                if i in first_appear:
                    heapq.heappush(h, nums[changeIndices[i]])
                    if time_available > 0:
                        time_available -= 1
                    else:
                        time_available += 1
                        heapq.heappop(h)
                else:
                    time_available += 1
            return time_available >= n - len(h) + s - sum(h)

        lo = 0
        hi = m + 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo if lo <= m else -1


if __name__ == '__main__':
    r = Solution().earliestSecondToMarkIndices(nums=[2, 2], changeIndices=[2, 2, 1, 2])
    print(r)
