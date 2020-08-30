from math import sqrt

from collections import defaultdict


def query(s, x):
    t = []
    while s[x] != x:
        t.append(x)
        x = s[x]
    for i in t:
        s[i] = x
    return x


def merge(s, x, y):
    sx, sy = query(s, x), query(s, y)
    s[sy] = sx


class Solution:
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = max(A)
        p = []
        v = [True] * int(sqrt(m) + 1)
        n, lv = len(A), len(v)
        for i in range(2, lv):
            if v[i]:
                p.append(i)
                j = i
                while j * i < lv:
                    v[j * i] = False
                    j += 1

        s = [i for i in range(n)] + [i + n for i in range(len(p))]
        for i in range(len(p)):
            for j in range(n):
                if A[j] % p[i] == 0:
                    merge(s, n + i, j)
                    while A[j] % p[i] == 0:
                        A[j] //= p[i]
        t = list(set(A))
        td = {}
        for i in range(len(t)):
            if t[i] != 1:
                td[t[i]] = i
        ls = len(s)
        s = s + [i + ls for i in range(len(t))]
        for i in range(n):
            if A[i] != 1:
                merge(s, i, td[A[i]] + ls)

        d = defaultdict(lambda: 0)
        for i in range(n):
            d[query(s, i)] += 1
        return max(d.values())


if __name__ == '__main__':
    print(Solution().largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))
