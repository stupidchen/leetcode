import bisect
from typing import List


def build_next(b):
    n = len(b)
    r = [0] * n
    matched = 0
    for i in range(1, n):
        while matched > 0 and (b[matched] != b[i]):
            matched = r[matched - 1]

        if b[matched] == b[i]:
            matched += 1
        r[i] = matched
    return r


def match(o, p, nxt):
    r = []
    matched = 0
    n = len(o)
    m = len(p)
    for i in range(n):
        while matched > 0 and (p[matched] != o[i]):
            matched = nxt[matched - 1]

        if p[matched] == o[i]:
            matched += 1

        if matched == m:
            r.append(i - m + 1)
            matched = nxt[matched - 1]
    return r


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        nxt_a = build_next(a)
        nxt_b = build_next(b)
        indices_a = match(s, a, nxt_a)
        indices_b = match(s, b, nxt_b)

        res = []
        if indices_b:
            for index_a in indices_a:
                ib_l = bisect.bisect_left(indices_b, index_a)
                if (ib_l < len(indices_b) and abs(indices_b[ib_l] - index_a) <= k) or \
                        (ib_l > 0 and abs(indices_b[ib_l - 1] - index_a) <= k):
                    res.append(index_a)
        return res


if __name__ == '__main__':
    r = Solution().beautifulIndices("lrtsi", "lrts", "i", 3)
    print(r)
