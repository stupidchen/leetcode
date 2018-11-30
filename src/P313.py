class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = [0] * n
        ret[0] = 1
        m = len(primes)
        f = [0] * m
        for i in range(1, n):
            t = min([primes[j] * ret[f[j]] for j in range(m)])
            ret[i] = t
            for j in range(m):
                if t == primes[j] * ret[f[j]]:
                    f[j] += 1
        return ret[-1]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
