class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            while nums[num - 1] != num:
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
                num = nums[i]

        ret = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ret.append(nums[i])
        return ret

if __name__ == "__main__":
    print(Solution().findDuplicates([[4,3,2,7,8,2,3,1]]))
