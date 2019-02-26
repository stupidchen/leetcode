class Solution:
    def integerReplacement(self, n: int) -> int:
        ret = 0
        while n != 1:
            ret += 1
            if n & 1 == 0:
                n >>= 1
            else:
                if ((n >> 1) & 1 == 0) or n == 3:
                    n -= 1
                else:
                    n += 1
        return ret

if __name__ == '__main__':
    print(Solution().integerReplacement(7))
