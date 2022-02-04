class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        n = len(s)
        for i in range(n):
            if s[i] == '6':
                return int(s[:i] + '9' + s[i + 1:])
        return num
