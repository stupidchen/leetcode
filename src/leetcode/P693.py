class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        t = n & 1
        n = n >> 1
        while n > 0:
            b = n & 1
            if b == t:
                return False
            t = b
            n = n >> 1
        return True


if __name__ == '__main__':
    print(Solution().hasAlternatingBits(4))
