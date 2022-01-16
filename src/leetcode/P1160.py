from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        r = 0
        for word in words:
            t = Counter(word)
            b = True
            for k, v in t.items():
                if c.get(k, 0) < v:
                    b = False
                    break
            if b:
                r += len(word)
        return r

