class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        t = s.find(part)
        m = len(part)
        while t >= 0:
            s = s[:t] + s[t+m:]
            t = s.find(part)
        return s
