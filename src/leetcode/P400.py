class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        tmp = 0
        while tmp < n:
            tmp += i * (10 ** i - 10 ** (i - 1))
            i += 1

        i -= 1
        tmp -= i * (10 ** i - 10 ** (i - 1))
        num = (n - tmp - 1) // i + 10 ** (i - 1)
        index = (n - tmp) - (n - tmp - 1) // i * i
        return int(str(num)[index - 1])


if __name__ == '__main__':
    print(Solution().findNthDigit(9))
