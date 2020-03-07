import collections


class Solution:
    def sortString(self, s: str) -> str:
        r = ''
        d = collections.Counter(s)
        while d.keys():
            t = sorted(d.keys())
            for c in t:
                r += c
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
            t = sorted(d.keys())
            for c in reversed(t):
                r += c
                d[c] -= 1
                if d[c] == 0:
                    del d[c]

        return r


if __name__ == '__main__':
    print(Solution().sortString("ggggggg"))
