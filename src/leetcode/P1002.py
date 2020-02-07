from collections import defaultdict


class Solution:
    def commonChars(self, A):
        d = defaultdict(lambda: [])
        for s in A:
            dd = defaultdict(lambda: 0)
            for c in s:
                dd[c] += 1
            for k in dd.keys():
                d[k].append(dd[k])

        ret = []
        for a in range(26):
            c = chr(a + 97)
            if c in d and len(d[c]) == len(A):
                ret.extend([c] * min(d[c]))
        return ret

if __name__ == '__main__':
    print(Solution().commonChars(["cool","lock","cook"]))
