from collections import defaultdict

MOD = 10 ** 9 + 7


class Solution:
    def countNicePairs(self, nums):
        def rev(x):
            return int(str(x)[::-1])

        c = defaultdict(lambda: 0)
        for i, num in enumerate(nums):
            t = num - rev(num)
            c[t] += 1

        r = 0
        for k, v in c.items():
            r = (r + (v * (v - 1) >> 1)) % MOD
        return r


if __name__ == '__main__':
    print(Solution().countNicePairs([42, 11, 1, 97]))
