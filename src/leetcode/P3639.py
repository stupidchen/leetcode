class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        c = [-1] * n
        ret = [True]

        def color(x, w):
            for y in graph[x]:
                if c[y] == -1:
                    c[y] = 1 - w
                    color(y, 1 - w)
                    if not ret[0]:
                        return
                elif c[y] != 1 - w:
                    ret[0] = False
                    return

        for i in range(n):
            if c[i] == -1:
                color(i, 0)
        return ret[0]
