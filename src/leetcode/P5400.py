from collections import defaultdict


class Solution:
    def destCity(self, paths):
        d = defaultdict(lambda: 0)
        for path in paths:
            if path[1] not in d:
                d[path[1]] = 0
            d[path[0]] += 1

        for c in d:
            if d[c] == 0:
                return c

if __name__ == '__main__':
    print(Solution().destCity([["A","Z"]]))
