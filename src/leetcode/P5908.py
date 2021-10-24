from collections import defaultdict
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = defaultdict(lambda: [])
        n = len(parents)
        depth = [0] * n
        dp = [(0, 0)]
        for i in range(1, n):
            children[parents[i]].append(i)
        q = [0]
        h = 0
        while h < len(q):
            c = q[h]
            for child in children[c]:
                depth[child] = depth[c] + 1
                q.append(child)
                dp.append((depth[child], child))
            h += 1
        dp.sort(reverse=True)
        count = [0] * n
        for _, i in dp:
            count[i] = sum([count[child] for child in children[i]]) + 1
        r = 0
        m = 0
        for i in range(n):
            t = (n - count[i])
            if t == 0:
                t = 1
            for child in children[i]:
                t *= count[child]
            if t == m:
                r += 1
            elif t > m:
                m = t
                r = 1
        return r


if __name__ == '__main__':
    print(Solution().countHighestScoreNodes([-1, 2, 0, 2, 0]))
