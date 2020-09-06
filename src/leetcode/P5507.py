class Solution:
    def modifyString(self, s: str) -> str:
        r = ''
        for i in range(len(s)):
            if s[i] == '?':
                for j in range(26):
                    c = chr(j + 97)
                    if (i == 0 or c != r[i - 1]) and (i == len(s) - 1 or c != s[i + 1]):
                        r += c
                        break
            else:
                r += s[i]
        return r


if __name__ == '__main__':
    print(Solution().modifyString('a???a'))
