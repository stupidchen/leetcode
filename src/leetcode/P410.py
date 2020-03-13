class Solution:
    def splitArray(self, nums, m):
        n = len(nums)

        def valid(s):
            ts = 0
            p = 1
            for i in range(n):
                if ts + nums[i] <= s:
                    ts += nums[i]
                else:
                    p += 1
                    if p > m:
                        return False
                    ts = nums[i]
                    if ts > s:
                        return False
            return True

        l, r = 0, sum(nums)
        while l < r:
            mid = (l + r) >> 1
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return r


if __name__ == '__main__':
    print(Solution().splitArray([1, 10000], 2))
