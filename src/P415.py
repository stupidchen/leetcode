class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        for i in range(len(num2) - len(num1)):
            num1 = '0' + num1

        k = 0
        ret = []
        n = len(num2)
        for i in range(n):
            t = int(num1[n - i - 1]) + int(num2[n - i - 1]) + k
            k = t // 10
            ret.append(str(t % 10))
        if k != 0:
            ret.append(str(k))

        return (''.join(ret))[::-1]


if __name__ == '__main__':
    print(Solution().addStrings('10', '1'))
