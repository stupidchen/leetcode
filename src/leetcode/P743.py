import math
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(lambda: [])
        for edge in times:
            x, y, w = edge
            edges[x - 1].append((y - 1, w))

        k -= 1
        f = [math.inf] * n
        f[k] = 0
        h = 0
        q = [k]
        while h < len(q):
            c = q[h]
            for edge in edges[c]:
                y, w = edge
                if f[c] + w < f[y]:
                    q.append(y)
                    f[y] = f[c] + w

            h += 1

        r = max(f)
        if math.isinf(r):
            r = -1
        return r


if __name__ == '__main__':
    print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
