from heapq import heappush, heappop


class Solution:
    def minStoneSum(self, piles, k):
        heap = []
        for pile in piles:
            heappush(heap, -pile)

        for i in range(k):
            heappush(heap, -((1-heappop(heap)) >> 1))
        return -sum(heap)


if __name__ == '__main__':
    print(Solution().minStoneSum([5, 4, 9], 2))
