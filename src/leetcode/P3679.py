class Solution:
    def can(self, x, y):
        a = {}
        for i in x:
            a[i] = a.setdefault(i, 0) + 1
        for i in y:
            if i not in a:
                return False
            if a[i] == 0:
                return False
            a[i] -= 1
        for i in x:
            if a[i] != 0:
                return False
        return True

    def reorderedPowerOf2(self, N):
        if N == 0:
            return True
        n = str(N)
        l = len(n)
        i = 1
        p = []
        while len(str(i)) <= l:
            p.append(str(i))
            i = i << 1

        for t in p:
            if self.can(n, t):
                return True

        return False
