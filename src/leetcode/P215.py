from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            elif heap[0] < num:
                heappop(heap)
                heappush(heap, num)
        return heap[0]