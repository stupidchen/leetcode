class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        def cal(x, y):
            r = 0
            for i in range(n):
                if x[i] != y[i]:
                    r += 1
            return r

        s1 = ''
        s2 = ''
        for i in range(n):
            s1 += str(i & 1)
            s2 += str((i + 1) & 1)

        return min(cal(s1, s), cal(s2, s))


if __name__ == '__main__':
    print(Solution().minOperations("0100"))
