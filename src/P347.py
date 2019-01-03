import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(lambda: 0)
        for num in nums:
            d[num] = d[num] + 1

        tmp = []
        for key, val in d.items():
            heapq.heappush(tmp, (val, key))
            if len(tmp) > k:
                heapq.heappop(tmp)

        return [v for k, v in tmp]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 2, 2, 1, 1, 3, 3, 3, 4, 3], 1))
