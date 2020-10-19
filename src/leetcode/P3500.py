from collections import defaultdict


class Solution:
    def minDominoRotations(self, A, B):
        d = defaultdict(lambda: 0)
        n = len(A)
        for i in range(n):
            d[A[i]] += 1
            if A[i] != B[i]:
                d[B[i]] += 1

        ra = rb = 0
        found = False
        for k, v in d.items():
            if v >= n:
                for i in range(n):
                    if A[i] != k:
                        ra += 1
                    if B[i] != k:
                        rb += 1
                found = True
        if not found:
            return -1
        return min(ra, rb)
