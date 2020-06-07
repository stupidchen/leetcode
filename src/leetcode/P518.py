class Solution:
    def change(self, amount, coins):
        f = [0] * (amount + 1)
        f[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                f[i] += f[i - coin]
        return f[amount]


if __name__ == '__main__':
    print(Solution().change(amount=5, coins=[1, 2, 5]))
