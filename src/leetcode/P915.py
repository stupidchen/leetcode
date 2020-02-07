class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        m = [0] * n
        m[n - 1] = A[n - 1]
        for i in reversed(range(n - 1)):
            m[i] = min(A[i], m[i + 1])

        t = -1
        for i in range(n - 1):
            t = max(A[i], t)
            if t <= m[i + 1]:
                return i + 1