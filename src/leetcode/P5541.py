from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        tn = len(t)
        dt = defaultdict(lambda: 0)
        for i in range(tn):
            for j in range(i, tn):
                dt[t[i:j + 1]] += 1

        ds = defaultdict(lambda: 0)
        sn = len(s)
        for i in range(sn):
            for j in range(i, sn):
                ds[s[i:j + 1]] += 1

        r = 0
        for ss, nss in ds.items():
            for k in range(len(ss)):
                for i in range(26):
                    if chr(97 + i) == ss[k]:
                        continue
                    tr = ss[:k] + chr(97 + i) + ss[k+1:]
                    if tr in dt:
                        r += dt[tr] * nss
        return r


if __name__ == '__main__':
    print(Solution().countSubstrings('ab', 'bb'))
    print(Solution().countSubstrings('a', 'a'))
    print(Solution().countSubstrings('aba', 'baba'))
