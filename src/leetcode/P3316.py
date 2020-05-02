class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (l + r) >> 1
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid - 1
        if isBadVersion(l):
            return l
        return l + 1