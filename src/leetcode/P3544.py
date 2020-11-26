import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        d = collections.Counter(s)

        t, r = 0, 0
        for i, c in enumerate(s):
            if d[c] < k:
                r = max(r, self.longestSubstring(s[t: i], k))
                t = i + 1

        return len(s) if t == 0 else max(r, self.longestSubstring(s[t:], k))


# For test only
SI = (("ababbc", 2),
      ("aaabb", 3),)
SO = (5, 3)
TM = 'longestSubstring'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
