class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = 0
        i3 = 0
        i5 = 0
        f = [1]
        ret = 1
        for i in range(n - 1):
            t = min(f[i2] * 2, f[i3] * 3, f[i5] * 5)
            if t == f[i2] * 2:
                i2 += 1
            if t == f[i3] * 3:
                i3 += 1
            if t == f[i5] * 5:
                i5 += 1
            f.append(t)
        return f[n - 1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber(1690))
