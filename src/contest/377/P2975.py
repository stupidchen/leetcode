from typing import List

MODULO = 10 ** 9 + 7


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hs = [1] + sorted(hFences) + [m]
        vs = [1] + sorted(vFences) + [n]

        vss = set()
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                vss.add(vs[j] - vs[i])

        res = -1
        for i in range(len(hs)):
            for j in range(i + 1, len(hs)):
                h = hs[j] - hs[i]
                if h in vss:
                    res = max(res, h)
        if res == -1:
            return res
        return (res * res) % MODULO


if __name__ == '__main__':
    r = Solution().maximizeSquareArea(3, 9, [2], [8, 6, 5, 4])
    print(r)
