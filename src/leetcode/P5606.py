class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        r = ''
        t = (26 * n - k) // 25
        r += 'a' * t
        k -= t
        l = 2
        for i in range(t, n):
            j = 0
            for j in range(l, 27):
                if n - i - 1 <= k - j <= 26 * (n - i - 1):
                    break
            r += chr(96 + j)
            k -= j
            l = j
        return r


if __name__ == '__main__':
    print(Solution().getSmallestString(3, 27))
