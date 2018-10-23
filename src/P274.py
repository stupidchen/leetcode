class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        a = sorted(citations)
        n = len(citations)
        l, r = 0, n - 1
        ret = 0
        while l <= r:
            mid = (l + r) >> 1
            if n - mid <= a[mid]:
                ret = n - mid
                r = mid - 1
            else:
                l = mid + 1
        return ret

if __name__ == '__main__':
    print(Solution().hIndex([100, 3, 4, 5, 1]))
