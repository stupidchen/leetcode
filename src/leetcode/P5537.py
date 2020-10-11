class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        if n == 1:
            return True

        def validate(x, l, r, d):
            if l > r:
                d[l] = True
            else:
                t = validate(x, l + 1, r - 1, d)
                if x[l] == x[r]:
                    d[l] = t
                else:
                    d[l] = False

            return d[l]

        def solve(x, y):
            dx = [False] * n
            validate(x, 0, n - 1, dx)
            dy = [False] * n
            validate(y, 0, n - 1, dy)

            ix = 0
            iy = n - 1
            while ix <= iy and x[ix] == y[iy]:
                ix += 1
                iy -= 1
                if dx[ix] or dy[ix]:
                    return True
            if ix > iy or dx[ix] or dy[ix]:
                return True

            return False

        return solve(a, b) or solve(b, a)


if __name__ == '__main__':
    print(Solution().checkPalindromeFormation("aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd",
                                              "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"))
    print(Solution().checkPalindromeFormation(a="xxx", b="aba"))
    print(Solution().checkPalindromeFormation(a="abcd", b="abcd"))
