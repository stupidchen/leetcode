class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        while i * i < num:
            i += 1
        return i * i == num