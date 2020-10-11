class Solution:
    def maxDepth(self, s: str) -> int:
        r = 0
        t = 0
        for c in s:
            if c == '(':
                t += 1
            if c == ')':
                t -= 1
            r = max(t, r)
        return r
