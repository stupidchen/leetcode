class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)
        for i in range(n):
            for j in range(i + 1, n):
                if s1[:i] + s1[j] + s1[i+1:j] + s1[i] + s1[j+1:] == s2:
                    return True
        return False
