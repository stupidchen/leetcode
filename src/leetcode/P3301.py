class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        l, r = 0, 0
        for i in range(n):
            if s[i] == '(' or s[i] == '*':
                l += 1
            else:
                l -= 1

            if s[n - i - 1] == ')' or s[n - i - 1] == '*':
                r += 1
            else:
                r -= 1

            if l < 0 or r < 0:
                return False

        return True


if __name__ == '__main__':
    print(Solution().checkValidString("((*())"))
