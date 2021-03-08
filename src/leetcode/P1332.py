class Solution:
    def removePalindromeSub(self, s):
        return 0 if s == "" else 1 if s == s[::-1] else 2
