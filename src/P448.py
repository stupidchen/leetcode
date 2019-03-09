class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            t = i + 1
            while nums[t - 1] != t and nums[t - 1] != 0:
                if nums[t - 1] != nums[nums[t - 1] - 1]:
                    k = nums[t - 1]
                    nums[t - 1] = nums[nums[t - 1] - 1]
                    nums[k - 1] = k
                else:
                    nums[t - 1] = 0

        ret = []
        for i in range(n):
            if nums[i] == 0:
                ret.append(i + 1)
        return ret

if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
