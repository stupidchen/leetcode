import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = collections.Counter(s)

        def find(c):
            l = r = t = 0
            for i in range(len(s)):
                if s[i] != c:
                    t += 1
                while t > k:
                    if s[l] != c:
                        t -= 1
                    l += 1
                r = max(i - l + 1, r)
            return r

        r = 0
        for c in d.keys():
            r = max(r, find(c))
        return r


# For test only
SI = (('AABABBA', 1,),)
SO = (4,)
TM = 'characterReplacement'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
