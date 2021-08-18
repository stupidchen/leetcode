from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def is_valid(num_str):
            if num_str == '' or num_str[0] == '0':
                return False

            num = int(num_str)
            return 1 <= num <= 26

        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n):
            for j in range(i + 1):
                if is_valid(s[j:i + 1]):
                    f[i + 1] += f[j]
        return f[n]


if __name__ == '__main__':
    print(Solution().numDecodings('226'))
