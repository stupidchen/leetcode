class Solution:
    def maxRotateFunction(self, A):
        n = len(A)
        s = [0] * (n + 1)
        ret, t = 0, 0
        for i in range(n):
            s[i + 1] = s[i] + A[i]
            t += i * A[i]

        ret = t
        for i in range(n):
            t -= (n - 1) * A[n - 1 - i]
            t += s[n] - A[n - 1 - i]
            ret = max(ret, t)
        return ret

if __name__ == '__main__':
    print(Solution().maxRotateFunction([4, 3, 2, 6]))
