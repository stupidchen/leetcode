from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n, edges):
        f = defaultdict(lambda: [])
        for v1, v2 in edges:
            f[v1].append(v2)
            f[v2].append(v1)

        def find_longest_path(x):
            q = [x]
            d = [-1] * n
            p = [-1] * n
            d[x] = 0
            h = 0
            while h < len(q):
                for y in f[q[h]]:
                    if d[y] == -1:
                        d[y] = d[q[h]] + 1
                        p[y] = q[h]
                        q.append(y)
                h += 1

            mv = -1
            mi = 0
            for i, t in enumerate(d):
                if t > mv:
                    mv = t
                    mi = i
            pp = [mi]
            t = mi
            while p[t] != -1:
                pp.append(p[t])
                t = p[t]
            return mi, pp

        i1, p1 = find_longest_path(0)
        i2, p2 = find_longest_path(i1)
        m = len(p2)
        return list({p2[m >> 1], p2[(m - 1) >> 1]})


if __name__ == '__main__':
    print(Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
