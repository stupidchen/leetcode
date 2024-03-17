class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rs = ''.join(reversed(s))
        for i in range(1, len(s)):
            if rs.find(s[i-1:i+1]) >= 0:
                return True
        return False


if __name__ == '__main__':
    r = Solution().isSubstringPresent('leetcode')
    print(r)