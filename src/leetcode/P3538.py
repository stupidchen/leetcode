class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        f = [0] * 10
        digits = set([int(digit) for digit in digits])
        for i in range(1, 10):
            f[i] = f[i - 1]
            if i in digits:
                f[i] += 1

        sn = str(n)
        r = 0
        m = len(sn)
        for i in range(m + 1):
            if i > 0 and int(sn[i - 1]) not in digits:
                break

            if i == m:
                r += 1
                break

            if int(sn[i]) > 0:
                t = f[int(sn[i]) - 1]
                r += t * (f[9] ** (m - i - 1))

        t = 1
        for i in range(m - 1):
            t *= f[9]
            r += t

        return r


if __name__ == '__main__':
    print(Solution().atMostNGivenDigitSet(digits=["3", "4", "8"], n=4))
    print(Solution().atMostNGivenDigitSet(digits=["1", "3", "5", "7"], n=314752))
