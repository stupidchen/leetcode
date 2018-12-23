def lowbit(x):
    return x & (x ^ (x - 1))

MAXL = 50003

class Solution:

    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        f = [-1] * MAXL
        ret = 0
        for i in range(n):
            t = A[i] + 1
            m = -1
            while t != 0:
                if f[t] != -1:
                    m = f[t] if m == -1 or m > f[t] else m
                t -= lowbit(t)
            t = A[i] + 1
            while t < MAXL:
                if f[t] == -1:
                    f[t] = i
                t += lowbit(t)
            if m != -1:
                ret = max(ret, i - m)

        return ret

if __name__ == '__main__':
    print(Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
