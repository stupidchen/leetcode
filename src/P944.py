class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0
        m = len(A[0])
        ret = 0
        for i in range(m):
            t = False
            for j in range(n - 1):
                if A[j][i] > A[j + 1][i]:
                    t = True
                    break
            if t:
                ret += 1
        return ret
