from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections):
        d = defaultdict(lambda: [])
        for connection in connections:
            x, y = connection
            d[x].append((y, False))
            d[y].append((x, True))

        q = [0]
        v = [False] * n
        v[0] = True
        h = 0
        r = 0
        while h < len(q):
            c = q[h]
            for i in range(len(d[c])):
                t, dr = d[c][i]
                if not v[t]:
                    if not dr:
                        r += 1
                    q.append(t)
                    v[t] = True
            h += 1

        return r

