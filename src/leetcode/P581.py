class Solution:
    def findUnsortedSubarray(self, nums):
        p = [(nums[0], nums[0])]
        s = [(nums[-1], nums[-1])]
        n = len(nums)
        for i in range(1, n):
            p.append((min(p[-1][0], nums[i]), max(p[-1][1], nums[i])))
        for i in reversed(range(n - 1)):
            s = [(min(s[0][0], nums[i]), max(s[0][1], nums[i]))] + s

        i = 0
        while i < n - 1 and nums[i] <= nums[i + 1] and p[i][1] <= s[i + 1][0]:
            i += 1

        j = n - 1
        while j >= i and nums[j] >= nums[j - 1] and p[j - 1][1] <= s[j][0]:
            j -= 1

        return j - i + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([2, 3, 3, 2, 4]))
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
