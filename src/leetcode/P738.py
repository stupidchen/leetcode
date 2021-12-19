class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        s = str(n)
        m = len(s)
        r = [0] * m
        t = -1
        while t != m - 1:
            min_c = 'a'
            min_p = -1
            for i in range(t + 1, m):
                if min_c > s[i]:
                    min_c = s[i]
                    min_p = i

            for i in range(t + 1, min_p + 1):
                r[i] = min_c
            t = min_p

        rr = 0
        for i in range(m):
            if i == 0 or s[i] > s[i - 1]:
                rr = max(rr, int(''.join(s[:i] + chr(ord(s[i]) - 1) + '9' * (m - i - 1))))
            if i > 0 and s[i] < s[i - 1]:
                break
        r = max(int(''.join(r)), rr)
        return r


if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(0))
