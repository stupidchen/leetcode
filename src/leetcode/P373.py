import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        tmp = []
        n, m = len(nums1), len(nums2)

        for i in range(n):
            for j in range(m):
                if len(tmp) == k + 1:
                    heapq.heappop(tmp)

                heapq.heappush(tmp, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))

        ret = []
        while len(tmp) != 0:
            pair = heapq.heappop(tmp)
            ret.append([pair[1], pair[2]])
        if len(ret) <= k:
            return ret[::-1]
        else:
            return ret[::-1][:-1]


if __name__ == '__main__':
    print(Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 10))
