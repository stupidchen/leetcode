class Solution:
    def minSubsequence(self, nums):
        r = []
        nums = sorted(nums, reverse=True)
        s = sum(nums)
        t = 0
        for num in nums:
            t += num
            r.append(num)
            if t > s >> 1:
                break

        return r


if __name__ == '__main__':
    print(Solution().minSubsequence([4, 3, 10, 9, 8]))
