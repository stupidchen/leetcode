MOD = 10 ** 9 + 7


class Solution:
    def numSubseq(self, nums, target):
        m = max(nums)
        n = len(nums)
        d = [0] * (m + 1)
        for num in nums:
            d[num] += 1

        s = [0] * (m + 1)
        for i in range(1, m + 1):
            s[i] = s[i - 1] + d[i]

        r = 0
        for i in range(1, m + 1):
            if d[i] != 0 and i <= target:
                k = target - i
                hi = i
                lo = min(k, i - 1)
                t = (pow(2, d[hi], MOD) - 1) * (pow(2, s[lo], MOD) - 1) % MOD * pow(2, s[hi - 1] - s[lo], MOD) % MOD
                r = (r + t) % MOD
                if i << 1 <= target:
                    r = (r + (pow(2, d[hi], MOD) - 1)) % MOD

        return r


if __name__ == '__main__':
    print(Solution().numSubseq([2,9,4,3,6,9,1,1], 6))
