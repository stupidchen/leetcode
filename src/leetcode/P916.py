def isSubset(s, d):
    t = {}
    for l in s:
        t[l] = t.setdefault(l, 0) + 1
    for k, v in d.items():
        if k not in t or t[k] < v:
            return False
    return True


class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        d = {}
        for b in B:
            t = {}
            for l in b:
                t[l] = t.setdefault(l, 0) + 1
            for k, v in t.items():
                d[k] = max(d.setdefault(k, 0), v)
        ret = []
        for a in A:
            if isSubset(a, d):
                ret.append(a)
        return ret
