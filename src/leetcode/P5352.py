class Solution:
    def generateTheString(self, n: int) -> str:
        r = ''
        if n & 1 == 0:
            r += 'a'
            n -= 1
        else:
            if n > 2:
                r += 'ab'
                n -= 2
            else:
                r += 'a'
                n -= 1

        if n > 0:
            r += 'c' * n
        return r


if __name__ == '__main__':
    print(Solution().generateTheString(3))
