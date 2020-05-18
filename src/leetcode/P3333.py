from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = Counter(s1)
        t = Counter(s2[:len(s1) - 1])
        for i in range(len(s1) - 1, len(s2)):
            t[s2[i]] += 1
            if t == d:
                return True
            t[s2[i + 1 - len(s1)]] -= 1
            if t[s2[i + 1 - len(s1)]] == 0:
                del t[s2[i + 1 - len(s1)]]
        return False

