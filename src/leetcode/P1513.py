MOD = 10 ** 9 + 7


class Solution:
    def numSub(self, s: str) -> int:
        s = s + '0'
        n = len(s)
        r = 0
        t = 0
        for i in range(n):
            if s[i] == '0':
                r = (r + (t * (t + 1) >> 1)) % MOD
                t = 0
            else:
                t += 1
        return r


if __name__ == '__main__':
    print(Solution().numSub('0110111'))
