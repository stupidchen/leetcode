from collections import defaultdict

MAX = 6000


class Solution:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)

        q = [(0, False)]
        g = defaultdict(lambda: -1)
        g[(0, False)] = 0
        h = 0
        while h < len(q):
            p, f = q[h]
            if p == x:
                return g[q[h]]

            if f:
                if p + a < MAX and p + a not in forbidden:
                    t = (p + a, False)
                    if g[t] == -1 or (g[q[h]] + 1 < g[t]):
                        q.append(t)
                        g[t] = g[q[h]] + 1
            else:
                if p + a < MAX and p + a not in forbidden:
                    t = (p + a, False)
                    if g[t] == -1 or (g[q[h]] + 1 < g[t]):
                        q.append(t)
                        g[t] = g[q[h]] + 1

                if p - b > 0 and p - b not in forbidden:
                    t = (p - b, True)
                    if g[t] == -1 or (g[q[h]] + 1 < g[t]):
                        q.append(t)
                        g[t] = g[q[h]] + 1
            h += 1
        return -1


if __name__ == '__main__':
    print(Solution().minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))
