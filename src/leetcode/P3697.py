class Solution:
    def isIdealPermutation(self, A):
        n = len(A)
        m = -1
        for i in range(1, n):
            if A[i] < m:
                return False
            else:
                m = max(A[i - 1], m)

        return True
