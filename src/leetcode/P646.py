from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted([tuple(pair) for pair in pairs])
        n = len(pairs)
        f = [1] * n
        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)
