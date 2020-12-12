MAX = 10 ** 4 + 2

class Solution:
    def getSumAbsoluteDifferences(self, nums):
        f = [0] * MAX
        for num in nums:
            f[num] += 1
        d = [0] * MAX
        t = c = 0
        for i in range(1, MAX):
            d[i] += t
            c += f[i]
            t += c

        t = c = 0
        for i in reversed(range(1, MAX)):
            d[i] += t
            c += f[i]
            t += c

        n = len(nums)
        r = [0] * n
        for i in range(n):
            r[i] = d[nums[i]]

        return r


if __name__ == '__main__':
    print(Solution().getSumAbsoluteDifferences([2, 3, 5]))
