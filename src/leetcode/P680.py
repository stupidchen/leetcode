def is_palindrome(s):
    rs = ''.join(reversed(s))
    return rs == s


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if is_palindrome(s):
            return True

        for i, c in enumerate(s):
            t = -(i + 1)
            if c != s[t]:
                ts = s[:i] + s[i + 1:]
                cs = s[:t] + (s[t + 1:] if t != -1 else '')
                return is_palindrome(ts) or is_palindrome(cs)


if __name__ == '__main__':
    print(Solution().validPalindrome('abc'))
