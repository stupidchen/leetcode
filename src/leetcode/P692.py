from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        a = sorted([(-t, s) for s, t in c.items()])
        r = []
        for t, s in a[:k]:
            r.append(s)
        return r


if __name__ == '__main__':
    print(Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
