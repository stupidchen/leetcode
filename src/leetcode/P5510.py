from collections import defaultdict


class Solution:
    def maxNumEdgesToRemove(self, n, edges) -> int:
        e = [defaultdict(lambda: set()) for i in range(3)]
        d = 0
        for edge in edges:
            t, x, y = edge
            x -= 1
            y -= 1
            t -= 1
            if y in e[t][x]:
                d += 1
            else:
                e[t][x].add(y)
                e[t][y].add(x)

        q = 0
        for i in range(n):
            for j in e[2][i]:
                for k in range(2):
                    if j in e[k][i]:
                        q += 1
                        e[k][i].remove(j)
        q = q >> 1

        def visit(v, c, t, o):
            v[c] = o
            for i in e[t][c]:
                if v[i] == -1:
                    visit(v, i, t, o)
            if t != 2:
                for i in e[2][c]:
                    if v[i] == -1:
                        visit(v, i, t, o)

        def solve(t):
            v = [-1] * n
            p = 0
            for i in range(n):
                if v[i] == -1:
                    visit(v, i, t, p)
                    p += 1

            mp = [0] * p
            cp = [0] * p
            for i in range(n):
                mp[v[i]] += len(e[t][i])
                cp[v[i]] += 1

            return p, mp, cp, v

        r = d + q
        p2, mp2, cp2, vp2 = solve(2)
        for i in range(p2):
            r += (mp2[i] >> 1) - (cp2[i] - 1)

        rr = [solve(t) for t in range(2)]
        if rr[0][0] != 1 or rr[1][0] != 1:
            return -1

        tp = p2 + (n - sum(cp2))
        for k in range(2):
            ee = 0
            tt = 0
            for i in range(n):
                for j in e[k][i]:
                    if vp2[i] != vp2[j]:
                        ee += 1
                    else:
                        tt += 1
            ee = ee >> 1
            tt = tt >> 1
            r += ee - (tp - 1) + tt

        return r


if __name__ == '__main__':
    print(Solution().maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))
    print(Solution().maxNumEdgesToRemove(13,
                                         [[1, 1, 2], [2, 1, 3], [3, 2, 4], [3, 2, 5], [1, 2, 6], [3, 6, 7], [3, 7, 8], [
                                             3, 6, 9], [3, 4, 10], [2, 3, 11], [1, 5, 12], [3, 3, 13], [2, 1, 10],
                                          [2, 6, 11], [3, 5, 13], [1, 9, 12], [
                                              1, 6, 8], [3, 6, 13], [2, 1, 4], [1, 1, 13], [2, 9, 10], [2, 1, 6], [2,
                                                                                                                   10,
                                                                                                                   13],
                                          [
                                              2, 2, 9], [3, 4, 12], [2, 4, 7], [1, 1, 10], [1, 3, 7], [1, 7, 11], [3, 3,
                                                                                                                   12],
                                          [
                                              2, 4, 8], [3, 8, 9], [1, 9, 13], [2, 4, 10], [1, 6, 9], [3, 10, 13], [1,
                                                                                                                    7,
                                                                                                                    10],
                                          [
                                              1, 1, 11], [2, 4, 9], [3, 5, 11], [3, 2, 6], [2, 1, 5], [2, 5, 11], [2, 1,
                                                                                                                   7], [
                                              2, 3, 8], [2, 8, 9], [3, 4, 13], [3, 3, 8], [3, 3, 11], [2, 9, 11], [3, 1,
                                                                                                                   8], [
                                              2, 1, 8], [3, 8, 13], [2, 10, 11], [3, 1, 5], [1, 10, 11], [1, 7, 12], [2,
                                                                                                                      3,
                                                                                                                      5],
                                          [
                                              3, 1, 13], [2, 4, 11], [2, 3, 9], [2, 6, 9], [2, 1, 13], [3, 1, 12], [2,
                                                                                                                    7,
                                                                                                                    8],
                                          [
                                              2, 5, 6], [3, 1, 9], [1, 5, 10], [3, 2, 13], [2, 3, 6], [2, 2, 10], [3, 4,
                                                                                                                   11],
                                          [
                                              1, 4, 13], [3, 5, 10], [1, 4, 10], [1, 1, 8], [3, 3, 4], [2, 4, 6], [2, 7,
                                                                                                                   11],
                                          [
                                              2, 7, 10], [2, 3, 12], [3, 7, 11], [3, 9, 10], [2, 11, 13], [1, 1, 12], [
                                              2, 10, 12], [1, 7, 13], [1, 4, 11], [2, 4, 5], [1, 3, 10], [2, 12, 13], [
                                              3, 3, 10], [1, 6, 12], [3, 6, 10], [1, 3, 4], [2, 7, 9], [1, 3, 11], [2,
                                                                                                                    2,
                                                                                                                    8],
                                          [
                                              1, 2, 8], [1, 11, 13], [1, 2, 13], [2, 2, 6], [1, 4, 6], [1, 6, 11], [3,
                                                                                                                    1,
                                                                                                                    2],
                                          [
                                              1, 1, 3], [2, 11, 12], [3, 2, 11], [1, 9, 10], [2, 6, 12], [3, 1, 7], [1,
                                                                                                                     4,
                                                                                                                     9],
                                          [
                                              1, 10, 12], [2, 6, 13], [2, 2, 12], [2, 1, 11], [2, 5, 9], [1, 3, 8], [1,
                                                                                                                     7,
                                                                                                                     8],
                                          [
                                              1, 2, 12], [1, 5, 11], [2, 7, 12], [3, 1, 11], [3, 9, 12], [3, 2, 9], [3,
                                                                                                                     10,
                                                                                                                     11]]))