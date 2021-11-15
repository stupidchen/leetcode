import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k
        while len(list(nums)) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(list(self.nums)) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
