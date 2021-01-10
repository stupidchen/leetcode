from collections import defaultdict


class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        s = [1] * n
        b = [i for i in range(n)]

        def find(x):
            if b[x] != x:
                b[x] = find(b[x])
            return b[x]

        def merge(x, y):
            bx = find(x)
            by = find(y)
            if s[bx] > s[by]:
                b[by] = b[bx]
            else:
                b[bx] = b[by]
                s[by] = max(s[bx] + 1, s[by])

        for x, y in allowedSwaps:
            merge(x, y)

        d = defaultdict(lambda: [])
        for i in range(n):
            d[find(i)].append(i)


        r = 0
        for i, p in d.items():
            qs = defaultdict(lambda: 0)
            qt = defaultdict(lambda: 0)
            for v in p:
                qs[source[v]] += 1
                qt[target[v]] += 1

            r += len(p)
            for k, v in qs.items():
                r -= min(v, qt[k])
        return r


if __name__ == '__main__':
    print(Solution().minimumHammingDistance([41, 37, 51, 100, 25, 33, 90, 49, 65, 87, 11, 18, 15, 18],
                                            [41, 92, 69, 75, 29, 13, 53, 21, 17, 81, 33, 19, 33, 32],
                                            [[0, 11], [5, 9], [6, 9], [5, 7], [8, 13], [4, 8], [12, 7], [8, 2], [13, 5],
                                             [0, 7], [6, 4], [8, 9], [4, 12], [6, 1], [10, 0], [10, 2], [7, 3],
                                             [11, 10], [5, 2], [11, 1], [3, 0], [8, 5], [12, 6], [2, 1], [11, 2],
                                             [4, 9], [2, 9], [10, 6], [12, 10], [4, 13], [13, 2], [11, 9], [3, 6],
                                             [0, 4], [1, 10], [5, 11], [12, 1], [10, 4], [6, 2], [10, 7], [3, 13],
                                             [4, 5], [13, 10], [4, 7], [0, 12], [9, 10], [9, 3], [0, 5], [1, 9],
                                             [5, 10], [8, 0], [12, 11], [11, 4], [7, 9], [7, 2], [13, 9], [12, 3],
                                             [8, 6], [7, 6], [8, 12], [4, 3], [7, 13], [0, 13], [2, 0], [3, 8], [8, 1],
                                             [13, 6], [1, 4], [0, 9], [2, 3], [8, 7], [4, 2], [9, 12]]))
