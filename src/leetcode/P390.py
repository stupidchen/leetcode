class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = range(1, n + 1)
        while len(t) != 1:
            t = t[1::2][::-1]
        return t[0]
