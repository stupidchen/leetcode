import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = collections.Counter(s)
        r = ''
        while len(d) != 0:
            t = sorted(d.keys())
            for c in t:
                f = s.find(c)
                p = collections.Counter(s[:f])
                o = True
                for k in p:
                    if d[k] <= p[k]:
                        o = False
                        break
                if o:
                    r += c
                    for k in p:
                        d[k] -= p[k]
                    del d[c]
                    s = s[f + 1:]
                    s = s.replace(c, '')
                    break

        return r


# For test only
SI = (("bbcaac", ), ("cbacdcbc",), ("bcabc",))
SO = ("bac", "acdb", "abc")
TM = 'removeDuplicateLetters'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
