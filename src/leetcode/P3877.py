import collections


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        d = collections.defaultdict(lambda: 0)
        for a in A:
            d[a] += 1

        n = [k for k in d.keys() if k < 0]
        p = [k for k in d.keys() if k > 0]
        n = list(reversed(sorted(n)))
        p = sorted(p)
        for k in p:
            if d[k] != 0:
                if d[k] > d[k << 1]:
                    return False
                d[k << 1] -= d[k]
                d[k] = 0
        for k in p:
            if d[k] > 0:
                return False

        for k in n:
            if d[k] != 0:
                if d[k] > d[k << 1]:
                    return False
                d[k << 1] -= d[k]
                d[k] = 0
        for k in n:
            if d[k] > 0:
                return False

        return (d[0] & 1) == 0
