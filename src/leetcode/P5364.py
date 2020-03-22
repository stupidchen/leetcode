class Solution:
    def createTargetArray(self, nums, index):
        n = len(nums)
        r = []
        for i in range(n):
            r.insert(index[i], nums[i])
        return r


if __name__ == '__main__':
    print(Solution().createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
