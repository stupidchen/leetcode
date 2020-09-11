class Solution:
    def maxProduct(self, nums):
        p = n = 1
        r = nums[0]
        for num in nums:
            if num == 0:
                p = n = 1
                r = max(0, r)
                continue

            if num > 0:
                n *= num
                p *= num
                r = max(p, r)
            else:
                t = p
                p = n * num
                n = t * num
                r = max(p, r)
                if p < 0:
                    p = 1
        return r


if __name__ == '__main__':
    print(Solution().maxProduct([2, -5, -2, -4, 3]))
