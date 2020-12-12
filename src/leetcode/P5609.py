from collections import Counter


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        r = 0
        for word in words:
            c = Counter(word)
            v = True
            for k in c:
                if k not in allowed:
                    v = False
                    break
            if v:
                r += 1
        return r
