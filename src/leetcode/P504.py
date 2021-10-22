class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        r = ''
        n = False
        if num < 0:
            num = -num
            n = True
        while num > 0:
            r = str(num % 7) + r
            num = num // 7
        if n:
            r = '-' + r
        return r
