class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2] + [0] * max(0, n - 3)
        ans = 0
        r, w = 0, 0
        while True:
            num = 1 + (s[w - 1] & 1)
            for _ in range(s[r]):
                s[w] = num
                ans += (num == 1)
                w += 1
                if w == n:
                    return ans
            r += 1
