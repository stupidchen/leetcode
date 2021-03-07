class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s == '':
            return True

        while s and s[0] == '1':
            s = s[1:]
        try:
            s.index('1')
        except ValueError:
            return True
        return False


if __name__ == '__main__':
    print(Solution().checkOnesSegment(''))
