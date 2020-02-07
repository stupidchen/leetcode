class Solution:
    def isEqual(self, x, y):
        d = {}
        for c in x:
            d[c] = d.setdefault(c, 0) + 1
        for c in y:
            if c not in d:
                return False
            d[c] -= 1
        for k, v in d.items():
            if v != 0:
                return False
        return True

    def numSpecialEquivGroups(self, A):
        s0 = []
        s1 = []
        n = len(A)
        if n == 0:
            return 0
        for a in A:
            s0.append(a[::2])
            s1.append(a[1::2])
        c = [i for i in range(n)]
        ret = 0
        for i in range(n):
            if c[i] == i:
                ret += 1
                for j in range(i + 1, n):
                    if self.isEqual(s0[i], s0[j]) and self.isEqual(s1[i], s1[j]):
                        c[j] = i
        return ret


if __name__ == '__main__':
    print(Solution().numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]))
