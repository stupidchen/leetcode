from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s):
        d = defaultdict(lambda: [])
        for i, c in enumerate(s):
            d[c].append(i)

        f = [[0] * 26]
        for i, c in enumerate(s):
            s = f[-1].copy()
            s[ord(c) - 97] += 1
            f.append(s)

        def count(l, r):
            ret = 0
            for i in range(26):
                if f[r][i] - f[l + 1][i] != 0:
                    ret += 1
            return ret

        ret = 0
        for c, p in d.items():
            if len(p) > 1:
                ret += count(p[0], p[-1])
        return ret


if __name__ == '__main__':
    print(Solution().countPalindromicSubsequence("bbcbaba"))
    print(Solution().countPalindromicSubsequence("bbb"))
