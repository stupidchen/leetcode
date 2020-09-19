from math import inf


class Solution:
    def minSubarray(self, nums, p):
        s = sum(nums)
        n = len(nums)
        m = s % p
        if m == 0:
            return 0
        r = inf
        l = {0: -1}
        t = 0
        for i in range(n):
            num = nums[i]
            t += num
            q = (t - m) % p
            if q in l:
                r = min(r, i - l[q])
            l[t % p] = i
        if r == inf or r == n:
            r = -1
        return r


if __name__ == '__main__':
    print(Solution().minSubarray(nums=[2, 2, 3], p=6))
