class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        f = [0] * n
        rf = [0] * n
        f[0] = 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                f[i] = f[i - 1] + 1
            else:
                f[i] = 1
        rf[n - 1] = 1
        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                rf[i] = rf[i + 1] + 1
            else:
                rf[i] = 1

        ret = 0
        for i in range(n):
            if f[i] > rf[i]:
                ret += f[i]
            else:
                ret += rf[i]
        return ret


if __name__ == '__main__':
    print(Solution().candy([1,2,2]))
