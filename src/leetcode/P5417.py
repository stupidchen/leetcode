VOWELS = 'aeiou'

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        r = 0
        l = 0
        for i in range(len(s)):
            if i - k >= 0:
                if s[i - k] in VOWELS:
                    l -= 1
            if s[i] in VOWELS:
                l += 1
            r = max(r, l)
        return r
