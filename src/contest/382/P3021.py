class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_n, even_m = n >> 1, m >> 1
        odd_n, odd_m = n - even_n, m - even_m
        return even_n * odd_m + odd_n * even_m


if __name__ == '__main__':
    r = Solution()
    print(r.flowerGame(3, 1))
