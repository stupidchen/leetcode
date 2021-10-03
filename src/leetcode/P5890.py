class Solution:
    def minimumMoves(self, s: str) -> int:
        r = 0
        n = len(s)
        for i in range(n - 2):
            if s[i] == 'X':
                s = s[:i] + 'O' * 3 + s[i + 3:]
                r += 1
        if s[n - 1] == 'X' or s[n - 2] == 'X':
            r += 1
        return r


if __name__ == '__main__':
    print(Solution().minimumMoves('OXOX'))
