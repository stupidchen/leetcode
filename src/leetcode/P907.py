from math import log, ceil, floor

MODULO = 10 ** 9 + 7

f = []
id = []
lg = {}

class Solution:

    def findMin(self, l, r):
        t = lg[r - l]
        ret = min(f[l][t], f[r - (1 << t) + 1][t])
        if ret == f[l][t]:
            index = id[l][t]
        else:
            index = id[r - (1 << t) + 1][t]
        return index, ret

    def solve(self, l, r):
        if l > r:
            return 0
        if r - l == 0:
            return f[l][0]
        index, value = self.findMin(l, r)
        ret = ((index - l + 1) * (r - index + 1) % MODULO * value) % MODULO
        return ((ret + self.solve(l, index - 1)) % MODULO + self.solve(index + 1, r)) % MODULO

    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        m = int(ceil(log(n) / log(2)))
        global f
        global id
        global lg
        f = []
        id = []
        lg = {}
        for i in range(1, n):
            lg[i] = int(floor(log(i) / log(2)))
        for i in range(n):
            f.append([0] * (m + 1))
            id.append([-1] * (m + 1))
            f[i][0] = A[i]
            id[i][0] = i
        for j in range(1, m + 1):
            for i in range(n):
                f[i][j] = f[i][j - 1]
                if i + (1 << (j - 1)) < n:
                    f[i][j] = min(f[i][j], f[i + (1 << (j - 1))][j - 1])
                if f[i][j] == f[i][j - 1]:
                    id[i][j] = id[i][j - 1]
                else:
                    id[i][j] = id[i + (1 << (j - 1))][j - 1]
        return self.solve(0, n - 1)


if __name__ == '__main__':
    print(Solution().sumSubarrayMins([95, 58, 46, 67, 100]))
