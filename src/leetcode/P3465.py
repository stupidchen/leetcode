class Solution:
    def sequentialDigits(self, low: int, high: int):
        ll = len(str(low))
        rr = len(str(high))
        r = []

        def solve(c, m, s, t):
            if c == m:
                if low <= s <= high:
                    r.append(s)
                return
            if t > 9:
                return
            solve(c + 1, m, s * 10 + t, t + 1)

        for i in range(ll, rr + 1):
            for j in range(9):
                solve(0, i, 0, j + 1)
        return list(sorted(r))


if __name__ == '__main__':
    print(Solution().sequentialDigits(100, 300))
