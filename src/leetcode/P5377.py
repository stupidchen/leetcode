class Solution:
    def numSteps(self, s: str) -> int:
        if s == '1':
            return 0
        if s[-1] == '1':
            i = 0
            for i in reversed(range(len(s))):
                if s[i] == '0':
                    break
            n = ''
            if s[i] == '0':
                n = s[:i] + '1' + '0' * (len(s) - i - 1)
            else:
                n = '1' + '0' * len(s)
            return self.numSteps(n) + 1
        else:
            return self.numSteps(s[:-1]) + 1


if __name__ == '__main__':
    print(Solution().numSteps('1'))
