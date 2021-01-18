class Solution:
    def maxOperations(self, nums, k):
        nums = sorted(nums)
        n = len(nums)
        r = 0
        j = n - 1
        for i in range(n):
            while j > i and nums[i] + nums[j] > k:
                j -= 1
            if j > i and nums[i] + nums[j] == k:
                r += 1
                j -= 1
        return r


if __name__ == '__main__':
    print(Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6))
