from collections import Counter
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        r = 0
        for i in range(1, 1 << n):
            s = ''
            for j in range(n):
                if i | (1 << j) == i:
                    s += arr[j]
            c = Counter(s)
            if all([v <= 1 for v in c.values()]):
                r = max(r, len(s))
        return r


if __name__ == '__main__':
    print(Solution().maxLength(['uni', 'que']))
