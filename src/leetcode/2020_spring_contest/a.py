class Solution:
    def minCount(self, coins):
        r = 0
        for coin in coins:
            r += (coin + 1) >> 1
        return r


if __name__ == '__main__':
    print(Solution().minCount([2, 3, 10]))
