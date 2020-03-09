VOWELS = {
    'a': 0,
    'e': 1,
    'i': 2,
    'o': 3,
    'u': 4,
}
LV = 5


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {0: -1}
        n = len(s)
        r, t = 0, 0
        for i in range(n):
            if s[i] in VOWELS:
                t ^= 1 << (VOWELS[s[i]])
            if t in d:
                r = max(r, i - d[t])
            else:
                d[t] = i
        return r


# For test only
SI = (("eleetminicoworoep", ),
      ("leetcodeisgreat", ),
      ("bcbcbc", ),
      )
SO = (13, 5, 6)
TM = 'findTheLongestSubstring'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
