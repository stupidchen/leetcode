from bisect import bisect


class Solution:
    def fourSumCount(self, A, B, C, D):
        n = len(A)
        if n == 0:
            return 0
        s1, s2 = [], []
        for a in A:
            for b in B:
                s1.append(a + b)

        for c in C:
            for d in D:
                s2.append(c + d)

        s1 = sorted(s1)
        s2 = sorted(s2)
        t = bisect(s2, -s1[0]) - 1
        r = 0
        l = 0
        for i in range(n * n):
            if i > 0 and s1[i] == s1[i - 1]:
                r += l
                continue
            l = 0
            while t > 0 and s2[t] > -s1[i]:
                t -= 1
            while t >= 0 and s2[t] == -s1[i]:
                r += 1
                l += 1
                t -= 1
        return r


if __name__ == '__main__':
    print(Solution().fourSumCount(A=[-1, -1],
                                  B=[-1, 1],
                                  C=[-1, 1],
                                  D=[1, -1]))
