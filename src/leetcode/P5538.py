from collections import defaultdict


class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        m = len(edges)

        def find(v, x):
            if v[x] != x:
                v[x] = find(v, v[x])
            return v[x]

        def merge(v, x, y):
            fx = find(v, x)
            fy = find(v, y)
            v[fx] = v[fy]

        def longest(s, e):
            q = [s]
            h = 0
            v = [-1] * n
            v[s] = 0
            while h < len(q):
                t = q[h]
                for i in e[t]:
                    if v[i] == -1:
                        v[i] = v[t] + 1
                        q.append(i)
                h += 1

            rv = 0
            ri = None
            for i in range(n):
                if v[i] > rv:
                    rv = v[i]
                    ri = i
            return rv, ri

        def solve(s):
            e = defaultdict(lambda: [])
            v = [i for i in range(n)]
            ss = [False] * n
            for i in range(m):
                if (1 << i) | s == s:
                    x, y = edges[i][0] - 1, edges[i][1] - 1
                    ss[x] = True
                    ss[y] = True
                    merge(v, x, y)
                    e[x].append(y)
                    e[y].append(x)
            d = set()
            t = None
            for i in range(1, n):
                if ss[i]:
                    t = i
                    d.add(find(v, i))
            if len(d) != 1:
                return None
            tv, ti = longest(t, e)
            tv, ti = longest(ti, e)
            return tv

        r = [0] * (n - 1)
        for i in range(1, (1 << m)):
            t = solve(i)
            if t is not None:
                r[t - 1] += 1
        return r


if __name__ == '__main__':
    print(Solution().countSubgraphsForEachDiameter(n=15, edges=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [13, 15]]))
