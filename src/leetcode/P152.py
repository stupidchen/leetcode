class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return None
        l = 1
        r = 1
        ans = nums[0]
        for i in range(n):
            if nums[i] == 0:
                l = 1
                r = 1
                if 0 > ans:
                    ans = 0
                continue
            if nums[i] > 0:
                l = l * nums[i]
                r = r * nums[i]
                if r > ans:
                    ans = r
                continue
            if nums[i] < 0:
                t = l
                l = r * nums[i]
                r = t * nums[i]
                if r > ans:
                    ans = r
                if r < 0:
                    r = 1
                continue
        return ans


if __name__ == '__main__':
    print(Solution().maxProduct([3, -1, 4]))
