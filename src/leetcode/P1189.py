from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text.lower())
        return min(c['b'], c['a'], c['l'] >> 1, c['o'] >> 1, c['n'])