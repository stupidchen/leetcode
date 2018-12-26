class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = [-1] * (amount + 1)
        f[0] = 0
        for i in range(len(coins)):
            for j in range(amount - coins[i] + 1):
                if f[j] != -1:
                    f[j + coins[i]] = f[j] + 1 if f[j + coins[i]] == -1 or f[j + coins[i]] > f[j] + 1 else f[j + coins[i]]

        return f[amount]
