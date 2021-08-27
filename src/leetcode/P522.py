from typing import List


def is_subsequence(x, y):
    y = iter(y)
    return all(c in y for c in x)


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs = list(sorted(strs, key=lambda x: len(x), reverse=True))
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, t) for j, t in enumerate(strs) if j != i):
                return len(strs[i])
        return -1

