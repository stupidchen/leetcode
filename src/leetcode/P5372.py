class Solution:
    def minStartValue(self, nums):
        r, t = 1, 0
        for num in nums:
            t += num
            if t < 0 and -t + 1 > r:
                r = -t + 1
        return r


if __name__ == '__main__':
    print(Solution().minStartValue([1, -2, -3]))
