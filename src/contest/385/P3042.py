from typing import List


def valid(s1: str, s2: str) -> bool:
    return s2.startswith(s1) and s2.endswith(s1)


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                if valid(words[i], words[j]):
                    ret += 1
        return ret


