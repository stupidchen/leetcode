class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        for i in range(k):
            t = len(num) - 1
            for j in range(len(num) - 1):
                if num[j] > num[j + 1]:
                    t = j
                    break
            num = num[:t] + num[t + 1:]
        if len(num) == 0:
            return '0'
        while len(num) > 1 and num[0] == '0':
            num = num[1:]
        return num


if __name__ == '__main__':
    print(Solution().removeKdigits("1", 2))
