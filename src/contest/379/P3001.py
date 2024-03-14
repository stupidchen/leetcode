class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if e == a and (e != c or (d - b) * (d - f) >= 0):
            return 1

        if b == f and (d != f or (c - a) * (c - e) >= 0):
            return 1

        if e - f == c - d and (a - b != e - f or (a - c) * (a - e) >= 0):
            return 1

        if e + f == c + d and (a + b != e + f or (a - c) * (a - e) >= 0):
            return 1

        return 2


if __name__ == '__main__':
    r = Solution().minMovesToCaptureTheQueen(1, 1, 1, 4, 1, 8)
    print(r)
