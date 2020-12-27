VOWELS = 'AEIOU'


def count_vowels(x):
    r = 0
    for c in x:
        if c.upper() in VOWELS:
            r += 1
    return r


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        h = len(s) >> 1
        return count_vowels(s[:h]) == count_vowels(s[h:])
