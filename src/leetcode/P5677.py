MOD = 10 ** 9 + 7


class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        i = 0
        r = 0
        while i < n:
            j = i
            while j < n and s[i] == s[j]:
                j += 1

            k = j - i
            r = (r + (k * (k + 1) >> 1)) % MOD
            i = j

        return r


if __name__ == '__main__':
    print(Solution().countHomogenous('xy'))
