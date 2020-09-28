class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        r = 0
        p = 1
        l = 0
        for i in range(n):
            p *= nums[i]
            while p >= k and l <= i:
                p //= nums[l]
                l += 1
            r += i - l + 1
        return r


if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK(nums=[1, 1, 1, 1, 1], k=5))
