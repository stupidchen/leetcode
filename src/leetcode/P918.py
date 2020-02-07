class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        f = 0
        ret = -0xffffffff
        n = len(A)
        for i in range(n):
            if f >= 0:
                f = f + A[i]
            else:
                f = A[i]
            ret = max(f, ret)
        t = [0] * n
        s = 0
        for i in range(n):
            s += A[i]
            if i > 0:
                t[i] = max(s, t[i - 1])
            else:
                t[i] = s
        b = [0] * n
        s = 0
        for i in reversed(range(n)):
            s += A[i]
            if i < n - 1:
                b[i] = max(s, b[i + 1])
            else:
                b[i] = s
        for i in range(n - 1):
            ret = max(ret, t[i] + b[i + 1])
        return ret


if __name__ == '__main__':
    print(Solution().maxSubarraySumCircular([-2,-3,-1]))
