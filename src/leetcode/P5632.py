def find(s, x):
    p = []
    while s[x] != x:
        p.append(x)
        x = s[x]
    for pp in p:
        s[pp] = x
    return x


def merge(s, d, x, y):
    x = find(s, x)
    y = find(s, y)
    if d[x] < d[y]:
        s[x] = y
    elif d[x] > d[y]:
        s[y] = x
    else:
        s[x] = y
        d[x] += 1


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
        q = len(queries)
        m = len(edgeList)
        r = [False] * q
        edgeList = sorted(edgeList, key=lambda x: x[2])
        queries = [(*queries[i], i) for i in range(q)]
        queries = sorted(queries, key=lambda x: x[2])
        s = [i for i in range(n)]
        d = [1] * n
        t = 0
        for query in queries:
            qx, qy, limit, index = query
            while t < m and edgeList[t][2] < limit:
                merge(s, d, edgeList[t][0], edgeList[t][1])
                t += 1
            sx = find(s, qx)
            sy = find(s, qy)
            r[index] = sx == sy
        return r


if __name__ == '__main__':
    print(Solution().distanceLimitedPathsExist(n=5, edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                               queries=[[0, 4, 14], [1, 4, 13]]))
