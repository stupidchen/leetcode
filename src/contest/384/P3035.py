from collections import Counter
from typing import List


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        counter = Counter()
        length = []
        for word in words:
            counter += Counter(word)
            length.append(len(word))
        pair = sum([v >> 1 for v in counter.values()])
        length.sort()
        res = 0
        for i, l in enumerate(length):
            need_pair = l >> 1
            if pair < need_pair:
                break
            pair -= need_pair
            res += 1
        return res
