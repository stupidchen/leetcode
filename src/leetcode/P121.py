from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        c = 0
        for i in range(1, len(prices)):
            c = max(0, prices[i] - prices[i - 1] + c)
            r = max(r, c)
        return r
