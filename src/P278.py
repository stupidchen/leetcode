# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

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
            if isBadVersion(mid):
                l = mid + 1
            else:
                r = mid - 1
        if isBadVersion(l):
            return l
        return l + 1