from collections import defaultdict


class Solution:
    def makeEqual(self, words):
        d = defaultdict(lambda: 0)
        for word in words:
            for c in word:
                d[c] += 1
        n = len(words)
        for k, v in d.items():
            if v % n != 0:
                return False
        return True
