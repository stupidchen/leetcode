from collections import defaultdict, Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        c = defaultdict(lambda: 0)
        for w in words:
            t = Counter(w)
            for k, v in t.items():
                c[k] += v
        for k, v in c.items():
            if v % n:
                return False
        return True

