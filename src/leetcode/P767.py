from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        r = ''
        last = '#'
        for i in range(len(s)):
            m = 0
            c = ''
            for k, v in counter.items():
                if v > m and last != k:
                    c = k
                    m = v
            if c == '':
                return ''
            r += c
            last = c
            counter[c] -= 1
        return r

