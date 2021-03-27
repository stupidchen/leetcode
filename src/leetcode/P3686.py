class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def cal(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        ret = 0
        for i in range(n):
            ret += cal(i, i)
            if i > 0:
                ret += cal(i - 1, i)
        return ret
