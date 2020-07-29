class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        f = [[0, 0] for i in range(n)]
        for i in range(1, n):
            for j in range(i - 1):
                if f[j][1] > f[i][0]:
                    f[i][0] = f[j][1]

            for j in range(i):
                t = f[j][0] + prices[i] - prices[j]
                if t > f[i][1]:
                    f[i][1] = t

        m = 0
        for i in range(1, n):
            if f[i][1] > m:
                m = f[i][1]

        return m


# For test only
SI = (([1, 2, 3, 0, 2],),)
SO = (3,)
TM = 'maxProfit'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
