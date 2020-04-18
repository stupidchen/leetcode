MOD = 10 ** 9 + 7


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n):
            for j in range(min(i + 1, 9)):
                if s[i - j] != '0':
                    t = int(s[i - j: i + 1])
                    if t > k:
                        break
                    f[i + 1] = (f[i + 1] + f[i - j]) % MOD
        return f[n]


if __name__ == '__main__':
    print(Solution().numberOfArrays("1317", 2000))
