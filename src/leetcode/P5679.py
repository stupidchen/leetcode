from collections import defaultdict


class Solution:
    def minTrioDegree(self, n: int, edges):
        v = defaultdict(lambda: set())
        for edge in edges:
            x, y = edge
            v[x].add(y)
            v[y].add(x)

        f = [0]
        for i in range(n):
            f.append(len(v[i + 1]) - 2)

        r = -1
        for i in range(n):
            if r != -1 and r <= f[i]:
                continue

            for j in v[i]:
                if r != -1 and r <= f[i] + f[j]:
                    continue

                for k in v[i]:
                    if r != -1 and r <= f[i] + f[j] + f[k]:
                        continue

                    if k != j and k in v[j]:
                        d = f[i] + f[j] + f[k]
                        if r == -1 or r > d:
                            r = d

        return r


if __name__ == '__main__':
    n = 400
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append([i, j])

    print(Solution().minTrioDegree(n, edges))
