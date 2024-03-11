from collections import Counter

USEFUL = 8


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        s = sorted(counter.values(), key=lambda x: -x)
        res = 0
        for i in range((len(s) - 1) // USEFUL + 1):
            res += (i + 1) * sum(s[i * USEFUL: (i + 1) * USEFUL])
        return res

