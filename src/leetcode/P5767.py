class Solution:
    def isCovered(self, ranges, left, right):
        v = {}
        for s in ranges:
            l, r = s
            for i in range(l, r + 1):
                v[i] = True

        for i in range(left, right + 1):
            if i not in v:
                return False
        return True
