class Solution:
    def isPrefixString(self, s, words):
        n = len(s)
        m = 0
        for k in range(len(words)):
            if s[m:m+len(words[k])] == words[k]:
                m += len(words[k])
            else:
                return False
            if m == n:
                return True
        return False
