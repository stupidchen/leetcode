from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs):
        d = defaultdict(lambda: [])
        for pair in adjacentPairs:
            u, v = pair
            d[u].append(v)
            d[v].append(u)

        f = None
        for k, v in d.items():
            if len(v) == 1:
                f = k
                break
        r = [f]
        l = None
        while True:
            t = None
            for i in d[f]:
                if i != l:
                    t = i
                    break
            if t is None:
                break
            r.append(t)
            l = f
            f = t
        return r


if __name__ == '__main__':
    print(Solution().restoreArray([[2, 1], [3, 4], [3, 2]]))
