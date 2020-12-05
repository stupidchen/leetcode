class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        m = len(flowerbed)
        for i, v in enumerate(flowerbed):
            if v == 0 and (i == 0 or (i > 0 and flowerbed[i - 1] == 0)) and (i == m - 1 or (i < m - 1 and flowerbed[i + 1] == 0)):
                n -= 1
                if n <= 0:
                    break
                flowerbed[i] = 1
        return n <= 0


if __name__ == '__main__':
    print(Solution().canPlaceFlowers([0, 0], 2))
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
