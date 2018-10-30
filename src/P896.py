class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        n = 0
        p = 0
        for i in range(0, len(A) - 1):
            if A[i] - A[i + 1] > 0:
                n += 1
            if A[i] - A[i + 1] < 0:
                p += 1
        if n != 0 and p != 0:
            return False
        return True