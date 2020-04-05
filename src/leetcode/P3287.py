class Solution:
    def maxProfit(self, prices):
        r = 0
        for i in range(1, len(prices)):
            r += max(prices[i] - prices[i - 1], 0)
        return r
