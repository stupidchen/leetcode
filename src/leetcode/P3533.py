class Solution:
    def longestMountain(self, A):
        n = len(A)
        if n == 0:
            return 0
        f = [0] * n
        rf = [0] * n
        f[0] = 1
        for i in range(1, n):
            if A[i] > A[i - 1]:
                f[i] = f[i - 1] + 1
            else:
                f[i] = 1
        rf[n - 1] = 1
        for i in range(n - 2, 0, -1):
            if A[i] > A[i + 1]:
                rf[i] = rf[i + 1] + 1
            else:
                rf[i] = 1

        ans = 0
        for i in range(n):
            t = 0
            if f[i] != 1 and rf[i] != 1:
                t = f[i] + rf[i] - 1
            if t > ans:
                ans = t
        return ans
