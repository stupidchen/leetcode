from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds = defaultdict(lambda: 0)
        dt = defaultdict(lambda: 0)
        for c in t:
            dt[c] += 1
        for c in s:
            ds[c] += 1

        cc = set(dt.keys()) | set(ds.keys())
        r = 0
        for c in cc:
            r += abs(ds[c] - dt[c])
        r = r >> 1
        return r


# For test only
SI = (('bab', 'aba'), ('leetcode', 'practice'), ('anagram', 'mangaar'), ('xxyyzz', 'xxyyzz'), ('friend', 'family'))
SO = (1, 5, 0, 0, 4)
TM = 'minSteps'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
