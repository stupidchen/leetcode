class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        r = 0
        for i in range(len(s) - 2):
            t = s[i:i+3]
            if t[0] != t[1] and t[1] != t[2] and t[2] != t[0]:
                r += 1
        return r
