from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = Counter([x.lower() for x in licensePlate if x.isalpha()])
        return min([word for word in words if not d - Counter(word)], key=len)
