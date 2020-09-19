from math import inf


class Solution:
    def isPrintable(self, targetGrid):
        d = {}
        t = 0
        n = len(targetGrid)
        m = len(targetGrid[0])
        for row in targetGrid:
            for i in range(m):
                c = row[i]
                if c not in d:
                    d[c] = t
                    t += 1
                row[i] = d[c]

        v = [False] * t
        minx = [inf] * t
        maxx = [-1] * t
        miny = [inf] * t
        maxy = [-1] * t
        for i in range(n):
            for j in range(m):
                minx[targetGrid[i][j]] = min(minx[targetGrid[i][j]], i)
                maxx[targetGrid[i][j]] = max(maxx[targetGrid[i][j]], i)
                miny[targetGrid[i][j]] = min(miny[targetGrid[i][j]], j)
                maxy[targetGrid[i][j]] = max(maxy[targetGrid[i][j]], j)
        e = [set() for i in range(t)]
        re = [set() for i in range(t)]
        r = set()
        for c in range(t):
            p = True
            for i in range(minx[c], maxx[c] + 1):
                for j in range(miny[c], maxy[c] + 1):
                    if targetGrid[i][j] != c:
                        p = False
                        e[c].add(targetGrid[i][j])
                        re[targetGrid[i][j]].add(c)
            if p:
                r.add(c)
        while True:
            nr = set()
            for c in r:
                if not v[c]:
                    v[c] = True
                    for i in re[c]:
                        e[i].remove(c)
                        if len(e[i]) == 0:
                            nr.add(i)
            r = nr
            if len(r) == 0:
                break
        return all(v)


if __name__ == '__main__':
    print(Solution().isPrintable(targetGrid=[[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]]))
    print(Solution().isPrintable(targetGrid=[[1, 2], [2, 1]]))
