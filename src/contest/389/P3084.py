class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        res = 0
        cc = 0
        for ch in s:
            if ch == c:
                cc += 1
                res += cc
        return res
