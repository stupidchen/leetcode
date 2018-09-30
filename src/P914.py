def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d = {}
        for i in deck:
            d[i] = d.setdefault(i, 0) + 1
        v = d.values()
        if len(v) == 0:
            return False
        X = v[0]
        for vv in v:
            X = gcd(vv, X)
        return X >= 2
