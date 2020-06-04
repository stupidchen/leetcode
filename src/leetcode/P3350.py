class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        for i in range(n >> 1):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]

