class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        l = 0
        r = -1
        ans = 0
        ret = 0
        for i in range(n):
            ans += nums[i]
            r += 1
            while ans >= s:
                if r - l + 1 < ret or ret == 0:
                    ret = r - l + 1
                ans -= nums[l]
                l += 1
        return ret


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [7]))