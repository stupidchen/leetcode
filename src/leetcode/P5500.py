class Solution:
    def getMaxLen(self, nums):
        r = 0
        m = c = 0
        n = len(nums)
        for i in range(n):
            t = nums[i]
            c += 1
            if t > 0:
                if m % 2 == 0:
                    r = max(r, c)
            elif t < 0:
                m += 1
                if m % 2 == 0:
                    r = max(r, c)
            else:
                m = c = 0

        m = c = 0
        for i in reversed(range(n)):
            t = nums[i]
            c += 1
            if t > 0:
                if m % 2 == 0:
                    r = max(r, c)
            elif t < 0:
                m += 1
                if m % 2 == 0:
                    r = max(r, c)
            else:
                m = c = 0

        return r


if __name__ == '__main__':
    print(Solution().getMaxLen([-1, -2, -3, 0, 1]))
