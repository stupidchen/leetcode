class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        n = len(A)
        l = 0
        r = 0
        s = 0
        ret = 0
        f = [0] * (n + 2)
        for i in reversed(range(n)):
            if A[i] != 0:
                f[i] = 0
            else:
                f[i] = f[i + 1] + 1
        while l < n:
            if l >= r:
                r = l + 1
                s = A[l]
            while r < n and s < S:
                s += A[r]
                r += 1
            if s == S:
                ret += 1 + f[r]
            s -= A[l]
            l += 1
        return ret


if __name__ == '__main__':
    print(Solution().numSubarraysWithSum([1, 2, 1, 2, 1, 1], 6))
