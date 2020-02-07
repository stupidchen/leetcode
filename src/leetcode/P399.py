from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        d = defaultdict(lambda: {})
        m = len(equations)
        for i in range(m):
            x, y = equations[i]
            d[x][y] = values[i]
            d[y][x] = 1 / values[i]

        n = len(d)
        for i in range(n):
            d[i][i] = 1
        o = d.keys()
        for k in o:
            for i in o:
                for j in o:
                    if j not in d[i] and k in d[i] and j in d[k]:
                        d[i][j] = d[i][k] * d[k][j]
                        d[j][i] = 1 / d[i][j]
        ret = []
        for query in queries:
            x, y = query
            if y in d[x]:
                ret.append(d[x][y])
            else:
                ret.append(-1.0)
        return ret


if __name__ == '__main__':
    print(Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                                  [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
