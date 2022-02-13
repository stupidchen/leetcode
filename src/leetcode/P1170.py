from bisect import bisect_right
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            max_c = 'z'
            ret = 0
            for c in word:
                if max_c > c:
                    max_c = c
                    ret = 1
                elif max_c == c:
                    ret += 1
            return ret

        a = sorted(map(f, words))
        n = len(words)
        ret = []
        for query in queries:
            ff = f(query)
            index = bisect_right(a, ff)
            ret.append(n - index)
        return ret
