class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        nums = nums + nums

        r = [-1] * n
        s = []
        for i in range(n << 1):
            while s and nums[s[-1]] < nums[i % n]:
                r[s[-1]] = nums[i % n]
                s.pop()
            if i < n:
                s.append(i)

        return r


if __name__ == '__main__':
    print(Solution().nextGreaterElements([1, 2, 1, 3, 4]))
