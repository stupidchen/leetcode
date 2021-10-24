from collections import defaultdict
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        v = defaultdict(lambda: [])
        ind = [0] * n
        for x, y in relations:
            x -= 1
            y -= 1
            v[x].append(y)
            ind[y] += 1

        f = [0] * n
        c = []
        for i in range(n):
            if ind[i] == 0:
                f[i] = time[i]
                c.append(i)
        while len(c) != 0:
            nc = []
            for cc in c:
                for i in v[cc]:
                    ind[i] -= 1
                    f[i] = max(time[i] + f[cc], f[i])
                    if ind[i] == 0:
                        nc.append(i)
            c = nc
        return max(f)


if __name__ == '__main__':
    print(Solution().minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
