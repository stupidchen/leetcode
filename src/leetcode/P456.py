from math import inf


class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        min_p = [inf] * n
        for i in range(1, n):
            min_p[i] = min(nums[i - 1], min_p[i - 1])
        s = []
        for i in reversed(range(n - 1)):
            t = nums[i + 1]
            s.append(t)
            while s and min_p[i] >= s[-1]:
                s.pop()
            if s and s[-1] < nums[i]:
                return True

        return False


if __name__ == '__main__':
    print(Solution().find132pattern([-2, 1, 2, -2, 1, 2]))
