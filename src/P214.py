class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ''

        for i in reversed(range((n >> 1) + 1)):
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if l < 0:
                return ''.join(reversed(s[r:])) + s
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if l < 0:
                return ''.join(reversed(s[r:])) + s


if __name__ == '__main__':
    print(Solution().shortestPalindrome('aabba'))
