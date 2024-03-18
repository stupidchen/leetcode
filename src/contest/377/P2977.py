import math
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        chars = list(set(original) | set(changed))
        chars_map = {char: i for i, char in enumerate(chars)}
        n = len(chars)
        d = [[math.inf] * n for i in range(n)]
        for cc in zip(original, changed, cost):
            x, y, w = cc
            x = chars_map[x]
            y = chars_map[y]
            d[x][y] = min(w, d[x][y])
        for i in range(n):
            d[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]

        m = max(map(len, original))
        n = len(source)
        f = [0] * (n + 1)
        for i in range(n):
            if source[i] == target[i]:
                f[i + 1] = f[i]
            else:
                f[i + 1] = math.inf
            for char in chars:
                if len(char) <= i + 1 and source[i - len(char) + 1: i + 1] == char:
                    oo = chars_map.get(char)
                    tt = chars_map.get(target[i - len(char) + 1: i + 1])
                    if oo is None or tt is None:
                        continue
                    f[i + 1] = min(f[i + 1], f[i - len(char) + 1] + d[oo][tt])
        res = f[n] if not math.isinf(f[n]) else -1
        return res


if __name__ == '__main__':
    # r = Solution().minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
    #                            changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20])
    r = Solution().minimumCost("ajhpd",
                               "djjdc",
                               ["hpd", "iyk", "qzd", "hpi", "aic", "znh", "cea", "fug", "wir", "kwu", "yjo", "rzi", "a",
                                "n", "f", "q", "u", "w", "x", "i", "x", "s", "o", "u"],
                               ["iyk", "qzd", "hpi", "aic", "znh", "cea", "fug", "wir", "kwu", "yjo", "rzi", "jdc", "n",
                                "f", "q", "u", "w", "x", "i", "x", "s", "o", "u", "d"],
                               [80257, 95140, 96349, 89449, 81714, 5859, 96734, 96109, 41211, 99975, 57611, 32644,
                                82896, 22164, 99889, 98061, 95403, 90922, 64031, 94558, 58418, 99717, 96588, 88286])
    print(r)
