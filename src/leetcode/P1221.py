class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        b = 0
        for c in s:
            if c == 'L':
                b += 1
            else:
                b -= 1
            if b == 0:
                r += 1
        return r
