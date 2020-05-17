from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        r = []
        if len(s) < len(p):
            return r
        d = Counter(p)
        t = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            t[s[i]] += 1
            if t == d:
                r.append(i + 1 - len(p))
            t[s[i + 1 - len(p)]] -= 1
            if t[s[i + 1 - len(p)]] == 0:
                del t[s[i + 1 - len(p)]]
        return r


if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))
