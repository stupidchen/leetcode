class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        ret = []

        def solve(last, t, n):
            if n == N:
                ret.append(''.join(t))
                return

            if last + K < 10:
                t[n] = chr(last + K + 48)
                solve(last + K, t, n + 1)

            if last - K >= 0:
                t[n] = chr(last - K + 48)
                solve(last - K, t, n + 1)

        t = [0] * N
        for i in range(1, 10):
            t[0] = chr(i + 48)
            solve(i, t, 1)
        if N == 1:
            ret.append('0')

        ret = list(set([int(i) for i in ret]))
        return ret
