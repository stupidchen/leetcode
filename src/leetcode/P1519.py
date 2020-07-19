from collections import defaultdict


class Solution:
    def countSubTrees(self, n, edges, labels):
        d = defaultdict(lambda: [])
        for edge in edges:
            x, y = edge
            d[x].append(y)
            d[y].append(x)

        r = [0] * n
        v = [False] * n

        def solve(x):
            t = defaultdict(lambda: 0)
            t[labels[x]] = 1
            v[x] = True
            for y in d[x]:
                if not v[y]:
                    j = solve(y)
                    for k, va in j.items():
                        t[k] += va
            r[x] = t[labels[x]]
            return t

        solve(0)
        return r


if __name__ == '__main__':
    print(Solution().countSubTrees(4,
                                   [[0, 2], [0, 3], [1, 2]],
                                   "aeed",
                                   ))
