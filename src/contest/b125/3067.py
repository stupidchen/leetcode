from collections import defaultdict
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        e = defaultdict(lambda: [])
        for edge in edges:
            a, b, w = edge
            e[a].append((b, w))
            e[b].append((a, w))

        n = len(e)
        r = [0] * n
        v = [False] * n
        for i in range(n):
            branch = []
            v[i] = True
            for br in e[i]:
                b, w = br
                cc = 0
                q = [(b, w % signalSpeed)]
                v[b] = True
                h = 0
                while h < len(q):
                    c, s = q[h]
                    if s == 0:
                        cc += 1
                    for edge in e[c]:
                        b, w = edge
                        if not v[b]:
                            v[b] = True
                            q.append((b, (s + w) % signalSpeed))
                    h += 1
                branch.append(cc)
            for j in range(n):
                v[j] = False
            for j in range(len(branch)):
                for k in range(j + 1, len(branch)):
                    r[i] += branch[j] * branch[k]
        return r


if __name__ == '__main__':
    r = Solution().countPairsOfConnectableServers(edges=[[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]],
                                                  signalSpeed=1)
    print(r)
