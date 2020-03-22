class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for i in range(1, n):
            if s[:n - i] == s[i:]:
                return s[i:]
        return ''


if __name__ == '__main__':
    print(Solution().longestPrefix("aa"))
    print(Solution().longestPrefix("level"))
    print(Solution().longestPrefix("ababab"))
    print(Solution().longestPrefix("leetcodeleet"))
    print(Solution().longestPrefix("a"))
