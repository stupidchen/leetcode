class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1:
            return 0
        ret = 0
        if k >= n >> 1:
            for i in range(1, n):
                if prices[i] - prices[i - 1] > 0:
                    ret += prices[i] - prices[i - 1]
            return ret
        f = []
        for i in range(k + 1):
            f.append([0] * n)
        for i in range(1, k + 1):
            t = f[i - 1][0] - prices[0]
            for j in range(1, n):
                f[i][j] = f[i][j - 1]
                if prices[j] + t > f[i][j]:
                    f[i][j] = prices[j] + t
                if f[i - 1][j] - prices[j] > t:
                    t = f[i - 1][j] - prices[j]
                if f[i][j] > ret:
                    ret = f[i][j]
        return ret

if __name__ == "__main__":
    print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))