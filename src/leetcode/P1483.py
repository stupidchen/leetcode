from typing import List

DEPTH = 17


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        f = []
        depth = n.bit_length() + 1
        for i in range(n):
            f.append([-1] * depth)
            f[i][0] = parent[i]
        for k in range(1, depth):
            for i in range(n):
                if f[i][k - 1] != -1:
                    f[i][k] = f[f[i][k - 1]][k - 1]
        self._n = n
        self._depth = depth
        self._f = f

    def getKthAncestor(self, node: int, k: int) -> int:
        depth = self._depth
        f = self._f

        r = node
        for i in reversed(range(depth)):
            p = 1 << i
            if k - p >= 0:
                if f[r][i] == -1:
                    return -1
                r = f[r][i]
                k -= p

        return r
