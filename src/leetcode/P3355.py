class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p = 0
        for i in t:
            if p >= len(s):
                break
            if i == s[p]:
                p += 1
        return p >= len(s)
