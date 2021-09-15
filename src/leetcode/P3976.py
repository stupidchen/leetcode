class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        f = [1] * n
        g = [1] * n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                f[i] = g[i - 1] + 1
            if A[i] < A[i - 1]:
                g[i] = f[i - 1] + 1

        return max(f + g)
