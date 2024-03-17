import math
from collections import Counter


def count(counter, key, mask, k):
    min_f = math.inf
    res = 0
    for i, c in enumerate(key):
        f = counter[c]
        if mask & (1 << i) == 0:
            min_f = min(min_f, f)
        else:
            res += f

    for i, c in enumerate(key):
        if mask & (1 << i) == 0:
            f = counter[c]
            res += max(f - min_f - k, 0)
    return res


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        key = sorted(list(counter.keys()), key=lambda x: counter[x])
        m = len(key)
        res = math.inf
        for i in range(m + 1):
            mask = (1 << m) - 1
            for j in range(i):
                mask -= 1 << j
            res = min(res, count(counter, key, mask, k))

            mask = (1 << m) - 1
            for j in range(i):
                mask -= 1 << (m - j - 1)
            res = min(res, count(counter, key, mask, k))
        return res


if __name__ == '__main__':
    r = Solution().minimumDeletions("k", 1)
    print(r)
