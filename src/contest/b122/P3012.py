import heapq
from collections import Counter
from typing import List


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        min_num = min(nums)
        min_count = counter[min_num]
        if min_num == 1:
            return ((min_count - 1) >> 1) + 1

        h = list(map(lambda x: -x, counter.keys()))
        heapq.heapify(h)
        while len(h) > 1:
            p, q = heapq.heappop(h), heapq.heappop(h)
            mod = -p % -q
            if mod != 0:
                heapq.heappush(h, -mod)
            heapq.heappush(h, q)
        if -h[0] < min_num:
            return 1
        else:
            return ((min_count - 1) >> 1) + 1


if __name__ == '__main__':
    r = Solution().minimumArrayLength(nums=[3, 3, 3, 4])
    print(r)
